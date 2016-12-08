#!/usr/bin/python3
# Script for Python3.* by Stephen Curtis - 7 Dec 2016



def main():
    buffersize = 50000  # Creates a variable defining the buffer size in bytes.
    infile = open('bigfile.txt', 'r')  # Opens file in read mode.
    outfile = open('new.txt', 'w')  # Creates a variable for the output file with write permission.
    buffer = infile.read(buffersize)  # Creates a buffer variable and fills it with 50000 (buffersize) bytes of data.
    while len(buffer):  # While the buffer has content.
        outfile.write(buffer)  # Write the content of the buffer to the outfile.
        print('.', end='')  # Print the '.' to screen for each iteration of the loop.
        buffer = infile.read(buffersize)  # Reads the file to obtain the next buffer.

    print()
    print('Done')


if __name__ == "__main__": main()