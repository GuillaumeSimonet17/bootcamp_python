from recipe import Recipe
import time

class Book:

    def __init__(self, name, last_update, creation_date, recipes_list):
        self.name = name 
        self.last_update = last_update
        self.creation_date = creation_date
        self.recipes_list = {
            "starter": [],
            "lunch": [],
            "dessert": []
        }

    def get_recipe_by_name(self, name):
        for keys, values in self.recipes_list.items():
            for recipe in values:
                if recipe.name == name:
                        print(recipe)
                        return recipe
        print(f"No recipes match with '{name}'")

    def get_recipes_by_types(self, recipe_type):
        recipes = (self.recipes_list.get(recipe_type, []))
        if recipes:
            recipes_names = [recipe.name for recipe in recipes]
            return recipes_names
        

    def add_recipe(self, recipe):
        if not isinstance(recipe, Recipe):
            return print("Ce qui est passe en param n'est pas un objet de type Recipe")
        """Add a recipe to the book and update last_update"""
        self.recipes_list[recipe.recipe_type].append(recipe)
        self.last_update = time.time()
