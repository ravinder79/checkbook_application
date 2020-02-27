
import datetime
import csv
from dateutil.parser import parse
print("~~~ Welcome to your terminal checkbook! ~~~")


# This function checks if a user input for credit or debit is valid input or not.
def is_number(string):
    while True:
        try:
            input = float(string)
            return 1
        except ValueError:
            return 0

# This function is used to validate that date entered by user is valid
def validate(date_text):
    while True:
        try:
            input = datetime.datetime.strptime(date_text, '%Y-%m-%d')
            return 1
        except ValueError:
            return 0


# This function displays main menu and asks for a valid user menu input
def user_input():
    global userinput
    print("\n--- MAIN MENU ---")
    print("What would you like to do?")
    print( "1) view current balance \n2) record a debit (withdraw) \n3) record a credit (deposit)\n4) view all historical transactions\n5) exit")
    userinput = input("Your choice? ")
    while (userinput.isdigit() == False) or (int(userinput) >5 or int(userinput) < 1):
        print("\nInvalid Choice\n")
        print( "1) view current balance \n2) record a debit (withdraw) \n3) record a credit (deposit)\n4) view all historical transactions\n5) exit")
        userinput = input("\nYour choice? ")
    return userinput 


user_input()
t = datetime.datetime.now()


while userinput != '5':

    # this functions actually debits the amount from user's account. If debit transaction is higher than balance, it prevents the debit. 
    def debit(amount, debit_description):
        trans_types=[]
        trans_amounts=[]
        trans_notes = []
        trans_time =[]
        balance = 0.00
        trans_types = [x[0] for x in csv.reader(open('checkbook_v3.csv','r'), delimiter='\t')]
        trans_amounts = [x[1] for x in csv.reader(open('checkbook_v3.csv','r'), delimiter='\t')]
        trans_notes = [x[2] for x in csv.reader(open('checkbook_v3.csv','r'), delimiter='\t')]
        trans_time = [x[3] for x in csv.reader(open('checkbook_v3.csv','r'), delimiter='\t')]
        acc_balance = 0.00
        for i in range(0, len(trans_amounts)):
            acc_balance = acc_balance + float(trans_amounts[i])
            balance = balance + float(trans_amounts[i])
        acc_balance = acc_balance - amount
        if acc_balance < 0:
            print(f"\nYou do not have enough balance to withdraw ${'%.2f'%amount}")
            print(f"\nYour current balance is ${'%.2f'%balance}")
            return 'insufficent amount'
        else:
            amount = float(amount)* -1
            print(amount)
            print("I was here")
            amount = str(amount)
            debit_elements = ['debit', amount, debit_description, t ]
            print("I was here too!")
            with open("checkbook_v3.csv", 'a') as f:
                f.write("\n")
                for debit_element in debit_elements:
                    f.write(str(debit_element) + '\t')


    # This block accepts a valid user debit amount, calls 'debit' function and displays debit amount and total balance: .
    if userinput == '2':
        debit_amount_input = input("Enter the debit amount: ")
        while is_number(debit_amount_input) == 0:
            print("Invalid input!")
            debit_amount_input = input("\nEnter the debit amount: ")
        debit_description = input("Enter a description of this debit: ")
        debit_amount = float(debit_amount_input)
        output = debit(debit_amount, debit_description)
        trans_types=[]
        trans_amounts=[]
        trans_notes = []
        trans_time =[]
        if output == 'insufficent amount':
            print("\n")
        else:
            balance = 0.00
            trans_types = [x[0] for x in csv.reader(open('checkbook_v3.csv','r'), delimiter='\t')]
            trans_amounts = [x[1] for x in csv.reader(open('checkbook_v3.csv','r'), delimiter='\t')]
            trans_notes = [x[2] for x in csv.reader(open('checkbook_v3.csv','r'), delimiter='\t')]
            trans_time = [x[3] for x in csv.reader(open('checkbook_v3.csv','r'), delimiter='\t')]
            balance = 0.00
            for amount in range(0, len(trans_amounts)):
                balance = balance + float(trans_amounts[amount])
            print(f"\n Debit amount: ${debit_amount}. Your account balance is: ${'%.2f'%balance}\n")

    # this functions actually credits the amount to user's account. The credit amount is appended in the checbook.csv file.
    def credit(amount, credit_description):
        amount = str(amount)
        credit_elements = ['credit', amount, credit_description, t ]
        
        with open("checkbook_v3.csv", 'a') as f:
            f.write("\n")
            for credit_element in credit_elements:
                f.write(str(credit_element) + '\t')

    # code used when credit option is selected on main menu. # This block accepts a valid user credit amount, calls 'credit' function and displays credit amount and total balance: 
    if userinput == '3':
        credit_amount_input = input("Enter the credit amount: ")
        while is_number(credit_amount_input) == 0:
            print("\nInvalid input!")
            credit_amount_input = input("\nEnter the credit amount: ")
        credit_description = input("Enter a description of this credit: ")
        credit_amount = float(credit_amount_input)
        credit(credit_amount, credit_description)
        trans_types=[]
        trans_amounts=[]
        trans_notes = []
        trans_time =[]
        trans_types = [x[0] for x in csv.reader(open('checkbook_v3.csv','r'), delimiter='\t')]
        trans_amounts = [x[1] for x in csv.reader(open('checkbook_v3.csv','r'), delimiter='\t')]
        trans_notes = [x[2] for x in csv.reader(open('checkbook_v3.csv','r'), delimiter='\t')]
        trans_time = [x[3] for x in csv.reader(open('checkbook_v3.csv','r'), delimiter='\t')]
        balance = 0.00
        for amount in range(0, len(trans_amounts)):
            balance = balance + float(trans_amounts[amount])
        print(f"\n Credit amount: ${credit_amount}. Your account balance is: ${'%.2f'%balance}\n")


    # This function calculates and displays the user balance when called.
    def view_balance():
        trans_types=[]
        trans_amounts=[]
        trans_notes = []
        trans_time =[]
        trans_types = [x[0] for x in csv.reader(open('checkbook_v3.csv','r'), delimiter='\t')]
        trans_amounts = [x[1] for x in csv.reader(open('checkbook_v3.csv','r'), delimiter='\t')]
        trans_notes = [x[2] for x in csv.reader(open('checkbook_v3.csv','r'), delimiter='\t')]
        trans_time = [x[3] for x in csv.reader(open('checkbook_v3.csv','r'), delimiter='\t')]
        balance = 0.00
        for amount in range(0, len(trans_amounts)):
            balance = balance + float(trans_amounts[amount])
        print(f"\nYour account balance is: ${'%.2f'%balance}\n")


    if userinput == '1':
        view_balance()



