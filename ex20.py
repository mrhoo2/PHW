from sys import argv

script, input_file = argv


def print_all(f):
    print(">>> print_all: ", f)
    print(f.read())
    print("<<< print_all: ", f)


def rewind(f):
    f.seek(0)


def print_a_line(line_count, f):
    print(line_count, f.readline(), end="")

current_file = open(input_file)
current_line = 0

print("First let's print the whole file:\n")

print_all(current_file)

print("Now let's rewind, kind of like a tape.")

rewind(current_file)

# lines = int(input("How many lines should we print?\n"))

# Trying to get the while loop to terminate when the end of the file has been
# reached, if the user enters a larger number of lines than exist.
#
# while current_line < lines:
#     print_a_line(current_line, current_file)
#     current_line += 1
#     print("<<< ", current_file.readline())
#     if current_file.readline() == '':
#         break


print("Let's print three lines:")

for i in range(3):
    current_line = i
    print_a_line(current_line, current_file)

# for current_line in current_file:
#     print(current_line, end="")
#     current_line += 1

# print("\nThat's the end of the file.")
# rewind(current_file)
