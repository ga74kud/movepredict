# -------------------------------------------------------------
# code developed by Michael Hartmann during his Ph.D.
# Movement Prediction
#
# (C) 2020 Michael Hartmann, Graz, Austria
# Released under GNU GENERAL PUBLIC LICENSE
# email michael.hartmann@v2c2.at
# -------------------------------------------------------------
from src.programs.only_reachability import *
from src.programs.reachability_mdp import *

import argparse
import definitions
import datareader
import os
from src.main_loop import *

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--box_function', '-box', type=str, help='choices: without_box, with_box',
                        default='without_box', required=False)
    parser.add_argument('--visualization', '-vis', type=str, help='y, n',
                        default='y', required=False)
    parser.add_argument('--time_horizon', '-T', type=float, help='value like: T=2.2', default=2.2, required=False)
    parser.add_argument('--steps', '-N', type=int, help='value like N=4', default=6, required=False)
    parser.add_argument('--debug', '-deb', type=str, help='(y,n)', default='n', required=False)
    parser.add_argument('--window_x', '-wix', type=int, help='windowsize in x-direction for savgol_filter', default=101, required=False)
    parser.add_argument('--window_y', '-wiy', type=int, help='windowsize in y-direction for savgol_filter', default=101, required=False)
    parser.add_argument('--poly_x', '-pox', type=int, help='polygon order in x-direction for savgol_filter', default=2, required=False)
    parser.add_argument('--poly_y', '-poy', type=int, help='polygon order in y-direction for savgol_filter', default=2, required=False)
    parser.add_argument('--program', '-pro', type=str, help='a) only_reachability', default='only_reachability', required=False)
    parser.add_argument('--face_color', '-facol', type=str, help='name: orange, green or values', default='cyan',
                        required=False)
    parser.add_argument('--gamma', '-gam', type=float, help='gamma=0.9',
                        default='0.9', required=False)
    parser.add_argument('--x_grid', '-xgr', type=int, help='x_grid=5',
                        default='8', required=False)
    parser.add_argument('--y_grid', '-ygr', type=int, help='y_grid=5',
                        default='5', required=False)

    args = parser.parse_args()
    params = vars(args)
    params['PROJECT_ROOT']=definitions.get_project_root()
    if (params['debug'] == 'y'):
        logging.basicConfig(format='%(levelname)s:%(message)s', level=logging.DEBUG)

    only_mdp(params)

if __name__ == '__main__':
    main()
