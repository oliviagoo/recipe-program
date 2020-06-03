#recipe alteration program
#olivia goodman 3/6/20
#version 4 - this version will replace the hard-coded ingredients and units, with a better input method

def recipe_input():
    while True:
        new_ingredient = input("Enter an ingredient, or press Q to quit: ").lower().strip()
        if new_ingredient == "q":
            break
        else:
            ingredients.append(new_ingredient)
            units.append(input("Enter the unit for the ingredient: "))

#main routine

#hard coded recipe
print("Pancake recipe courtesy of Chelsea Sugar (https://www.chelsea.co.nz/browse-recipes/sunday-pancake-recipe/)")
ingredients = []
units = []
amounts = [1, 2, 0.5, 1, 1, 30]
new_amounts = []
old_servings = 3

recipe_input()

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

