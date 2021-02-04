import reachab
import numpy as np
import md_pro as md
from movepredict.src.programs.helpfunctions import *


def only_mdp(params):
    strt_pnt = '16'
    P = md.get_meshgrid_points(params)
    x,y,z=get_xyz(P)
    # Topology
    T, S = md.get_simple_topology_for_regular_grid(params, P)
    # rewards
    R = {'23': 100}
    mdp_challenge = {'S': S, 'R': R, 'T': T, 'P': P}
    dict_mdp = md.start_mdp(params, mdp_challenge)
    reach_set = md.reach_n_steps(strt_pnt, mdp_challenge, dict_mdp, params, steps=10)
    optimal_traj = md.get_deterministic_trajectory(strt_pnt, dict_mdp, steps=20)
    print_info(dict_mdp, optimal_traj)
    plot_topology(x, y, dict_mdp)
    plot_arrows_path(x, y, optimal_traj)
    scatter_value_function(x, y, np.array(dict_mdp['U']), dict_mdp, R)
    plt_show()

