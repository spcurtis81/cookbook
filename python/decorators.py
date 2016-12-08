#!/usr/bin/python3


class car:
    def __init__(self, **kwargs):
        self.properties = kwargs

    def noise(self):
        print('Vroom!')

    def get_properties(self):
        return self.properties

    def get_property(self, key):
        return self.properties.get(key, None)

    @property # Creates a color property which can be passed to the class as arguments when creating an object.
    def color(self):
        return self.properties.get('color', None)

    @color.setter
    def color(self, c):
        self.properties['color'] = c

    @color.deleter
    def color(self):
        del self.properties['color']

    @property # Creates a speed property which can be passed to the class as arguments when creating an object.
    def speed(self):
        return self.properties.get('speed', None)

    @speed.setter
    def speed(self, s):
        self.properties['speed'] = s

    @speed.deleter
    def speed(self):
        del self.properties['speed']


def main():
    Porsche = car()
    Porsche.color = 'Blue'
    Porsche.speed = '156 mph'
    print(Porsche.color)
    print(Porsche.speed)

if __name__ == "__main__": main()
