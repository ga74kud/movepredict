import numpy as np
import matplotlib.pyplot as plt
import md_pro as md

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
              fc="red", ec='red', alpha=.165, width=.4,
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
'''
    Plot the trajectories of two agents
'''
def plot_trajectories_two_agents(traj_A, traj_B):
    for i in range(0, len(traj_A)-1):
        pos_A=traj_A[i]
        nxt_pos_A = traj_A[i+1]
        pos_B = traj_B[i]
        nxt_pos_B = traj_B[i + 1]
        plt.arrow(pos_A[0], pos_A[1], nxt_pos_A[0]-pos_A[0], nxt_pos_A[1]-pos_A[1],
              fc="red", ec='red', alpha=.165, width=.4,
              head_width=1.4, head_length=1)
        plt.arrow(pos_B[0], pos_B[1], nxt_pos_B[0] - pos_B[0], nxt_pos_B[1] - pos_B[1],
                  fc="green", ec='red', alpha=.165, width=.4,
                  head_width=1.4, head_length=1)

'''
    Compute xva with force 
'''
def comp_xva(F, params):
    erg=[]
    xva=[0, 0]
    erg.append(xva)
    for i in range(0, len(F)):
        xva=next_xva(xva, F[i], params)
        erg.append(xva)
    return erg

def next_xva(xva, F, params):
    Ts = params['Ts']
    x = xva[0]
    v = xva[1]
    x = Ts * v + x
    v = Ts * F + v
    return [x, v]