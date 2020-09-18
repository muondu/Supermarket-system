import sqlite3
conn = sqlite3.connect('homework2.db')
c = conn.cursor()

def create_table():
    c.execute('CREATE TABLE IF NOT EXISTS favorite(fav TEXT)')
    c.execute('CREATE TABLE IF NOT EXISTS imform(name TEXT, age INTEGER, fav TEXT)')
create_table()
def insert_items():
    # with conn:
        # c.execute('INSERT INTO imform VALUES("Malli","10","Ugali")')
        # c.execute('INSERT INTO imform VALUES("Sharon","13","Fish")')
    c.execute('INSERT INTO imform VALUES("Nesh","10","Pizza")')
    c.execute('INSERT INTO imform VALUES("Newton","10","Burger")')
    c.execute('INSERT INTO imform VALUES("Malli","12","Cake")')
insert_items()
def read():
    c.execute('SELECT * FROM imform')
    print(c.fetchall())
# read()

def add_food():
    food = c.execute('SELECT fav FROM imform WHERE age = 10')
    food_results = c.fetchall()
    # print(food_results)
    for dub in food_results:
        print(dub)
        c.execute('INSERT INTO favorite VALUES(?)', dub)
        c.execute('SELECT * FROM favorite')
        print(c.fetchall())
add_food()