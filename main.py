import csv
import getpass
import time
import random
import os
import sys
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

font1 = {'family': 'Comic Sans MS',
         'weight': 'bold', 'color': '#f73f02', 'size': 15}

font2 = {'family': 'Comic Sans MS',
         'color': 'red', 'size': 20, 'weight': 'bold', }


def clear(): return os.system('cls' if os.name == 'nt' else 'clear')


def getpath(name):
    filepath = os.path.dirname(os.path.realpath(__file__)) + "\\" + str(name)
    return filepath


def dtc(d):
    if (d == "monday" or d == "mon"):
        return 1
    elif (d == "tuesday" or d == "tues"):
        return 2
    elif (d == "wednesday" or d == "wed"):
        return 3
    elif (d == "thursday" or d == "thur"):
        return 4
    elif (d == "friday" or d == "fri"):
        return 5
    elif (d == "saturday" or d == "sat"):
        return 6
    elif (d == "sunday" or d == "sun"):
        return 7
    else:
        return 9


def ttc(t):
    if (t == "morning" or t == "day"):
        return 1
    elif (t == "afternoon" or t == "noon"):
        return 2
    elif (t == "evening"):
        return 3
    elif (t == "night" or t == "midnight"):
        return 4
    else:
        print("Invalid time entry!")
        return 9


def addBooking():
    bookings = []
    pricedata = []
    data = []
    with open(getpath("cinema.csv")) as csvfile:
        reader = csv.reader(csvfile)
        for row in reader:
            data.append(row)

    bookingref = random.randint(1, 200)
    bookingref = str(bookingref)

    col2 = [x[0] for x in data]

    clear()

    if bookingref in col2:
        bookingref = int(bookingref)
        bookingref2 = random.randint(1, 1000)
        newbookingref = bookingref * bookingref2
        newbookingref = str(newbookingref)

        print("The booking ref is:", newbookingref)
        print("\n")

        forename = input("Enter forename: ")
        surname = input("Enter surname: ")

        print("\n\n")
        print("List of available movies:")
        print("\n")
        data = []

        with open(getpath("Movies/list.csv")) as csvfile:
            reader = csv.reader(csvfile)
            for row in reader:
                data.append(row)
        for k in range(0, len(data)):
            print(str(data[k])[2:len(str(data[k]))-2])
        print("\n\n")

        film = input("Enter film name: ").lower()

        file = getpath("Movies/" + film + ".csv")

        try:
            with open(file) as csvfile:
                reader = csv.reader(csvfile)
                for row in reader:
                    pricedata.append(row)
        except:
            import time
            print("\n\nInvalid Film Name!")
            time.sleep(2)
            userMenu()

        price = pd.read_csv(file, index_col="day")
        print("\n")
        print(price)
        print("\n")

        date = str(input("Enter the date(dd-mm-yyyy): "))

        day = input("Enter day: ").lower()
        dcode = dtc(day)
        if dcode == 9:
            exit()

        time = input("Enter time of the day: ").lower()
        tcode = ttc(time)
        if tcode == 9:
            exit()

        quantity = int(
            input("Enter the amount of tickets you want to purchase: "))

        rate = int(pricedata[dcode][tcode])
        cost = int(rate * quantity)

        print("\n\nConfirm your details:\n")
        print('Your name: ' + forename + ' ' + surname)
        print('Your booking number: ' + bookingref)
        print('Selected film: ' + film)
        print('Chosen date, day and time: ' + date + ' ' + day + ' ' + time)
        print('\nAmount of tickets: ' + str(quantity))
        print('Rate of each ticket: ' + str(rate))
        print('\nTotal booking cost: ' + str(cost))

        choice = input('\n\nAre you sure about your booking (y/n): ').lower()

        if (choice == 'y' or choice == 'yes'):
            bookings.append(newbookingref)
            bookings.append(forename)
            bookings.append(surname)
            bookings.append(film)
            bookings.append(date)
            bookings.append(day)
            bookings.append(time)
            bookings.append(quantity)
            bookings.append(rate)
            bookings.append(cost)

            with open(getpath("cinema.csv"), "a", newline='') as csvfile:
                writer = csv.writer(csvfile)
                writer.writerow(bookings)
            anim("Adding your booking")
            clear()
            print("Booking successfull!\n\n")
            input("Press Enter to continue...")
        else:
            exit()
    else:
        print("The booking ref is:", bookingref)
        print("\n")
        forename = input("Enter forename: ")
        surname = input("Enter surname: ")
        print("\n\n")
        print("List of available movies:")
        print("\n")
        data = []

        with open(getpath("Movies/list.csv")) as csvfile:
            reader = csv.reader(csvfile)
            for row in reader:
                data.append(row)
        for k in range(0, len(data)):
            print(str(data[k])[2:len(str(data[k]))-2])
        print("\n\n")

        film = input("Enter film name: ").lower()

        file = getpath("Movies/" + film + ".csv")

        try:
            with open(file) as csvfile:
                reader = csv.reader(csvfile)
                for row in reader:
                    pricedata.append(row)
        except:
            import time
            print("\n\nInvalid Film Name!")
            time.sleep(2)
            userMenu()

        price = pd.read_csv(file, index_col="day")
        print('\n')
        print(price)
        print('\n')

        date = str(input("Enter the date(dd-mm-yyyy): "))
        day = input("Enter day: ").lower()
        dcode = dtc(day)
        if dcode == 9:
            exit()

        time = input("Enter time of the day: ").lower()
        tcode = ttc(time)
        if tcode == 9:
            exit()

        quantity = int(
            input("Enter the amount of tickets you want to purchase: "))
        rate = int(pricedata[dcode][tcode])
        cost = int(rate * quantity)

        print("\n\nConfirm your details:\n")
        print('Your name: ' + forename + ' ' + surname)
        print('Your booking number: ' + bookingref)
        print('Selected film: ' + film)
        print('Chosen date: ' + date)
        print('Chosen day and time: ' + day + ' ' + time)
        print('\nAmount of tickets: ' + str(quantity))
        print('Rate of each ticket: ' + str(rate))
        print('\nTotal booking cost: ' + str(cost))

        choice = input('\n\nAre you sure about your booking (y/n): ').lower()

        if (choice == 'y' or choice == 'yes'):
            bookings.append(bookingref)
            bookings.append(forename)
            bookings.append(surname)
            bookings.append(film)
            bookings.append(date)
            bookings.append(day)
            bookings.append(time)
            bookings.append(quantity)
            bookings.append(rate)
            bookings.append(cost)

            with open(getpath("cinema.csv"), "a", newline='') as csvfile:
                writer = csv.writer(csvfile)
                writer.writerow(bookings)
            anim("Adding your booking")
            clear()
            print("Booking successfull!\n\n")
            input("Press Enter to continue...")
        else:
            exit()


