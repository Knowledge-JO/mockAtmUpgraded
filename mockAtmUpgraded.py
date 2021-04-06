import time
import datetime
import random

database = {}
class bank:
    def __init__(self, account_balance):
        self.account_balance = account_balance
        
    #get current time
    def current_time(self):
        time_now= datetime.datetime.now()
        time_now = time_now.strftime("%Y-%m-%d-%H-%M")
        print("------------------------------------")
        print("CURRENT TIME: %s" %time_now)
        print("------------------------------------")


    #intiate bank
    def init_session(self):
        self.current_time()
        print('============================')
        print('WELCOME TO MEGBANK')
        print('********HAPPY EASTER********')
        print('============================')
        print('============================')
        print('1. OPEN ACCOUNT')
        print('2. LOGIN')
        print('3. EXIT')
        print('============================')
        try:
            option_selected = int(input('SELECT AN OPTION: '))
            if option_selected == 1:
                self.register_session()
            elif option_selected == 2:
                self.login_session()
            elif option_selected ==3:
                exit()
            elif option_selected != 1 or 2 or 3:
                print('----------------------------------')
                print('CHOOSE FROM AVAILABLE OPTIONS')
                print('----------------------------------')
                self.init_session()
        except ValueError:
            print('------------------------------')
            print('ONLY NUMBERS ARE ALLOWED')
            print('------------------------------')
            self.init_session()


    #open an account
    def register_session(self):
        print('============================')
        print('REGISTRATION')
        print('============================')
        self.first_name = input('ENTER YOUR FIRST NAME: ')
        self.last_name = input('ENTER YOUR LAST NAME: ')
        email_address = input('ENTER YOUR EMAIL ADDRESS: ')
        password = input('ENTER A PASSWORD: ')
        account_number = self.generate_account_number()
        database[account_number] = [self.first_name, self.last_name, email_address, password, self.account_balance]
        print('-------------------------------')
        print('ACCOUNT CREATION SUCCESSFUL')
        print('-----------------------------------')
        print('YOUR ACCOUNT NUMBER: %d' %account_number)
        print('-------------------------------------')
        print('ACCOUNT DETAILS MUST BE KEPT SAFE')
        print('-------------------------------------')
        self.login_session()


    def login_session(self):
        print('==========================')
        print('LOGIN')
        print('==========================')
        try:
            input_account_number = int(input('ENTER YOU ACCOUNT NUMBER: '))
            input_password = input('ENTER YOUR PASSWORD: ')
            for account_number, self.userDetails in database.items():
                if account_number == input_account_number:
                    if self.userDetails[3] == input_password:
                        print('---------------------------')
                        print('LOGIN SUCCESSFUL')
                        print('---------------------------')
                        self.bank_operations()
                
            print('----------------------------------')
            print('INVALID ACCOUNT NUMBER OR PASSWORD. TRY AGAIN')
            print('----------------------------------')
            self.login_session()
        except ValueError:
            print('-------------------------------------------')
            print('ACCOUNT NUMBER SHOULD BE IN NUMBERS ONLY')
            print('-------------------------------------------')
            self.login_session()


    def bank_operations(self):
        self.current_time()
        print("============================")
        print("WELCOME %s %s" %(self.userDetails[0], self.userDetails[1]))
        print("============================")
        print("1. WITHDRAWAL")
        print("2. DEPOSIT")
        print("3. CUSTOMER SERVICE") #formerly complaint
        print("4. LOGOUT")
        print("===========================")
        try:
            output = int(input('SELECT AN OPTION: '))
            if output == 1:
                self.withdraw_session()
            elif output == 2:
                self.deposit_session()
            elif output == 3:
                self.customer_service()
            elif output == 4:
                self.logout_session()
            elif output != 1 or 2 or 3 or 4:
                print('--------------------------------')
                print('CHOOSE FROM AVAILABLE OPTIONS')
                print('---------------------------------')
                self.bank_operations()
        except ValueError:
            print("-------------------------------")
            print('ONLY NUMBER ARE ALLOWED')
            print("-------------------------------")
            self.bank_operations()


    def withdraw_session(self):
        print("==============================")
        print("WITHDRAWAL")
        print("==============================")
        print("*****ACCOUNT BALANCE: %d" %self.account_balance)
        print("==============================")
        try:
            Withdrawal = int(input("HOW MUCH WOULD YOU LIKE TO WITHDRAW: "))
            balance_remaining = self.account_balance - Withdrawal
            if balance_remaining > 0:
                self.account_balance = balance_remaining
                print("-----------------------------")
                print("PROCESSING WITHDRAWAL.....")
                time.sleep(2)
                print("---------------------------")
                print("WITHDRAWAL SUCCESSFUL.")
                print("---------------------------------")
                print("ACCOUNT BALANCE UPDATED")
                print("----------------------------------------")
                print("*****ACCOUNT BALANCE: %d" %self.account_balance)
                print("---------------------------------------------")
                print("TAKE YOUR CASH")
                print("---------------------------")
                self.bank_operations()
            elif balance_remaining < 0:
                print("---------------------------------------------")
                print("INSUFFICIENT FUNDS. PLEASE MAKE A DEPOSIT")
                print("---------------------------------------------")
                print("*****ENTER 'Y' IF YES AND 'N' IF NO*****")
                while True:
                    make_deposit = input('*****DO YOU WANT TO MAKE A DEPOSIT: ')
                    if make_deposit == 'Y':
                        self.deposit_session()
                    elif make_deposit == 'N':
                        self.bank_operations()
                    elif make_deposit != 'Y' or 'N':
                        print("ENTER 'Y' OR 'N' ")
        except ValueError:
            print("---------------------------------------------")
            print("ENTER AMOUNT YOU WANT TO WITHDRAW IN NUMBERS")
            print("---------------------------------------------")
            self.withdraw_session()
            

    def deposit_session(self):
        print("=================")
        print("DEPOSIT")
        print("=================")
        print("-------------------------------------")
        print("*****ACCOUNT BALANCE: %d" %self.account_balance)
        try:
            deposit = int(input("HOW MUCH WOULD YOU LIKE TO DEPOSIT: "))
            new_balance = self.account_balance + deposit
            print("------------------------------------")
            print("PLEASE WAIT...")
            time.sleep(2)
            print("------------------------------------")
            print("DEPOSIT SUCCESSFUL")
            print("------------------------------------")
            print("ACCOUNT BALANCE UPDATED")
            self.account_balance = new_balance
            print("----------------------------------------")
            print("*****ACCOUNT BALANCE: %d" %self.account_balance)
            print("---------------------------------------------")
            self.bank_operations()
        except ValueError:
            #print("----------------------------------------------------")
            print("ENTER AMOUNT YOU WOULD LIKE TO DEPOSIT IN NUMBERS")
            print("----------------------------------------------------")
            self.deposit_session()


    def generate_account_number(self):
        return random.randrange(1111111111, 9999999999)


    def customer_service(self):
        print('------------------------------------')
        complaint = input("WHAT ISSUE WILL YOU LIKE TO REPORT: ")
        print("------------------------------------")
        print("THANK YOU FOR CONTACTING US")
        print("-------------------------------------------")
        print("WE WILL GET IN TOUCH AS SOON AS POSSIBLE")
        print("-------------------------------------------")
        self.bank_operations()


    def logout_session(self):
        print('---------------------------------')
        print('THANK YOU FOR USING OUR SERVICE')
        print('---------------------------------')
        self.init_session()
    

default_account_balance = 0 
obj = bank(default_account_balance)
obj.init_session()
