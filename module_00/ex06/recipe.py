cookbook = {
    "Sandwich": {
        "ingredients": ["ham", "bread", "cheese", "tomatoes"],
        "meal": "lunch",
        "prep_time": 10,
    },
    "Cake": {
        "ingredients": ["flour", "sugar", "eggs"],
        "meal": "dessert",
        "prep_time": 60,
    },
    "Salad": {
        "ingredients": ["avocado", "arugula", "tomatoes", "spinach"],
        "meal": "lunch",
        "prep_time": 15,
    }
}

def print_recipes_names():
    if not cookbook:
        return print('the cookbook is empty')
    for n in cookbook:
        print(n)
        print_recipe(n)
        print('\n')

def print_recipe(recipe_name=""):
    if recipe_name == "":
        recipe_name = input(">> What the name of the recipe you search?\n")
    try:
        print(f"Ingredients list: ", cookbook[recipe_name]["ingredients"])
        print(f"To be eaten for {cookbook[recipe_name]['meal']}.")
        print(f"Takes {cookbook[recipe_name]['prep_time']} minutes of cooking.")
    except:
        print("!!! This recipe does not exist in the cookbook !!!\n")

def delete_recipe(recipe_name=""):
    if recipe_name == "":
        recipe_name = input(">> What the name of the recipe you want to delete?\n")
    try:
        del cookbook[recipe_name]
        print(f'{recipe_name}\'s recipe removed')
    except:
        print("!!! This recipe does not exist in the cookbook !!!\n")

def add_recipe():
    name = input(">>> Enter a name:\n")
    ingredient = input(">>> Enter ingredients:\n")
    list_ingredients = []
    list_ingredients.append(ingredient)
    while ingredient != '':
        ingredient = input()
        if ingredient == '':
            break
        list_ingredients.append(ingredient)
    meal_type = input(">>> Enter a meal type:\n")
    prep_time = input(">>> Enter a preparation time:\n")

    new_recipe = {'ingredients': list_ingredients, 'meal': meal_type, 'prep_time': prep_time}
    cookbook[name] = new_recipe

def help_cmd():
    print("List of available option:\n")
    print("1: Add a recipe\n2: Delete a recipe\n3: Print a recipe\n4: Print the cookbook\n5: Quit\n6: Help")

def get_command(option):
    switch_dic = {
        1: add_recipe,
        2: delete_recipe,
        3: print_recipe,
        4: print_recipes_names,
        6: help_cmd
    }
    return switch_dic.get(option)()

def main():
    print("Welcome to the Python Cookbook !\n")
    help_cmd()
    while 1:
        option = 0

        while option < 1 or option > 6:
            print("\nPlease select an option:")
            try:
                option = int(input(">> "))
                if option < 1 or option > 6:
                    print("\nSorry, this option does not exist.")
                    help_cmd()
            except:
                print("\nSorry, this option does not exist.")
                help_cmd()


        if option == 5:
            print("\nCookbook closed. Goodbye !")
            return
        get_command(option)

    # print_recipes_names()

    # print_recipe('Cake')

    # delete_recipe('Cake')
    # print_recipes_names()

    # add_recipe()
    # print_recipes_names()
    # print_recipe('new')



    



if __name__ == "__main__":
    main()