#!/usr/bin/python3
# Script for Python3.* by Stephen Curtis - 8 Dec 2016


def main():
    buffersize = 50000
    infile = open('cat.jpg', 'rb')
    outfile = open('newCat.jpg', 'wb')
    buffer = infile.read(buffersize)
    while len(buffer):
        outfile.write(buffer)
        print('.', end='')
        buffer = infile.read(buffersize)
    print()
    print('Done')

if __name__ == "__main__": main()
