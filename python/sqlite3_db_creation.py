#!/usr/bin/python3
# Script for Python3.* by Stephen Curtis - 8 Dec 2016

import sqlite3

def main():
    db = sqlite3.connect('test.db')     # Creates/connects to test.db and assigns to variable db
    db.execute('drop table if exists test')     # Executes sql code in '' - drops the test table if it already exists.
    db.execute('create table test (t1 text, i1 int)')   # Creates a new test table with two fields
    db.execute('insert into test (t1 , i1) values (?, ?)', ('one', '1'))    # Inserts values to table - note: (?, ?) are placeholders for parameters passed later in the line.
    db.execute('insert into test (t1 , i1) values (?, ?)', ('two', '2'))
    db.execute('insert into test (t1 , i1) values (?, ?)', ('three', '3'))
    db.execute('insert into test (t1 , i1) values (?, ?)', ('four', '4'))
    db.execute('insert into test (t1 , i1) values (?, ?)', ('five', '5'))
    db.commit()     # Above code is only buffered - must commit to add it to the table.
    cursor = db.execute('select i1, t1 from test order by i1')  # Runs the select query and passes result to cursor variable as a tuple.

    for row in cursor:
        print(row)

if __name__ == "__main__": main()
