print("How old are you?", end=' ')
age = int(input())

# Can use repr() to represent a variable -- strings will have '' appended
print("How tall are you?", end=' ')
height = input()
print("How much do you weigh?", end=' ')
weight = input()

print(f"So, you're {age} old, {height} tall, and {weight} heavy.")
