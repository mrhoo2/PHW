import sys
# could use just argv instead of sys.argv if line 1 read: from sys import argv
script, input_encoding, error = sys.argv
# input encodings can be things like utf-8,-16,-32 or big5, etc.
# Python 3 defaults to unicode everywhere


def main(language_file, encoding, errors):
    line = language_file.readline()

    # if statement fails when line returns empty string
    if line:
        print_line(line, encoding, errors)
        # creates a while loop by calling main from inside main
        return main(language_file, encoding, errors)


def print_line(line, encoding, errors):
    # .strip([char]) strips leading/trailing characters from a string.
    # .strip defaults to whitespace when [char] is omitted; includes \n, \t
    next_lang = line.strip()
    # encode strings
    raw_bytes = next_lang.encode(encoding, errors=errors)
    
    # decode bytes
    cooked_string = raw_bytes.decode(encoding, errors=errors)

    print(raw_bytes, "<====>", cooked_string)


languages = open("languages.txt", encoding="utf-8")

main(languages, input_encoding, error)
