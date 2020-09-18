import sqlite3

conn = sqlite3.connect('stock.db')
c = conn.cursor()

c.execute('CREATE TABLE IF NOT EXISTS food(name TEXT, price INTEGER)')

c.execute('CREATE TABLE IF NOT EXISTS laundry(name TEXT, price INTEGER)')

c.execute('CREATE TABLE IF NOT EXISTS electronics(name TEXT, price INTEGER)')
c.execute('CREATE TABLE IF NOT EXISTS hardware(name TEXT, price INTEGER)')



def insert():
    c.execute('INSERT INTO food VALUES("bread","50")')
    c.execute('INSERT INTO laundry VALUES("Soap","10")')

    c.execute('INSERT INTO electronics VALUES("Laptop","10000")')

    c.execute('INSERT INTO hardware VALUES("Wheelbarrow","1000")')

insert()
conn.commit()
c.execute('SELECT * FROM food')

# c.execute('SELECT * FROM laundry')
# c.execute('SELECT * FROM electronics')
# c.execute('SELECT * FROM hardware')
# print(c.fetchall())