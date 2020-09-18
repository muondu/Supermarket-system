import sqlite3
conn = sqlite3.connect('pracise1.db')
c = conn.cursor()

def create_table():
    c.execute('CREATE TABLE IF NOT EXISTS imfrom( name TEXT, age INTEGER, food VARCHAR)')
    c.execute('CREATE TABLE IF NOT EXISTS store( name TEXT, age INTEGER, food VARCHAR)')
    c.execute('CREATE TABLE IF NOT EXISTS food( name TEXT, food VARCHAR)')
create_table()
def insert_values():
    global name
    name = input("Enter your name: ")
    age = int(input("Enter your age:  "))
    food = input("Enter your favorite food:  ")
    with conn:
        c.execute('INSERT INTO imfrom VALUES(?,?,?)',(name, age, food))
        c.execute('INSERT INTO store VALUES(?,?,?)',(name, age, food))
        print("Yay")
        
insert_values()
def read():
    c.execute('SELECT * FROM imfrom')
    print(c.fetchall())
    c.execute('SELECT * FROM store ')
    print(c.fetchall())
read()

def store_food():
    favorite_food = c.execute('SELECT food WHERE age = 10')
    favorite_food_11 = c.execute('SELECT food WHERE age = 11')
    favorite_food_12 = c.execute('SELECT food WHERE age = 12')
    with conn:
        c.execute('INSERT INTO food VALUES(?,?)',(name, favorite_food))
        c.execute('INSERT INTO food VALUES(?,?)',(name, favorite_food_11))
        c.execute('INSERT INTO food VALUES(?,?)',(name, favorite_food_12))
store_food()
