# import argparse module
import argparse

# get an instance of argument parser from argparse module
parser = argparse.ArgumentParser()

# setup firstname, lastname arguements
parser.add_argument('--firstname', help="Enter first name here")
parser.add_argument('--lastname', help="Enter last name here")

# get the dictionary of command line inputs entered by the user
args = parser.parse_args()

# access each command line input from the dictionary
fName = args.firstname
lName = args.lastname

print('Hi, {0} {1}'.format(fName, lName))