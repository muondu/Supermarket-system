import sqlite3
conn = sqlite3.connect('homework3.db')
c = conn.cursor()


def create_table():
    c.execute('CREATE TABLE IF NOT EXISTS employee(name TEXT, salary INTEGER, department TEXT)')
    c.execute('CREATE TABLE IF NOT EXISTS department(salary INTEGER)')
create_table()
def insert_items():
    # with conn:
        # c.execute('INSERT INTO imform VALUES("Malli","10","Ugali")')
        # c.execute('INSERT INTO imform VALUES("Sharon","13","Fish")')
    c.execute('INSERT INTO employee VALUES("Sharon","1","Google")')
    c.execute('INSERT INTO employee VALUES("Malli","10","Facebook")')
    c.execute('INSERT INTO employee VALUES("Nesh","100","Youtuber")')
insert_items()
# def read():
    # c.execute('SELECT * FROM employee')
    # print(c.fetchall())
# read()

def add_food():
        
    salary = c.execute('SELECT department FROM employee WHERE salary = 1')
    sallary_results = c.fetchall()
    # print(food_results)
    for dub in sallary_results:
        print(dub)
        c.execute('INSERT INTO department VALUES(?)', dub)
        conn.commit()
        c.execute('SELECT * FROM department')
        print(c.fetchall())
add_food()