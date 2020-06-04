#recipe alteration program
#olivia goodman 4/6/20
#version 8 - this version will focus on clean-up, for usability and ease of reading the code

#this function gets the user input for the original recipe
def recipe_input():
    while True:
        new_ingredient = input("Enter an ingredient, or press Q to quit: ").lower().strip()
        if new_ingredient == "q":
            break
        else:
            ingredients.append(new_ingredient)
            units.append(input("Enter the unit for the ingredient: "))
            amounts.append(force_num("How much of that unit is needed? "))
    old_servings = force_int("How many people does the recipe serve currently? ")
    return old_servings

#this funtion will force the user to enter an integer
def force_int(msg):
    while True:
        try:
            value = int(input(msg))
            break
        except ValueError:
            print("Please enter a valid whole number!")
    return value

#this funtion will force the user to enter a float OR int
def force_num(msg):
    while True:
        try:
            value = float(input(msg))
            break
        except ValueError:
            print("Please enter a valid number!")
    return value

#main routine
#setting up the necessary empty lists
ingredients = []
units = []
amounts = []
new_amounts = []

#welcome message, with basic instructions for the user
print("Welcome to the recipe modification program!")
print("""This program will take a recipe which serves a certain amount of people, and modify it to serve a new number.
The program will guide you through the process of entering the recipe, the serving amounts, and output a new recipe for you.
All input should be singular (e.g. egg, cup, gram). If a unit is not relevant, write n/a.
""")

#input - the recipe and how many people it should serve
old_servings = recipe_input()
while True:
    new_servings = force_int("How many people should the recipe serve? ")
    #calculating scale factor
    scale_factor = new_servings / old_servings
    if scale_factor > 3:
        print("The ingredients won't fit in the bowl! Please make a smaller batch.")
    elif scale_factor < 0.25:
        print("Your recipe is too small! Make a larger batch and freeze the leftovers.")
    else:
        break

#altering the amounts in the recipe
for value in amounts:
    new_amounts.append(value * scale_factor)

#outputting new recipe
print()
print("This recipe now serves {} people.".format(new_servings))
for i in range(len(ingredients)):
    if units[i] != "n/a":
        print("{:.2f} {}s of {}".format(new_amounts[i], units[i], ingredients[i]))
    else:
        print("{:.2f} {}s".format(new_amounts[i], ingredients[i]))
