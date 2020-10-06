import sqlite3


conn = sqlite3.connect('homework5.db')
c = conn.cursor()
c.execute('CREATE TABLE IF NOT EXISTS numbers(number INTEGER)')
number1 = int(input("Enter a number:  "))
c.execute('INSERT INTO numbers VALUES(?)')

