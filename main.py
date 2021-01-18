# -------------------------------------------------------------
# code developed by Michael Hartmann during his Ph.D.
# Movement Prediction
#
# (C) 2020 Michael Hartmann, Graz, Austria
# Released under GNU GENERAL PUBLIC LICENSE
# email michael.hartmann@v2c2.at
# -------------------------------------------------------------
from source.preprocessing.dataprocessing import *
import reachab
import numpy as np
import logging
import argparse
import definitions
def test_zonoset_computation(params):
    Omega_0 = {'c': np.matrix([[0],
                               [0],
                               [10],
                               [3]
                               ]),
               'g': np.matrix([[1, -1],
                               [1, 1],
                               [0, 0],
                               [0, 0]
                               ])
               }
    U = {'c': np.matrix([[0],
                         [0],
                         [0],
                         [0],
                         ]),
         'g': np.matrix([[1, 0, 1],
                         [1, 1, 0],
                         [0, 0, 0],
                         [0, 0, 0]
                         ])
         }
    zonoset=reachab.reach(Omega_0, U, params)
    logging.info("Numbers in num_list are: {}".format(' '.join(map(str, zonoset))))
    obj=dataprocessing(params)
    None


def test_reachab():
    reachab.test_me()
def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--box_function', '-box', type=str, help='choices: without_box, with_box',
                        default='without_box', required=False)
    parser.add_argument('--visualization', '-vis', type=str, help='y, n',
                        default='y', required=False)
    parser.add_argument('--time_horizon', '-T', type=float, help='value like: T=2.2', default=2.2, required=False)
    parser.add_argument('--steps', '-N', type=int, help='value like N=4', default=4, required=False)
    parser.add_argument('--debug', '-deb', type=str, help='(y,n)', default='n', required=False)
    parser.add_argument('--window_x', '-wix', type=int, help='windowsize in x-direction for savgol_filter', default=101, required=False)
    parser.add_argument('--window_y', '-wiy', type=int, help='windowsize in y-direction for savgol_filter', default=101, required=False)
    parser.add_argument('--poly_x', '-pox', type=int, help='polygon order in x-direction for savgol_filter', default=2, required=False)
    parser.add_argument('--poly_y', '-poy', type=int, help='polygon order in y-direction for savgol_filter', default=2, required=False)

    args = parser.parse_args()
    params = vars(args)
    params['PROJECT_ROOT']=get_project_root()
    if (params['debug'] == 'y'):
        logging.basicConfig(format='%(levelname)s:%(message)s', level=logging.DEBUG)
    test_zonoset_computation(params)
if __name__ == '__main__':
    main()
