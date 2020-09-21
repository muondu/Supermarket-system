import sqlite3
conn = sqlite3.connect('updating1.db')
c = conn.cursor()
name1 = "Malli"
age = 9
class1 = 5


age2 = 11
class2 = 7

def creates_db():
    c.execute('CREATE TABLE IF NOT EXISTS game_developers(name TEXT, age INTEGER, class VARCHAR)')
    c.execute('INSERT INTO game_developers VALUES(?,?,?)',(name1,age,class1))

creates_db()


input1 = input("Enter your class:  ")
input2 = int(input("Enter your age:  "))


def update():
    with conn:
        c.execute('UPDATE game_developers SET age = ? WHERE age = ?',(input2,age))
        c.execute('UPDATE game_developers SET class = ? WHERE class = ?',(input1,class1))
update()


def read():
    c.execute('SELECT * FROM game_developers')
    print(c.fetchall())
read()

input3 = input("Delete a class: ")
input4 = int(input("Delete an age:  "))

def delete():
    c.execute('DELETE FROM game_developers WHERE class = ?',(input3))
    read()
delete()