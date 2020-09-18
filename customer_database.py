import sqlite3
donn = sqlite3.connect('bill.db')
conn = sqlite3.connect('customer_bought.db')
c = conn.cursor()
d = donn.cursor()

c.execute('CREATE TABLE IF NOT EXISTS customer_items(name TEXT, price INTEGER)')

d.execute('CREATE TABLE IF NOT EXISTS total(price VARCHAR)')
