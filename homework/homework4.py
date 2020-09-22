import sqlite3

conn = sqlite3.connect('homework4.db')
c = conn.cursor()

def create_table():
    c.execute('CREATE TABLE IF NOT EXISTS imformation(name TEXT, age INTEGER, class INTEGER)')
    c.execute('INSERT INTO imformation VALUES("Nesh",11,"7")')
create_table()



def activities():
    global activities
    activities = input("""
    These are the activites

    a See everyone
    b Add someone
    c Remove someone
    
    d Quit program

    Which activites do you want:

    
    """)
activities()
if activities == "a":
    def read():
        c.execute('SELECT * FROM imformation')
        print(c.fetchall())
        # activities()
    read()
elif activities == "b":
    def update():
        old_name = input("Enter the old name:  ")
        old_age = int(input("Enter the old age:  "))
        old_class = input("Enter the old class:  ")
        new_name = input("Enter your name:  ")
        new_age = int(input("Enter your age:  "))
        new_class = input("Enter your class:  ")
        with conn:
            c.execute('UPDATE imformation SET name = ? WHERE name = ?',(old_name,new_name))
            c.execute('UPDATE imformation SET age = ? WHERE age = ?',(old_age,new_age))
            c.execute('UPDATE imformation SET class = ? WHERE class = ?',(old_class,new_class))
        # activities()
    update()

elif activities == "c":
    delete_name = input("Enter the deleting name:  ")
    delete_age = int(input("Enter the deleting age:  "))
    delete_class = input("Enter the deleting class:  ")
    def delete():
        c.execute('DELETE FROM imformation WHERE name = ?',(delete_name))
        c.execute('DELETE FROM imformation WHERE age = ?',(delete_age))
        c.execute('DELETE FROM imformation WHERE class = ?',(delete_class))
        read()
        # activities()
    delete()
elif activities == "d":
    print("Good bye.")
    exit()
else:
    print("I did not unsderstand you")


