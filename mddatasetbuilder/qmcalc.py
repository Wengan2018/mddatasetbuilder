'''QM calculation with Gaussian'''

import os
import argparse
from gaussianrunner import GaussianRunner


def qmcalc(dir, command='g16'):
    gjflist = [filename for filename in os.listdir(dir)]
    GaussianRunner(command=command).runGaussianInParallel('GJF', gjflist)


def _commandline():
    parser = argparse.ArgumentParser(description='MDDatasetBuilder')
    parser.add_argument('-d', '--dir',
                        help='Dataset dirs', required=True)
    parser.add_argument('-c', '--command',
                        help='Gaussian command, default is g16')
    args = parser.parse_args()
    qmcalc(dir=args.dir, command=args.command)
