import numpy as np
import reachab
import igraph
"""
    only one cycle of reachability analysis
"""
def only_one_reachability(params):
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
         'g': np.matrix([[1, 0],
                         [1, 1],
                         [0, 0],
                         [0, 0]
                         ])
         }
    zonoset=reachab.reach(Omega_0, U, params)


