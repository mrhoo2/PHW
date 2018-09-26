# Here's some new strange stuff, remember type it exactly.

days = "Mon Tue Wed Thu Fri Sat Sun"
# \n is an escape character, which doesn't break the string. use \" similarly.
months = "\nJan\nFeb\nMar\nApr\nMay\nJun\nJul\nAug"

print("Here are the days: ", days)
print("Here are the months: ", months)

# triple quotes are a special type of escape character.
# formatting is weird with them.
print("""
There's something going on here.
With the three double-quotes.
We'll be able tot ype as much as we like.
Even 4 lines if we want, or 5, or 6.
""")
