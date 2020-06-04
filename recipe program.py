#recipe alteration program
#olivia goodman 3/6/20
#version 7 - this version will focus on exceptional error handling

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

#print("Pancake recipe courtesy of Chelsea Sugar (https://www.chelsea.co.nz/browse-recipes/sunday-pancake-recipe/)")
#setting up the necessary empty lists
ingredients = []
units = []
amounts = []
new_amounts = []
old_servings = recipe_input()

#input - how many people the recipe should serve
while True:
    new_servings = force_int("How many people should the recipe serve? ")
    #calculating scale factor
    scale_factor = new_servings / old_servings
    #print(scale_factor)
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
print("This recipe now serves {} people.".format(new_servings))
for i in range(len(ingredients)):
    print("{:.2f} {}s of {}".format(new_amounts[i], units[i], ingredients[i]))

