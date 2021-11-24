import math



class Account:
    def __init__(self):
        self.balance = 0

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
    user = Account()

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






