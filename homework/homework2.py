import sqlite3
conn = sqlite3.connect('homework2.db')
c = conn.cursor()

def create_table():
    c.execute('CREATE TABLE IF NOT EXISTS favorite(fav TEXT)')
    c.execute('CREATE TABLE IF NOT EXISTS imform(name TEXT, age INTEGER, fav TEXT)')
create_table()
def insert_items():
    c.execute('INSERT INTO imform VALUES("Malli","10","Ugali")')
    c.execute('INSERT INTO imform VALUES("Sharon","13","Fish")')
    c.execute('INSERT INTO imform VALUES("Nesh","11","Not a question")')
    c.execute('INSERT INTO imform VALUES("Malli","9","Pizza")')
insert_items()
def check_age():
    favorite-food = c.execute('SELECT fav WHERE age = 10')
    favorite-food2 = c.execute('SELECT fav WHERE age = 11')
    favorite-food3 = c.execute('SELECT favofavrite_food WHERE age = 12')
check_age()
def add_favorite_food():
    c.execute('INSERT INTO favorite VALUES("?")',favorite-food,favorite-food2,favorite-food3)
add_favorite_food()