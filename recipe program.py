#recipe alteration program
#olivia goodman 3/6/20
#version 3 - this version will replace the hard-coded ingredients and units

def input_menu():
    while True:
        mode = input("Press I to input an ingredient, U for a unit, or Q to quit: ").lower().strip()
        if mode == "i":
            ingredients.append(input("Please enter the ingredient: "))
        elif mode == "u":
            units.append(input("Please enter the unit: "))
        else:
            break

#main routine

#hard coded recipe
print("Pancake recipe courtesy of Chelsea Sugar (https://www.chelsea.co.nz/browse-recipes/sunday-pancake-recipe/)")
ingredients = []
units = []
amounts = [1, 2, 0.5, 1, 1, 30]
new_amounts = []
old_servings = 3

input_menu()

#input - servings amount
print("The current recipe serves {} people.".format(old_servings))
new_servings = int(input("How many people should the recipe serve? "))

#calculating scale factor
scale_factor = new_servings / old_servings
print(scale_factor)

#altering the amounts in the recipe
for value in amounts:
    new_amounts.append(value * scale_factor)

#outputting new recipe
for i in range(len(ingredients)):
    print("{:.2f} {}s of {}".format(new_amounts[i], units[i], ingredients[i]))

