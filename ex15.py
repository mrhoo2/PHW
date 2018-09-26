from sys import argv

script, filename = argv

txt = open(filename)
# txt.close() -- this causes an I/O error because you can't read a closed file

print(f"Here's your file {filename}:")
print(txt.read())
txt.close()

print("Type the filename again:")
file_again = input('> ')

txt_again = open(file_again)

print(txt_again.read())
txt_again.close()
