name = 'Mackenzie Hoover'
age = 26 # not a lie
height = 66 # inches
height_cm = round(height * 2.54)
weight = 150 # lbs
weight_kg = round(weight / 2.2)
eyes = 'Brown'
teeth = 'White'
hair = 'Brown'

print(f"Let's talk about {name}.")
print(f"He's {height_cm} cm tall.")
print(f"He's {weight_kg} kg heavy.")
print("Actually that's not too heavy.")
print(f"He's got {eyes} eyes and {hair} hair.")
print(f"His teeth are usually {teeth} depending on the coffee.")

# this line is tricky, try to get it exactly right
total = age + height_cm + weight_kg
print(f"If I add {age}, {height_cm}, and {weight_kg} I get {total}.")