def delBooking():
    df = pd.read_csv(getpath("cinema.csv"), index_col=0)
    ref_no = input("\n\nEnter the reference number of your booking: ")

    choice = input(
        "\nAre you sure you want to delete this booking? (y/n): ").lower()
    if (choice != "y"):
        exit()
    df.drop(int(ref_no), inplace=True)

    anim("Canceling your booking")

    os.remove(getpath("cinema.csv"))

    df.to_csv(getpath("cinema.csv"))
    print("\nBooking successfully removed!\n\n")


def filmAppend(a, b, c, d, e, f, g, file):
    with open(file, "a", newline='') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(["day", "morning", "noon", "evening", "night"])
        writer.writerow(a)
        writer.writerow(b)
        writer.writerow(c)
        writer.writerow(d)
        writer.writerow(e)
        writer.writerow(f)
        writer.writerow(g)


def addFilm():
    name = input("\n\nEnter name of the movie: ").lower()
    rate = int(input("Enter the base rate: "))
    file = getpath('Movies/' + name + '.csv')

    with open(file, 'wb') as csvfile:
        filewriter = csv.writer(
            csvfile, delimiter=',', quotechar='|', quoting=csv.QUOTE_MINIMAL)

    a = []
    b = []
    c = []
    d = []
    e = []
    f = []
    g = []

    a.append("monday")
    a.append(rate)
    a.append(rate + 10)
    a.append(rate + 20)
    a.append(rate + 30)

    b.append("tuesday")
    b.append(rate)
    b.append(rate + 10)
    b.append(rate + 20)
    b.append(rate + 30)

    c.append("wednesday")
    c.append(rate)
    c.append(rate + 10)
    c.append(rate + 20)
    c.append(rate + 30)

    d.append("thursday")
    d.append(rate)
    d.append(rate + 10)
    d.append(rate + 20)
    d.append(rate + 30)

    e.append("friday")
    e.append(rate)
    e.append(rate + 10)
    e.append(rate + 20)
    e.append(rate + 30)

    wRate = rate * 2
    f.append("saturday")
    f.append(wRate)
    f.append(wRate + 20)
    f.append(wRate + 40)
    f.append(wRate + 60)

    g.append("sunday")
    g.append(wRate)
    g.append(wRate + 20)
    g.append(wRate + 40)
    g.append(wRate + 60)

    filmAppend(a, b, c, d, e, f, g, file)

    film = []
    film.append(name)

    with open(getpath("Movies/list.csv"), "a", newline='') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(film)

    anim("Creating file")
    clear()
    print("\nFile created successfully")
    input("\n\nPress Enter to continue...")


