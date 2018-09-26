# create a format string with four blank arguments
formatter = "{} {} {} {}"

# pass 1, 2, 3, 4 as arguments to the formatter string, then print it.
print(formatter.format(1, 2, 3, 4))
# pass strings into the formatter
print(formatter.format("one", "two", "three", "four"))
# pass booleans into the formatter & print
print(formatter.format(True, False, False, True))
# recursive
print(formatter.format(formatter, formatter, formatter, formatter))
print(formatter.format(
    """    Try your
    Own text here
    Maybe a poem
    Or a song about fear""", "", "", ""
))

# Make sure arguments are passed for all 4 {} in the formatter variable
# or you can get the tuple index error out of range.
