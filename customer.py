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
    def awsome():

        found_parking = input("After you have found parking. Enter e:  ")
        if found_parking == "e" or found_parking == "E":
            
                print("You can now enter the supermarket")
                print("Make sure you have put on your mask")
                print("Please prosseed to the gate to get checked and make sure you put some sanitizer")
                try:
                    def temperatur():
                        temperature = float(input("Pls input your temperature:  "))
                        if temperature > 36.9:
                            print("Yu cannot enter the supermarket coz we suspect u have covid 19")
                        elif temperature < 13.7:
                            print("THAT IS A LYE")
                        else:
                            print("Welcome to the supermarket")

                            def categories():
                                which_categorie = input("""
                                Which category do you want to shop from
                                a Food
                                b ELectronics
                                c Laundry
                                d Hardware
                                e Billing
                                
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
                                            d.execute('INSERT INTO total VALUES(?)',(food_bill,))
                                            donn.commit()
                                            categories()
                                        else:
                                            print("I did not understand you:/")
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
                                            electronics_bill += 10000
                                            print("You have bought a laptop for 1000 ksh")
                                            d.execute('INSERT INTO total VALUES(?)',(electronics_bill,))
                                            donn.commit()

                                            categories()
                                        else:
                                            print("I did not understand you:/")
                                            electronics()                

                                    electronics()
                                elif which_categorie == "c" or which_categorie == "laundry" or which_categorie == "C" or which_categorie == "Laundry":
                                    def laundry():
                                        global laundry_bill
                                        laundry_bill = 0
                                        c.execute('SELECT * FROM laundry')
                                        print(c.fetchall())

                                        which_laundry = input("Which laundry do you want:  ")
                                        if which_laundry == "soap" or which_laundry == "Soap":
                                            laundry_bill += 10
                                            print("You have bought soap for 10 ksh")
                                            d.execute('INSERT INTO total VALUES(?)',(laundry_bill,))
                                            donn.commit()
                                            
                                            categories()
                                        else:
                                            print("I did not understand you:/")
                                            laundry()                


                                    laundry()
                                elif which_categorie == "d" or which_categorie == "hardware" or which_categorie == "D" or which_categorie == "Hardware":
                                    def hardware():
                                        global hardware_bill
                                        hardware_bill = 0
                                        c.execute('SELECT * FROM hardware')
                                        print(c.fetchall())

                                        which_hardware = input("Which hardware do you want:  ")
                                        if which_hardware == "wheelbarrow" or which_hardware:
                                            hardware_bill += 1000
                                            print("You have bought a wheelbarrow for 1000 ksh")
                                            d.execute('INSERT INTO total VALUES(?)',(hardware_bill,))
                                            donn.commit()

                                            categories()
                                        else:
                                            print("I did not understand you:/")
                                            hardware()                

                    
                                    hardware()
                                elif which_categorie == "e" or which_categorie == "E":
                                    def total_amount():
                                        
                                        # print(bill)
                                        print("Your total price is ")
                                        global bill_total
                                        bill_total = 0

                                        for dub in d.execute('SELECT * FROM total'):
                                            bill_total += dub[0]
                                            print(bill_total)

                                        
                                        amount_cash = int(input("Enter amount paying here:  "))

                                        if amount_cash < bill_total:
                                            print("Please pay more or the equal amount")
                                            total_amount()
                                        elif amount_cash > bill_total:
                                            balance = amount_cash - bill_total
                                            print("Your change is " + str(balance))
                                            print("Good bye.:D")
                                        elif amount_cash == dub:
                                            print("Thankyou. Good bye:)")
                                        else:
                                            print("I did not understand you.:/")
                                            total_amount()
                                    total_amount()
                                elif which_categorie == "":
                                    print("You can't enter nothing")
                                    categories()
                                elif which_categorie == " ":
                                    print("You can't put spaces")
                                    categories()
                                else:
                                    print("There is no such category")
                                    categories()
                                
                            categories()
                    temperatur()
                except ValueError:
                    print("That is not a number")
                    temperatur()
        else:
            print("U did not input e :/.Please write e")
            awsome()
    awsome()
customer()