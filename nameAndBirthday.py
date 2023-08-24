import datetime

name = input("What's your name? ")
birthMonth = input("What month were you born in? ")

while type(birthMonth) == type(name):
    try : birthMonth = int(birthMonth)
    except : birthMonth = input("Please enter the number of your birth month. ")

print("Hi " + name + "!")

dateToday = datetime.date.today()

if (dateToday.month == birthMonth):
    print("Happy birthday " + name + "!")

print("There are " + str(len(name)) + " letters in your name.")
