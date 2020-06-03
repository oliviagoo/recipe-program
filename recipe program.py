#recipe alteration program
#olivia goodman 3/6/20
#version 2 - this version will alter the recipe's amounts based on the scale factor

#hard coded recipe
print("Pancake recipe courtesy of Chelsea Sugar (https://www.chelsea.co.nz/browse-recipes/sunday-pancake-recipe/)")
ingredients = ["flour", "white sugar", "grated lemon zest", "milk", "egg", "butter"]
units = ["cup", "tablespon", "teaspoon", "cup", "n/a", "gram"]
amounts = [1, 2, 0.5, 1, 1, 30]
new_amounts = []
old_servings = 3


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
