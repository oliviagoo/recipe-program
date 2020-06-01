#recipe alteration program
#olivia goodman 1/6/20
#version 1 - this version will focus on creating the scale factor

print("Pancake recipe courtesy of Chelsea Sugar (https://www.chelsea.co.nz/browse-recipes/sunday-pancake-recipe/)")
ingredients = ["flour", "white sugar", "grated lemon zest", "milk", "egg", "butter"]
units = ["cup", "tablespon", "teaspoon", "cup", "n/a", "grams"]
amounts = [1, 2, 0.5, 1, 1, 30]
old_servings = 3

print("The current recipe serves {} people.".format(old_servings))
new_servings = int(input("How many people should the recipe serve? "))

scale_factor = new_servings / old_servings
print(scale_factor)