def removeFilm():

    name = input("\n\nEnter name of the movie: ").lower()
    choice = input("\nAre you sure you want to remove the file for " + name +
                   " (y/n): ").lower()

    if (choice == 'y'):
        file = getpath('Movies/' + name + '.csv')
        os.remove(file)

        df = pd.read_csv(getpath("Movies/list.csv"), index_col=0)
        df.drop(name, inplace=True)

        anim("Removing the film")

        os.remove(getpath("Movies/list.csv"))

        df.to_csv(getpath("Movies/list.csv"))
        print("\n\n")
        print(name + ".csv" + " has been removed!")

        input("\n\nPress Enter to continue...")


def searchRef():
    data = []
    with open(getpath("cinema.csv")) as csvfile:
        reader = csv.reader(csvfile)
        for row in reader:
            data.append(row)

    lookup = input("Please enter the reference number: ")
    lookup = lookup.lower()

    col1 = [x[0] for x in data]

    if lookup in col1:
        for k in range(0, len(col1)):
            if col1[k] == lookup:
                print("\n")
                print(data[k])
        input("\n\nPress Enter to continue...")
    else:
        print("\n\nNo booking found!")
        time.sleep(2)


def searchFilm():
    data = []
    with open(getpath("cinema.csv")) as csvfile:
        reader = csv.reader(csvfile)
        for row in reader:
            data.append(row)

    lookup = input("Please enter the film name: ")
    lookup = lookup.lower()

    col4 = [x[3] for x in data]

    if lookup in col4:
        print("\n\n")
        print(data[0])
        print("\n")
        for k in range(0, len(col4)):
            if col4[k] == lookup:
                print(data[k])
        input("\n\nPress Enter to continue...")
    else:
        print("No booking for the film found!")


def filmPricing():
    data = []
    dataNames = []

    print("\n\nList of available movies:\n")

    with open(getpath("Movies/list.csv")) as csvfile:
        reader = csv.reader(csvfile)
        for row in reader:
            dataNames.append(row)

        for k in range(0, len(dataNames)):
            print(str(dataNames[k])[2:len(str(dataNames[k]))-2])
        print("\n\n")

    filmname = input("Please enter the film name: ").lower()

    file = getpath("Movies/" + filmname + ".csv")

    try:
        with open(file) as csvfile:
            reader = csv.reader(csvfile)
            for row in reader:
                data.append(row)
    except:
        import time
        print("\n\nInvalid film name!")
        time.sleep(2)
        clear()
        userMenu()

    day = input("Please enter the day: ").lower()

    if (dtc(day) != 9):
        print("\n")
        print(data[dtc(day)])
        print("\n\n")
        input("Press Enter to continue...")
    else:
        print("Invalid day entry!")
        input("\n\nPress Enter to continue...")


def anim(string):
    clear()
    print(string)
    time.sleep(0.6)
    clear()
    print(string+".")
    time.sleep(0.6)
    clear()
    print(string+"..")
    time.sleep(0.6)
    clear()
    print(string+"...")
    time.sleep(0.6)


