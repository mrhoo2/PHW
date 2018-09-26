# This is the first script that uses cli arguments

# Import functions argv and version_info from sys
from sys import argv, version_info
# read the wyss section for how to run this
# script, first, second, third = argv

print(">>>> your python version is:", repr(version_info))

# print arrays with brackets.
print("The script is called:", argv[0])
print("Your first variable is:", argv[1])
print("Your second variable is:", argv[2])
print("Your third variable is:", argv[3])
