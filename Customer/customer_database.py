import sqlite3
conn = sqlite3.connect('customer_bought.db')
c = conn.cursor()

c.execute('CREATE TABLE IF NOT EXISTS items(name TEXT, price INTEGER)')