def salesGraph():
    data = []
    dataNames = []
    films = []
    earnings = []
    with open(getpath("cinema.csv")) as csvfile:
        reader = csv.reader(csvfile)
        for row in reader:
            data.append(row)

    with open(getpath("Movies/list.csv")) as csvfile:
        reader = csv.reader(csvfile)
        for row in reader:
            dataNames.append(row)

    Names = [x[0] for x in dataNames]

    for n in Names:
        temp = 0
        lookup = n
        films.append(n)

        colCost = [x[9] for x in data]
        colNames = [x[3] for x in data]

        if lookup in colNames:
            for k in range(0, len(colCost)):
                if colNames[k] == lookup:
                    temp += int(colCost[k])
        earnings.append(temp)

    plt.bar(films, earnings, width=0.4)

    plt.xlabel("Movie Names", fontdict=font1)
    plt.ylabel("Profit Earned", fontdict=font1)
    plt.title("Sales Graph", fontdict=font2)
    plt.show()

    input("\nPress Enter to continue...")


def ticketChart():
    data = []
    dataNames = []
    films = []
    amount = []

    with open(getpath("cinema.csv")) as csvfile:
        reader = csv.reader(csvfile)
        for row in reader:
            data.append(row)

    with open(getpath("Movies/list.csv")) as csvfile:
        reader = csv.reader(csvfile)
        for row in reader:
            dataNames.append(row)

    Names = [x[0] for x in dataNames]

    for n in Names:
        temp = 0
        lookup = n
        films.append(n)

        colAmnt = [x[7] for x in data]
        colNames = [x[3] for x in data]

        if lookup in colNames:
            for k in range(0, len(colAmnt)):
                if colNames[k] == lookup:
                    temp += int(colAmnt[k])
        amount.append(temp)

    total = 0
    for x in amount:
        total += x

    percentages = []

    for x in amount:
        temp = x / total
        percentages.append(float(temp))

    plt.pie(percentages, labels=films)

    plt.title("Ticket Sales", fontdict=font2)
    plt.show()

    input("\nPress Enter to continue...")


def adminMenu():
    clear()
    print("Welcome to Cinema Booking System")
    print("\n\n-----------")
    print("ROOT ACCESS")
    print("-----------\n\n")
    print("Select a feature you want to access: \n")
    print("1  -  List bookings for a film")
    print("2  -  Find a booking with its id")
    print("3  -  Add new film")
    print("4  -  Remove existing film")
    print("5  -  Sales profit graph")
    print("6  -  Sold tickets' pie chart")
    print("7  -  Go back to login page")
    print("8  -  Exit app\n\n")
    choice = int(input("Please enter your choice: "))

    if choice == 1:
        searchFilm()
    elif choice == 2:
        searchRef()
    elif choice == 3:
        addFilm()
    elif choice == 4:
        removeFilm()
    elif choice == 5:
        clear()
        salesGraph()
    elif choice == 6:
        clear()
        ticketChart()
    elif choice == 7:
        a = str(input("\n\nAre you sure you want to go back to login? (y/n): ")).lower()
        if a == "y":
            clear()
            print("Taking you back to login.")
            time.sleep(1)
            clear()
            print("Taking you back to login..")
            time.sleep(1)
            login()
        else:
            adminMenu()
    elif choice == 8:
        a = str(input("\n\nAre you sure you want to exit the app? (y/n): ")).lower()
        if a == "y":
            anim("Exiting app")
            clear()
            exit()
        else:
            adminMenu()
    elif choice == 909:
        print("Test command\n\n")
        input()
    else:
        print("\nInvalid selection!")
        time.sleep(1)

    adminMenu()


