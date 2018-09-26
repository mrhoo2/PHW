# define new function called cheese and crackers, assign parameters
def cheese_and_crackers(cheese_count, boxes_of_crackers):
    # print something with cheese_count
    print(f"You have {cheese_count} cheeses!")
    # print something with boxes_of_crackers
    print(f"You have {boxes_of_crackers} boxes of crackers!")
    # print more garbage
    print("Man that's enough for a party!")
    print("Get a blanket.\n")

print("We can just give the function numbers directly:")
cheese_and_crackers(20, 30)

print("OR, we can use vairables from our script:")
amount_of_cheese = 10
amount_of_crackers = 50

print("We can even do math inside too:")
cheese_and_crackers(10 + 20, 5 + 6)

print("And we can combine the two, variables and math:")
cheese_and_crackers(amount_of_cheese + 100, amount_of_crackers + 1000)
