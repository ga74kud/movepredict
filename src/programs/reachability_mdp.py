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
    reach_set = md.reach_n_steps(strt_pnt, mdp_challenge, dict_mdp, params, steps=10)
    optimal_traj = md.get_stochastic_trajectory(strt_pnt, dict_mdp, steps=20)
    print_info(dict_mdp, optimal_traj)
    plot_topology(x, y, dict_mdp)
    plot_arrows_path(x, y, optimal_traj)
    scatter_value_function(x, y, np.array(dict_mdp['U']), dict_mdp, R)
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
    #zonoset = reachab.reach(Omega_0, U, params)
def print_info(dict_mdp, optimal_traj):
    print(optimal_traj)
    for idx, wlt in enumerate(optimal_traj):
        print("cycle " + str(idx) + " node: "+ wlt)
        print(md.get_U_for_agent_neighbours(dict_mdp, wlt))


def plot_topology(x, y, dict_mdp):
    for me_too in dict_mdp['S']:
        my_actions=dict_mdp['action'][me_too]
        for my_act in my_actions:
            x1 = x[np.int(me_too)]
            y1 = y[np.int(me_too)]
            x2 = x[np.int(my_act)]
            y2 = y[np.int(my_act)]
            if(my_act !=me_too):
                plt.arrow(x1,y1,x2-x1,y2-y1,
                    fc="black", ec='black', alpha=.015, width=.1,
                    head_width=1.0, head_length=1)


def plot_arrows_path(x, y, optimal_traj):
    x_pos = []
    y_pos = []
    for wlt in optimal_traj:
        x_pos.append(x[np.int(wlt)])
        y_pos.append(y[np.int(wlt)])
    for i in range(0, len(x_pos)-1):
        x_dif = x_pos[i+1] - x_pos[i]
        y_dif = y_pos[i + 1] - y_pos[i]
        plt.arrow(x_pos[i], y_pos[i], x_dif, y_dif,
              fc="green", ec='green', alpha=.065, width=.4,
              head_width=1.4, head_length=1)
def scatter_value_function(x, y, value_function, dict_mdp, R):
    S=dict_mdp['S']
    N=len(x)
    colors = value_function
    area = 80 * np.ones((N,1))
    plt.scatter(x, y, s=area, c=colors, alpha=0.5)

    for idx, txt in enumerate(S):
        if(txt in R):
            new_txt = txt + "/" + str(float("{:.1f}".format(dict_mdp['U'][idx])))+"/\n"+str(R[txt])
            plt.annotate(new_txt, (x[idx], y[idx]), color='red')
        else:
            new_txt = txt + "/" + str(float("{:.1f}".format(dict_mdp['U'][idx])))
            plt.annotate(new_txt, (x[idx], y[idx]))
def plt_show():
    plt.xlabel('x')
    plt.ylabel('y')
    plt.show()

def get_xyz(P):
    x = np.array([P[i][0] for i in P])
    y = np.array([P[i][1] for i in P])
    z = np.array([P[i][2] for i in P])
    return x,y,z