# user_input1 is a  function will displays 'sub-menu' which allows user to view transactions by category.
    def user_input1():
        global userinput1
        print("\nWhat would you like to do?")
        print( "1) view all transactions \n2) view debit transactions \n3) view credit transactions \n4) Go to main menu\n")
        userinput1 = input("Your choice? ")
        while (userinput1.isdigit() == False) or (int(userinput1) >5 or int(userinput1) < 1):
            print("\nInvalid Choice\n")
            print( "1) view all transactions \n2) view debit transactions \n3) view credit transactions \n4) Go to main menu\n")
            userinput1 = input("\nYour choice? ")
        return userinput1

# the block below is code which allows user to review different transactions by category.
    #code to display sub-menu:
    if userinput == '4':
        user_input1()
        while userinput1 != '4':

            #code to display ALL transactions:
            if userinput1 == '1':
                global userinput2
                print("\nWhat would you like to do?")
                print("1) view all transactions \n2) view all transactions by date")
                userinput2 = input("Your choice? ")
                while (userinput2.isdigit() == False) or (int(userinput2) >2 or int(userinput2) < 1):
                    print("\nInvalid Choice\n")
                    print("1) view all transactions \n2) view all transactions by date")
                    userinput2 = input("\nYour choice? ")

                if userinput2 == '1':
                    with open("checkbook_v3.csv", "r") as f:
                        print("type   amount  trans_note  trans_date-time")
                        contents = (f.readlines())
                        for line in contents:
                            print(line)
                #code to display transactions by date:
                if userinput2 == '2':
                    date_input = input("Please enter a date in YYYY-MM-DD format: ")
                    validate(date_input)
                    while validate(date_input) == 0:
                        print("Invalid input!")
                        date_input = input("Please enter a date in YYYY-MM-DD format: ")
                    trans_types=[]
                    trans_amounts=[]
                    trans_notes = []
                    trans_time =[]
                    print(f"\n Your transactions on date {date_input}: \n")
                    trans_types = [x[0] for x in csv.reader(open('checkbook_v3.csv','r'), delimiter='\t') if x[3].split(' ')[0] == date_input]
                    trans_amounts = [x[1] for x in csv.reader(open('checkbook_v3.csv','r'), delimiter='\t') if x[3].split(' ')[0] == date_input]
                    trans_notes = [x[2] for x in csv.reader(open('checkbook_v3.csv','r'), delimiter='\t') if x[3].split(' ')[0] == date_input]
                    trans_time = [x[3] for x in csv.reader(open('checkbook_v3.csv','r'), delimiter='\t') if x[3].split(' ')[0] == date_input]
                    if len(trans_types) == 0:
                        print(f" --- No transactions found for {date_input} ---")
                    else:
                        t_debit_amount = 0.00
                        print("type   amount  trans_note")
                        for i in range(0, len(trans_amounts)):
                            t_debit_amount = t_debit_amount + float(trans_amounts[i])
                            print(f"{trans_types[i]}, {trans_amounts[i]}, {trans_notes[i]} ")
                    


            #code to display sub-menu DEBIT transactions only:
            if userinput1 == '2':
                global userinput3
                print("\nWhat would you like to do?")
                print("1) view all debit transactions \n2) view all debit transactions by date")
                userinput3 = input("Your choice? ")
                while (userinput3.isdigit() == False) or (int(userinput3) >2 or int(userinput3) < 1):
                    print("\nInvalid Choice\n")
                    print("1) view all debit transactions \n2) view all debit transactions by date")
                    userinput3 = input("\nYour choice? ")

                if userinput3 == '1':
                    trans_types=[]
                    trans_amounts=[]
                    trans_notes = []
                    trans_time =[]
                    print("\n Your debit transactions: \n")
                    trans_types = [x[0] for x in csv.reader(open('checkbook_v3.csv','r'), delimiter='\t') if x[0] == 'debit']
                    trans_amounts = [x[1] for x in csv.reader(open('checkbook_v3.csv','r'), delimiter='\t') if x[0] == 'debit']
                    trans_notes = [x[2] for x in csv.reader(open('checkbook_v3.csv','r'), delimiter='\t') if x[0] == 'debit']
                    trans_time = [x[3] for x in csv.reader(open('checkbook_v3.csv','r'), delimiter='\t') if x[0] == 'debit']
                    t_debit_amount = 0.00
                    print("type   amount  trans_note  trans_date-time")
                    for i in range(0, len(trans_amounts)):
                        t_debit_amount = t_debit_amount + float(trans_amounts[i])
                        print(f"{trans_types[i]}, {trans_amounts[i]}, {trans_notes[i]}, {trans_time[i]}")
                    print(f"\nTotal debit amount = ${'%.2f'%t_debit_amount}\n")
                #code to display debit transactions by date:
                if userinput3 == '2':
                    date_input = input("Please enter a date in YYYY-MM-DD format: ")
                    validate(date_input)
                    while validate(date_input) == 0:
                        print("Invalid input!")
                        date_input = input("Please enter a date in YYYY-MM-DD format: ")
                    trans_types=[]
                    trans_amounts=[]
                    trans_notes = []
                    trans_time =[]
                    print(f"\n Your transactions on date {date_input}: \n")
                    trans_types = [x[0] for x in csv.reader(open('checkbook_v3.csv','r'), delimiter='\t') if (x[3].split(' ')[0] == date_input and x[0] == 'debit')]
                    trans_amounts = [x[1] for x in csv.reader(open('checkbook_v3.csv','r'), delimiter='\t') if (x[3].split(' ')[0] == date_input and x[0] == 'debit')]
                    trans_notes = [x[2] for x in csv.reader(open('checkbook_v3.csv','r'), delimiter='\t') if (x[3].split(' ')[0] == date_input and x[0] == 'debit')]
                    trans_time = [x[3] for x in csv.reader(open('checkbook_v3.csv','r'), delimiter='\t') if (x[3].split(' ')[0] == date_input and x[0] == 'debit')]
                    t_debit_amount = 0.00
                    if len(trans_amounts) == 0:
                        print(f"--- No transactions found for {date_input} ----")
                    else:
                        print("type   amount  trans_note")
                        for i in range(0, len(trans_amounts)):
                            t_debit_amount = t_debit_amount + float(trans_amounts[i])
                            print(f"{trans_types[i]}, {trans_amounts[i]}, {trans_notes[i]} ")
    
            
            #code to display sub-menu CREDIT transactions only:
            if userinput1 == '3':
                global userinput4
                print("\nWhat would you like to do?")
                print("1) view all credit transactions \n2) view all credit transactions by date")
                userinput4 = input("Your choice? ")
                while (userinput4.isdigit() == False) or (int(userinput4) >2 or int(userinput4) < 1):
                    print("\nInvalid Choice\n")
                    print("1) view all credit transactions \n2) view all credit transactions by date")
                    userinput4 = input("\nYour choice? ")

                if userinput4 == '1':
            
                    print("\n Your credit transactions: \n")
                    trans_types=[]
                    trans_amounts=[]
                    trans_notes = []
                    trans_time =[]
                    trans_types = [x[0] for x in csv.reader(open('checkbook_v3.csv','r'), delimiter='\t') if x[0] == 'credit']
                    trans_amounts = [x[1] for x in csv.reader(open('checkbook_v3.csv','r'), delimiter='\t') if x[0] == 'credit']
                    trans_notes = [x[2] for x in csv.reader(open('checkbook_v3.csv','r'), delimiter='\t') if x[0] == 'credit']
                    trans_time = [x[3] for x in csv.reader(open('checkbook_v3.csv','r'), delimiter='\t') if x[0] == 'credit']
                    t_credit_amount = 0.00
                    print("type   amount  trans_note  trans_date-time")
                    for i in range(0, len(trans_amounts)):
                        t_credit_amount = t_credit_amount + float(trans_amounts[i])
                        print(f"{trans_types[i]}, {trans_amounts[i]}, {trans_notes[i]}, {trans_time[i]}")
                    print(f"\nTotal credit amount = ${'%.2f'%t_credit_amount}\n")
            #code to display debit transactions by date:
                if userinput4 == '2':
                    date_input = input("Please enter a date in YYYY-MM-DD format: ")
                    validate(date_input)
                    while validate(date_input) == 0:
                        print("Invalid input!")
                        date_input = input("Please enter a date in YYYY-MM-DD format: ")
                    trans_types=[]
                    trans_amounts=[]
                    trans_notes = []
                    trans_time =[]
                    print(f"\n Your transactions on date {date_input}: \n")
                    trans_types = [x[0] for x in csv.reader(open('checkbook_v3.csv','r'), delimiter='\t') if (x[3].split(' ')[0] == date_input and x[0] == 'credit')]
                    trans_amounts = [x[1] for x in csv.reader(open('checkbook_v3.csv','r'), delimiter='\t') if (x[3].split(' ')[0] == date_input and x[0] == 'credit')]
                    trans_notes = [x[2] for x in csv.reader(open('checkbook_v3.csv','r'), delimiter='\t') if (x[3].split(' ')[0] == date_input and x[0] == 'credit')]
                    trans_time = [x[3] for x in csv.reader(open('checkbook_v3.csv','r'), delimiter='\t') if (x[3].split(' ')[0] == date_input and x[0] == 'credit')]
                    t_credit_amount = 0.00
                    if len(trans_amounts) == 0:
                        print(f"--- No transactions found for {date_input} ----")
                    else:
                        print("type   amount  trans_note")
                        for i in range(0, len(trans_amounts)):
                            t_credit_amount = t_credit_amount + float(trans_amounts[i])
                            print(f"{trans_types[i]}, {trans_amounts[i]}, {trans_notes[i]} ")
            user_input1() 
        
        
        #code to return from sub-menu to main-menu:
        if userinput1 == 4:
            user_input()
    
# the user_input function below will return use to main menu options
    user_input()

# exit main menu option
    if userinput == '5':
        print(" Have a nice day!")


