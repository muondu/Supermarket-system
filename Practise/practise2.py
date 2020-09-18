import sqlite3
conn = sqlite3.connect('practise2.db')
c = conn.cursor()
def create_table():
    c.execute('CREATE TABLE IF NOT EXISTS comal(name TEXT, age INTEGER)')
create_table()
def insert_values():
    with conn:
        c.execute('INSERT INTO comal VALUES("Unreal engine",11)')
insert_values()
        
def read():
    c.execute('SELECT * FROM comal')
    print(c.fetchall())
read()

def find():
    age = c.execute('SELECT * FROM comal WHERE age = 11')
    print(age)
    for dub in age:
        print(dub)
    # print(c.fetchall())
find()