from one import MassCalculator
from two import IntMachine
import argparse

parser = argparse.ArgumentParser(description='Advent of code runner.')
parser.add_argument('day', type=int,
                    help='an integer for the day to run')
parser.add_argument('--part', type=str, default='a', help='the part of the days assignment to run (a,b)')

args = parser.parse_args()

challenges = {
    1: lambda: MassCalculator.get_requirements_from_file(),
    2: lambda: IntMachine.run_challenge(args.part)
}

challenges.get(args.day)()
