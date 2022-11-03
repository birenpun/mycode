#!/usr/bin/python3

import sqlite3
conn = sqlite3.connect('challange.db')
print("Opened database successfully")

cursor = conn.execute("SELECT id, band, hometown, year from thursday")
for row in cursor:
    print("ID = ", row[0])
    print("band = ", row[1])
    print("hometown = ", row[2])
    print("year = ", row[3], "\n")

print("Operation done successfully")
conn.close()


