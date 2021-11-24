import math
from os import name
import pandas as pd

class User:
    def __init__(self, id, name, password):
        self.id = id
        self.name = name
        self.password = password

class Account (User):
    def __init__(self, id, name, password):
        self.balance = 0
        User.__init__(self, id, name, password)

    def credit(self, x=0, y=0):
        amount = x + y/100
        self.balance = round((self.balance + amount), 2)

    def debit(self, x=0, y=0):
        amount = x + y/100
        self.balance = round((self.balance - amount), 2)

    def check(self):
        c, d = math.modf(self.balance)
        c = int(100*c)
        d = int(d)
        if d == 0:
            print("Current Balance: "+ str(c) + "C")
        elif c == 0:
            print("Current Balance: "+ str(d) + "D")
        else:
            print("Current Balance: "+ str(d) + "D " + str(c) + "C")

if __name__ == '__main__':

    userdf = pd.read_csv('Database.csv')
    print('Select an option:')
    print('1. New user')
    print('2. Login')
    print('3. Exit')
    opt = int(input())
    if opt == 1:
        name = input('Enter Name: ')
        password = input('Enter Password: ')
        user = Account(len(userdf)+1, name, password)
        userdf.loc[len(userdf)] = (len(userdf)+1, name, password, user.balance)
    elif opt == 2:
        name = input('Enter Name: ')
        password = input('Enter Password: ')
        if len(userdf[(userdf['Name']==name) & (userdf['Password']==password)]) == 0:
            exit(0)
        else:
            ind = userdf.index(userdf[(userdf['Name']==name) & (userdf['Password']==password)])
    elif opt == 3:
        exit(0)

    while True:
        print('Select an option: ')
        print('1. Credit')
        print('2. Debit')
        print('3. Check Balance')
        print('4. Exit')
        option = int(input())
        if option == 1:
            amount = input('Enter Amount: ').split()
            if len(amount) == 2:
                x = int(amount[0][:-1])
                y = int(amount[1][:-1])
            else:
                if amount[0][-1] == 'D':
                    x = int(amount[0][:-1])
                    y = 0
                elif amount[0][-1] == 'C':
                    x = 0
                    y = int(amount[0][:-1])
            user.credit(x, y)
        elif option == 2:
            amount = input('Enter Amount: ').split()
            if len(amount) == 2:
                x = int(amount[0][:-1])
                y = int(amount[1][:-1])
            else:
                if amount[0][-1] == 'D':
                    x = int(amount[0][:-1])
                    y = 0
                elif amount[0][-1] == 'C':
                    x = 0
                    y = int(amount[0][:-1])
            user.debit(x, y)
        elif option == 3:
            user.check()
        elif option == 4:
            break






