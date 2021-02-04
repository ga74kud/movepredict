

import md_pro as md
from movepredict.src.programs.helpfunctions import *
'''
    agents without interaction coming together in the same environment
'''
def two_agents_without_interaction_common_playground(params):
    strt_pnt_A = '16'
    strt_pnt_B = '23'
    end_pnt_A ='23'
    end_pnt_B = '16'
    P = md.get_meshgrid_points(params)
    x, y, z = get_xyz(P)
    # Topology
    T, S = md.get_simple_topology_for_regular_grid(params, P)
    # rewards
    R_A = {end_pnt_A: 100}
    R_B = {end_pnt_B: 100}
    mdp_challenge_A = {'S': S, 'R': R_A, 'T': T, 'P': P}
    mdp_challenge_B = {'S': S, 'R': R_B, 'T': T, 'P': P}

    dict_mdp_A = md.start_mdp(params, mdp_challenge_A)
    dict_mdp_B = md.start_mdp(params, mdp_challenge_B)


    optimal_traj_A = md.get_deterministic_trajectory(strt_pnt_A, dict_mdp_A, steps=20)
    optimal_traj_B = md.get_deterministic_trajectory(strt_pnt_B, dict_mdp_B, steps=20)

    interpolated_points_A, points_A = md.get_result_trajectories_mdp(params, optimal_traj_A, P)
    interpolated_points_B, points_B = md.get_result_trajectories_mdp(params, optimal_traj_B, P)
    path_A = interpolated_points_A['quadratic']
    path_B = interpolated_points_B['quadratic']
    plot_trajectories_two_agents(path_A, path_B)
    #scatter_value_function(x, y, np.array(dict_mdp_A['U']), dict_mdp_A, R_A)
    plt.axis([-12, 12, -12, 12])
    plt.grid()
    plt_show()
    #print_info(dict_mdp_A, optimal_traj_A)
    # plot_topology(x, y, dict_mdp)
    # plot_arrows_path(x, y, optimal_traj)
    # scatter_value_function(x, y, np.array(dict_mdp['U']), dict_mdp, R)
    # plt_show()