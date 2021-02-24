import numpy as np
import reachab as rb
import matplotlib.pyplot as plt
import md_pro as md

def mdp_reachab():
    Omega_0 = {'c': np.matrix([[80],
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
         'g': np.matrix([[1, 0],
                         [1, 1],
                         [0, 0],
                         [0, 0]
                         ])
         }
    # zonoset=reach(Omega_0, U, params)
    R, X, obj_reach, zonoset = rb.reach_zonotype_without_box(Omega_0, U,
                                                          **{"time_horizon": 2.2, "steps": 4, "visualization": "y",
                                                             "face_color": "green"})
    all_inside_points = rb.get_sample_points_inside_hull(zonoset)
    rb.plot_all_inside_points(all_inside_points)
    plt.grid()
    plt.show()

if __name__ == '__main__':
    mdp_reachab()