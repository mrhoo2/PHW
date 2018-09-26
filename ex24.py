print("Let's practice everything.")
print('You\'d need to know \'bout escapes with \\ that do:')
print('\n newlines and \t tabs.')

poem = """
\t The lovely world
with logic so firmly planted
cannot discern \n the needs of love
nor comprehend passion from intuition
and requires an explanation
\n\t\twhere there is none.
"""

print("---------------")
print(poem)
print("---------------")


five = 10 - 2 + 3 - 6
print(f"This should be five: {five}")


def secret_formula(started):
    jelly_beans = started * 500
    jars = jelly_beans / 1000
    crates = jars / 100
    return jelly_beans, jars, crates


start_point = 10000
beans, jars, crates = secret_formula(start_point)

# remember that this is another way to format a string
print("With a starting point of: {}".format(start_point))
# it's just like with an f"" string
print(f"We'd have {beans} beans, {int(jars)} jars, and {crates} crates.")

start_point = start_point / 10

print("We can also do that this way:")
formula = secret_formula(start_point)
# this is an easy way to apply a list to a format string
print("We'd have {} beans, {} jars, and {} crates.".format(*formula))
# You can manually specify the order by declaring it inside the braces.
print("We'd have {2} beans, {1} jars, and {0} crates.".format(*formula))
# But you can't mix manual and auto-specify, like this.
# print("We'd have {2} beans, {1} jars, and {} crates.".format(*formula)

# print statements can use the % symbol to format strings,
# but this is an old way of doing things and is not recommended anymore.
format = 'format'
print("\nString %sting is used with the %% symbol." % (format))
