# import datetime
import sqlite3
donn = sqlite3.connect('bill.db')
d = donn.cursor()
conn = sqlite3.connect('stock.db')
c = conn.cursor()

# import time
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
    # time.sleep(5)
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
            e Nothing else
            
            """)
            if which_categorie == "a" or which_categorie == "food" or which_categorie == "A" or which_categorie == "Food":
                def food():
                    global food_bill
                    food_bill = 0
                    c.execute('SELECT * FROM food')
                    print(c.fetchall())

                    which_food = input("Which food do you want:  ")
                    if which_food == "bread" or which_food == "Bread":
                        food_bill += 50
                        print("You have bought break for 50 ksh")
                        categories()
                    else:
                        print("I did not understand you")
                        food()
                food()
            elif which_categorie == "b" or which_categorie == "electronics" or which_categorie == "B" or which_categorie == "Electronics":
                def electronics():
                    global electronics_bill
                    electronics_bill = 0
                    c.execute('SELECT * FROM electronics')
                    print(c.fetchall())

                    which_electronic = input("Which electronic do you want:  ")
                    if which_electronic == "Laptop":
                        electronics_bill += 1000
                        print("You have bought a laptop for 1000 ksh")

                        categories()
                    else:
                        print("I did not understand you")
                        electronics()                

                electronics()
            elif which_categorie == "c" or which_categorie == "laundry" or which_categorie == "C" or which_categorie == "Laundry":
                def laundry():
                    global laundry_bill
                    laundry_bill = 0

                    which_laundry = input("Which laundry do you want:  ")
                    if which_laundry == "soap" or which_laundry == "Soap":
                        laundry_bill += 10
                        print("You have bought soap for 10 ksh")
                        
                        categories()
                    else:
                        print("I did not understand you")
                        laundry()                
 

                laundry()
            elif which_categorie == "d" or which_categorie == "hardware" or which_categorie == "D" or which_categorie == "Hardware":
                def hardware():
                    global laundry_bill
                    hardware_bill = 0
                    c.execute('SELECT * FROM hardware')
                    print(c.fetchall())

                    which_hardware = input("Which hardware do you want:  ")
                    if which_hardware == "wheelbarrow" or which_hardware:
                        hardware_bill += 1000
                        print("You have bought a wheelbarrow for 1000 ksh")

                        categories()
                    else:
                        print("I did not understand you")
                        hardware()                


                hardware()
            elif which_categorie == "e" or which_categorie == "E":
                def total_amount():
                    
                    # print(bill)
                    print("Your total price is ")

                    total_bill = s
                    print(total_bill)
                    amount_cash = int(input("Enter amount paying here:  "))
                    if amount_cash < total_bill:
                        remaining = dub - amount_cash
                        print("You are still remaining with " + str(remaining))
                        total_amount()
                    elif amount_cash > total_bill:
                        balance = amount_cash - dub
                        print("Your change is " + str(balance))
                        print("Good bye")
                    elif amount_cash == total_bill:
                        print("Thankyou. Good bye")
                    else:
                        print("I did not understand you")
                        total_amount()
                total_amount()
            else:
                print("There is no such category")
            
        categories()


    else:
        print("I did not understand you")
customer()