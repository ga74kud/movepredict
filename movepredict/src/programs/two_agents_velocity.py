

import md_pro as md
from movepredict.src.programs.helpfunctions import *
'''
    agents without interaction coming together in the same environment and different velocities
'''
def two_agents_without_interaction_common_playground_different_velocities(params):
    params['Ts'] = params['time_horizon'] / (params['steps'] + 1)
    F_A = [8, 8, 0, 0, 0]
    F_B = [4, 4, 0, 0, 0]
    states_A = comp_xva(F_A, params)
    states_B = comp_xva(F_B, params)
    plot_xva(states_A, states_B)

'''
    plot xva
'''
def plot_xva(states_A, states_B):
    fig, (ax1, ax2)  = plt.subplots(2,1)
    x_A=[i[0] for i in states_A]
    v_A = [i[1] for i in states_A]
    x_B = [i[0] for i in states_B]
    v_B = [i[1] for i in states_B]

    ax1.plot(x_A)
    ax1.plot(x_B)
    #ax1.title('Positions')
    #ax1.xlabel('Step')
    #ax1.ylabel('Positions')
    ax1.grid()
    ax2.plot(v_A)
    ax2.plot(v_B)
    #ax2.title('Velocities')
    ax2.grid()
    #ax2.xlabel('Step')
    #ax2.ylabel('Velocities')
    plt.show()
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
    return path_A, path_B
def plot_later(path_A, path_B):
    plot_trajectories_two_agents(path_A, path_B)
    #scatter_value_function(x, y, np.array(dict_mdp_A['U']), dict_mdp_A, R_A)
    plt.axis([-12, 12, -12, 12])
    plt.grid()
    plt_show()