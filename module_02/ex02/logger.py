import time
from random import randint
import os

def log(func):
    def wrapper(*args, **kwargs):
        # ------------ print('0')
        start = time.perf_counter()
        res = func(*args, **kwargs)
        exec_time = time.perf_counter() - start
        # ------------ print('3')

        with open('machine.log', mode="a", encoding="utf-8") as file:
            user = os.getenv('USER')
            name = func.__name__.replace('-', ' ').title()
            file.write(f'({user})Running: {name:19}[ exec-time = {exec_time:.3f}ms ]\n')
        return res
            
    return wrapper

class CoffeeMachine():
    water_level = 100

    @log
    def start_machine(self):
        if self.water_level > 20:
            return True
        else:
            print("Please add water!")
            return False

    @log
    def boil_water(self):
        return "boiling..."

    @log
    def make_coffee(self):
        # ------------ print('1')
        if self.start_machine():
            for _ in range(20):
                time.sleep(0.1)
                self.water_level -= 1
            print(self.boil_water())
            print("Coffee is ready!")
        # ------------ print('2')
        

    @log
    def add_water(self, water_level):
        time.sleep(randint(1, 5))
        self.water_level += water_level
        print("Blub blub blub...")

if __name__ == "__main__":
    machine = CoffeeMachine()
    for i in range(0, 55):
        machine.make_coffee()
    machine.make_coffee()
    machine.add_water(70)
    