# Identify types of people and punchline. Use f preceding a string to enable
# variable substitution.
types_of_people = 10
# This is an f-string with types_of_people inserted.
x = f"There are {types_of_people} types of people."

# Assign "binary" to binary (string)
binary = "binary"
# Assign "don't" to do_not (string)
do_not = "don't"
# Assign f-string to y, insert (binary) and (do_not)
y = f"Those who know {binary} and those who {do_not}."

print(x)
print(y)

print(f"I said: {x}")
print(f"I also said: {y}")

hilarious = False
joke_evaluation = "Isn't that joke so funny?! {}"

# Print .format string (can't use f-string for this)
print(joke_evaluation.format(types_of_people))

w = "This is the left side of"
e = "a string with a right side."

print(w + "..." + e)
