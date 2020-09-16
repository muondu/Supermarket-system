# import datetime
import sqlite3
conn = sqlite3.connect('stock.db')
c = conn.cursor()
import time
# now = datetime.datetime.now()
# hour = now.hour()
# if hour < 12:
#     print("Good morning")
# elif hour > 12 and hour < 17:
#     print("Good afternoon")
# elif hour > 17 and hour < 19:
#     print("Good evening")
# else:
#     print('Good night.')

def customer():
    print("Welcome to Nero Nesh supermarket")
    print("Please prosseed to the gate to get your car checked and get your ticket.")
    time.sleep(5)
    print("You can now go and look for parking.")
    found_parking = input("After you have found parking. Enter e:  ")
    if found_parking == "e" or found_parking == "E":
        print("You can now enter the supermarket")
        print("Make sure you have put on your mask")
        print("Please prosseed to the gate to get checked and make sure u put some sanitizer")
        print("Welcome to the supermarket")
        def categories():
            which_categorie = input("""
            Which category do you want
            a Food
            b ELectronics
            c Laundry
            d Hardware
            
            """)
            if which_categorie == "a" or which_categorie == "food" or which_categorie == "A" or which_categorie == "Food":
                def food():
                    c.execute('SELECT * FROM food')
                    dub = c.fetchall()
                    lala = [item for a in dub for item in a]
                    print(lala)
                    print("The name is the first word and the price in the second one")
                    which_food = input("Which food do you want:  ")
                    print("You have bought " + which_food)
                    
                food()
            elif which_categorie == "b" or which_categorie == "electronics" or which_categorie == "B" or which_categorie == "Electronics":
                def electronics():
                    c.execute('SELECT * FROM electronics')
                    dub = c.fetchall()
                    lala = [item for a in dub for item in a]
                    print(lala)
                    print("The name is the first word and the price in the second one")
                    which_food = input("Which food do you want:  ")
                    print("You have bought " + which_food)
                electronics()
            elif which_categorie == "c" or which_categorie == "laundry" or which_categorie == "C" or which_categorie == "Laundry":
                def laundry():
                    c.execute('SELECT * FROM laundry')
                    dub = c.fetchall()
                    lala = [item for a in dub for item in a]
                    print(lala)
                    print("The name is the first word and the price in the second one")
                    which_food = input("Which food do you want:  ")
                    print("You have bought " + which_food)
                laundry()
            elif which_categorie == "d" or which_categorie == "hardware" or which_categorie == "D" or which_categorie == "Hardware":
                def hardware():
                    c.execute('SELECT * FROM hardware')
                    dub = c.fetchall()
                    lala = [item for a in dub for item in a]
                    print(lala)
                    print("The name is the first word and the price in the second one")
                    which_food = input("Which food do you want:  ")
                    print("You have bought " + which_food)
                hardware()
            else:
                print("There is no such category")
            
        categories()


    else:
        print("I did not understand you")
customer()