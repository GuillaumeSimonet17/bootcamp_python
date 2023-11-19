from recipe import Recipe
from book import Book
import time

def main():
    my_book = Book("firstOne", time.time(), time.time(), {"starter", "lunch", "dessert"})
    
    # first_recipe = Recipe("Tiramisu", 2, 25, ["sucre", "et puis d'autres des bails"], 'cher bon sa mere, c\'est italien au cas tu savais pas batard', "dessert")
    # sec_recipe = Recipe("Tiramisu2", 2, 25, ["sucre", "et puis d'autres des bails"], 'cher bon sa mere, c\'est italien au cas tu savais pas batard', "dessert")
    # my_book.add_recipe(first_recipe)
    # my_book.add_recipe(sec_recipe)
    # print("------------------------------")
    # print(first_recipe)
    # print("------------------------------")
    # print(sec_recipe)
    # print("------------------------------")
    # print(my_book.get_recipes_by_types('dessert'))
    # print("------------------------------")
    # print(my_book.get_recipes_by_types('lunch'))
    # print("------------------------------")
    # print(my_book.get_recipes_by_types('coucou'))
    # print("------------------------------")
    # my_book.get_recipe_by_name('Tiramisu')
    # print("------------------------------")
    # my_book.get_recipe_by_name('caramelo')

if __name__ == "__main__":
    main()