def userMenu():
    clear()
    print("Welcome to Cinema Booking System")
    print("Select a feature you want to access: \n")
    print("1  -  Make a booking")
    print("2  -  Check ticket rates")
    print("3  -  Cancel your booking")
    print("4  -  Go back to login page")
    print("5  -  Exit app\n\n")
    choice = int(input("Please enter your choice: "))

    if choice == 1:
        addBooking()
    elif choice == 2:
        filmPricing()
    elif choice == 3:
        delBooking()
    elif choice == 4:
        a = str(input("\n\nAre you sure you want to go back to login? (y/n): ")).lower()
        if a == "y":
            clear()
            print("Taking you back to login.")
            time.sleep(1)
            clear()
            print("Taking you back to login..")
            time.sleep(1)
            login()
        else:
            userMenu()
    elif choice == 5:
        a = str(input("\n\nAre you sure you want to exit the app? (y/n): ")).lower()
        if a == "y":
            anim("Exiting app")
            clear()
            exit()
        else:
            userMenu()
    else:
        print("\nInvalid selection!")
        time.sleep(1)
    userMenu()


def userLogin():
    clear()
    print("User Login Page\n\n")
    username = input("Enter your username: ")

    data = []
    with open(getpath("users.csv")) as csvfile:
        reader = csv.reader(csvfile)
        for row in reader:
            data.append(row)

    lookup = username

    col1 = [x[0] for x in data]
    col2 = [x[1] for x in data]

    x = 5

    if lookup in col1:
        for k in range(0, len(col1)):
            if col1[k] == lookup:
                while x > 0:
                    clear()
                    print("User Login Page\n\n")
                    print("Enter your username:", username)
                    passwd = getpass.getpass(prompt="Enter your password: ")
                    if col2[k] == passwd:
                        anim("Logging In")
                        time.sleep(1)
                        clear()
                        print("Logged in as", username)
                        x = -5
                        userMenu()
                    else:
                        print("\nIncorrect password!")
                        x -= 1
                        print(str(x) + " tries left\n")
                        time.sleep(2)
                if x != -5:
                    clear()
                    sys.exit()
    else:
        print("User not found!")


def userSignUp():
    i = 0
    while i == 0:
        clear()
        print("User Sign Up Page\n\n")

        u = str(input("Enter a new username: "))

        data = []
        with open(getpath("users.csv")) as csvfile:
            reader = csv.reader(csvfile)
            for row in reader:
                data.append(row)

        lookup = u

        col1 = [x[0] for x in data]

        if lookup in col1:
            print("\nUsername already taken")
            time.sleep(1)
            continue
        else:
            username = lookup
            break

    password = getpass.getpass(prompt="Enter a password: ")
    check = getpass.getpass(prompt="Confirm your password: ")
    if password != check:
        print("The entered passwords don't match")
    else:
        input("\n\nPress Enter to confirm...")
        anim("Creating account")
        clear()
        print("User account successfully created!")
        time.sleep(1)
        with open(getpath("users.csv"), "a", newline='') as csvfile:
            writer = csv.writer(csvfile)
            writer.writerow([username, password])
        input("\n\nPress Enter to continue...")
        userLogin()


def adminLogin():
    attempts = 0
    while(attempts < 3):
        clear()
        print("ADMIN LOGIN\n\n")
        username = str(input("Enter the admin username: "))
        if(username != "root"):
            print("Incorrect username!")
            attempts += 1
            print((3 - attempts), " tries left")
            time.sleep(2)
            continue
        elif(username == "root"):
            attempts = 0
            while(attempts < 3):
                clear()
                print("ADMIN LOGIN\n\n")
                print("Enter the admin username: root")
                password = getpass.getpass(
                    prompt="Enter the admin password : ")
                if(password != "toor"):
                    print("Incorrect password!")
                    attempts += 1
                    print((3 - attempts), " tries left")
                    time.sleep(2)
                    continue
                elif(password == "toor"):
                    anim("Logging In")
                    adminMenu()
                    break
            else:
                clear()
                exit()
    else:
        clear()
        exit()


def login():
    clear()
    print("Welcome to the Cinema Booking System")
    print("Select an access level to login at: \n")
    print("1  -  Admin Login")
    print("2  -  User Login")
    print("3  -  New User Sign Up\n\n")
    access = int(input("Please enter your choice: "))

    if access == 1:
        adminLogin()
    elif access == 2:
        userLogin()
    elif access == 3:
        userSignUp()
    elif access == 202:
        userMenu()
    elif access == 101:
        adminMenu()
    else:
        print("\nInvalid selection!\n\n")


login()
