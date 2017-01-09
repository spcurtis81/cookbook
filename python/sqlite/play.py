#!/usr/bin/python3
# Script for Python3.* by Stephen Curtis - 9 Jan 2017
# This script demonstrates opening a basic sqlite database and the using that connection to run a query and return results

import sqlite3

db_filename = 'play.db'

conn = sqlite3.connect(db_filename)

with sqlite3.connect(db_filename) as conn:
    cursor = conn.cursor()

    cursor.execute("""SELECT * FROM part_desc""")

    for row in cursor.fetchall():
        part, description = row
        print('Part {} is a {}'.format(part, description))

conn.close()