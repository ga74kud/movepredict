import matplotlib.pyplot as plt
import reachab
import numpy as np
import md_pro as md
import logging



def only_mdp(params):
    strt_pnt = '0'
    P = md.get_meshgrid_points(params)
    x,y,z=get_xyz(P)
    # Topology
    T, S = md.get_simple_topology_for_regular_grid(params, P)
    # rewards
    R = {'35': 100}
    mdp_challenge = {'S': S, 'R': R, 'T': T, 'P': P}
    dict_mdp = md.start_mdp(params, mdp_challenge)
    reach_set = md.reach_n_steps(strt_pnt, mdp_challenge, dict_mdp, params, steps=8)
    optimal_traj = md.get_trajectory(strt_pnt, dict_mdp, reach_set)
    scatter_value_function(x, y, np.array(dict_mdp['U']), dict_mdp, R, optimal_traj)
    plt_show()
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
    zonoset = reachab.reach(Omega_0, U, params)

def scatter_value_function(x, y, value_function, dict_mdp, R, optimal_traj):
    fig, ax = plt.subplots()
    S=dict_mdp['S']
    N=len(x)
    colors = value_function
    area = 30 * np.ones((N,1))
    plt.scatter(x, y, s=area, c=colors, alpha=0.5)

    for idx, txt in enumerate(S):
        if(txt in R):
            new_txt=txt+"("+str(R[txt])+")"
            plt.annotate(new_txt, (x[idx], y[idx]), color='red')
        else:
            plt.annotate(txt, (x[idx], y[idx]))
def plt_show():
    plt.xlabel('x')
    plt.ylabel('y')
    plt.show()

def get_xyz(P):
    x = np.array([P[i][0] for i in P])
    y = np.array([P[i][1] for i in P])
    z = np.array([P[i][2] for i in P])
    return x,y,z