#!/usr/bin/python3
# Simulates using Python's built in range function by creating a generator class which includes the the stop point (as opposed to ignoring in in the way range does).
# Example taken from Lynda.com - Python 3 Essential Training


class inclusive_range:
    def __init__(self, *args):
        numargs = len(args)
        if numargs <1: raise TypeError('Requires at least one argument')
        elif numargs == 1:
            self.stop = args[0]
            self.start = 0
            self.step = 1
        elif numargs == 2:
            (self.start, self.stop) = args
            self.stop = 1
        elif numargs == 3:
            (self.start, self.stop, self.step) = args
        else: raise TypeError('Cannot accept more than three arguments - {} passed'.format(numargs))

    def __iter__(self):
        i = self.start
        while i <= self.stop:
            yield i
            i += self.step


def main():
    o = inclusive_range(25)
    for i in o: print(i, end = ' ')

if __name__ == "__main__": main()
