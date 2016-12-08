#!/usr/bin/python3
# This is snippet shows the basic syntax for creating a class.


class car:
    def wheels (self): print("The car has 4 wheels")
    def colour (self): print("This is a red car")
    def sport (self): print("This is a sporty car")



def main():
    Ferarri = car()
    Ferarri.wheels()
    Ferarri.colour()
    Ferarri.sport()

if __name__ == "__main__": main()