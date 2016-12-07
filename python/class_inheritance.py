#!/usr/bin/python3
# This is snippet shows the basic syntax for creating a class.

# Main class of car
class car:
    def wheels (self): print("The car has 4 wheels")
    def colour (self): print("This is a red car")

# A child class of car which is called sports_car.
class sports_car(car): # Placing another class in parenthesis allows this class to inherit from anther.
    def sport(self): print("This is a sporty car")
    def speed(self): print("I go very fast")

class standard_car(car):
    def sport(self): print("I am a basic looking car but very efficient all the same")
    def speed(self): print("I am fast but not as fast as a sports car")


def main():
    Ferarri = sports_car() # Var Ferarri is created using the sports_car class
    Ferarri.wheels()
    Ferarri.colour()
    Ferarri.sport()
    Ferarri.speed()

    print("----- New Car -----")

    Polo = standard_car() # Var Polo is created using the standard_car class
    Polo.wheels()
    Polo.colour()
    Polo.sport()
    Polo.speed()

if __name__ == "__main__": main()