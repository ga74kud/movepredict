# -------------------------------------------------------------
# code developed by Michael Hartmann during his Ph.D.
# Movement Prediction
#
# (C) 2020-2021 Michael Hartmann, Graz, Austria
# Released under GNU GENERAL PUBLIC LICENSE
# email michael.hartmann@v2c2.at
# -------------------------------------------------------------

import md_pro as md
from movepredict.src.programs.helpfunctions import *
'''
    agents without interaction coming together in the same environment and different velocities
'''
def two_agents_without_interaction_common_playground_different_velocities(params):
    params['Ts'] = params['time_horizon'] / (params['steps'] + 1)
    F_A = [8, 8, 8, 0, 0, 0, 0, -4, 0, 0, 0, 0, 0, 0, 0, 0 ]
    F_B = [4, 4, 4, 0, 0, 0, 8, 0, 0, 0, 0, 0, 0, 0, 0, 0 ]
    F_A = [8, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    F_B = [8, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    states_A = comp_xva(F_A, params)
    states_B = comp_xva(F_B, params)
    plot_xva(states_A, states_B)
    path_A, path_B=two_agents_without_interaction_common_playground_123(params)
    cum_dist_A = md.cumulative_distance_without_filtering(path_A)
    cum_dist_B = md.cumulative_distance_without_filtering(path_B)
    plot_two_movements(path_A, cum_dist_A, states_A, path_B, cum_dist_B, states_B)
    None

'''
    plot xva
'''
def plot_xva(states_A, states_B):
    fig, (ax1, ax2)  = plt.subplots(2,1)
    x_A, v_A = get_xv(states_A)
    x_B, v_B = get_xv(states_B)

    ax1.plot(x_A, label='Position A')
    ax1.plot(x_B, label='Position B')
    ax1.grid()
    ax2.plot(v_A, label='Velocity A')
    ax2.plot(v_B, label='Velocity B')
    ax2.grid()
    ax1.set_ylabel('Positions [m]')
    ax2.set_xlabel('Time [s]')
    ax2.set_ylabel('Velocity [m/s]')
    ax1.legend()
    ax2.legend()
    plt.show()
'''
    agents without interaction coming together in the same environment
'''
def two_agents_without_interaction_common_playground_123(params):
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
    return path_A, path_B
def plot_later(path_A, path_B):
    plot_trajectories_two_agents(path_A, path_B)
    #scatter_value_function(x, y, np.array(dict_mdp_A['U']), dict_mdp_A, R_A)
    plt.axis([-12, 12, -12, 12])
    plt.grid()
    plt_show()