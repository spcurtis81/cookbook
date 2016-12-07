#!/usr/bin/python3
# Script for Python3.* by Stephen Curtis - 7 Dec 2016



def main():
    f = open('simple_text.txt', 'r') # Opens file in read mode and assigns content to f
    for line in f.readlines():
        print(line, end='')



if __name__ == "__main__": main()
