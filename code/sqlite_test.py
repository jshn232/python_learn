#! /usr/bin/env/python3

import sqlite3

conn = sqlite3.connect('test.db')
print('sqlite3 connect')

conn.close()
conn.close()