import os
import datareader
import reachab
import logging
class main_loop(object):
    def __init__(self, params, **kwargs):
        self.paths={"annotation": None, "image": None}
        self.params=params
        self.datasets={'X': None, 'Y': None}

    """
        initial steps: get the paths for the dataset annotation and reference image
    """
    def init_datareader(self):
        path = datareader.__path__[0]
        location = "bookstore"
        video = "video0"
        self.paths["annotation"] = os.path.join(path, "data/input/stanford/", location, video, "annotations.txt")
        self.paths["image"] = os.path.join(path, "data/input/stanford/", location, video, "reference.jpg")

    """
        read the whole dataset
    """
    def get_the_whole_dataset(self):
        ################################
        ###     read the dataset     ###
        ################################
        self.datasets['X'] = datareader.read_dataset(self.params, self.paths["annotation"])
        logging.info(self.datasets['X'])

    """
        get a selection of the dataset
    """
    def get_the_dataset_from_time_range(self, tmin, tmax):
        #################################
        ### read the dataset by range ###
        #################################
        self.datasets['Y'] = datareader.get_dataset_by_range(self.datasets['X'], 't', tmin, tmax)
        logging.info(self.datasets['Y'])

    """
        show rectangles from the annotation
    """
    def show_rectangles(self, timestamp):
        ###############################################
        ### plot rectangles for a specific timstamp ###
        ###############################################
        self.img = datareader.read_background_picture(self.paths["image"])
        self.img = datareader.plot_rectangle_for_timestamp(self.img, self.datasets['X'], timestamp)
    """
        show and hold the image
    """
    def show_and_hold(self):
        datareader.show_and_hold("", self.img)

    """
        main loop to run from frame to frame
    """
    def run_loop(self):
        self.init_datareader()
        self.get_the_whole_dataset()
        self.get_the_dataset_from_time_range(8520, 8531)
        self.show_rectangles(8524)
        self.show_rectangles(8531)
        #self.show_and_hold()

    """
        for one id perform reachability analysis
    """
    def run_loop_one_id(self):
        init_frame=10
        self.init_datareader()
        self.get_the_whole_dataset()
        r,Y=datareader.get_dataset_by_column_value(self.datasets['X'], "t", init_frame)
        id_array = datareader.get_all_ids(Y)
