class Recipe:

    def __init__(self, name, cooking_lvl, cooking_time, ingredients, description, recipe_type): 
        if not ingredients:
            return print("ERROR: Ingredients' list is missing bro! Just wake up, god..")
        for n in ingredients: 
            if not n:
                return print("ERROR: One or several place is empty in your ingredients list. Please, stop using drugs")
        if any(not arg for arg in [name, cooking_lvl, cooking_time, recipe_type]):
            return print('ERROR: An argument is empty')
        try:
            lvl = int(cooking_lvl)
            time = int(cooking_time)
        except:
            return print("ERROR: cooking_lvl or cooking_time is not an integer. Have you ever seen a guy save time by cooking ? Fucking dumbass!")
        if lvl < 1 or lvl > 5:
            return print('ERROR: the cooking_lvl must be contain between 1 and 5')
        if time < 0:
            return print('ERROR: time can not be negative... stupid!')
        if recipe_type not in ["starter", "lunch", "dessert"]:
            return print("Man, you're so stupid...")

        self.name = name
        self.cooking_lvl = cooking_lvl
        self.cooking_time = cooking_time
        self.ingredients = ingredients
        self.description = description
        self.recipe_type = recipe_type
        
    def __str__(self):
        ingriends_str = "\n- ".join([str(ingredient) for ingredient in self.ingredients ]) 
        return f"\n{self.name} ({self.recipe_type}): level {self.cooking_lvl} | {self.cooking_time}mn\n \nDescription: {self.description}\n \nIngredients:\n- {ingriends_str}"

