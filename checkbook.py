

print("~~~ Welcome to your terminal checkbook! ~~~")




def user_input():
    global userinput
    print("What would you like to do?")
    print( "1) view current balance \n2) record a debit (withdraw) '\n3) record a credit (deposit)\n4) exit")
    userinput = input("Your choice? ")
    while (userinput.isdigit() == False) or (int(userinput) >=5 or int(userinput) < 1):
        print("\nInvalid Choice\n")
        print( "1) view current balance \n2) record a debit (withdraw) '\n3) record a credit (deposit)\n4) exit")
        userinput = input("\nYour choice? ")
    return userinput 

user_input()
entry = ['0.00', '0.00', '100.00']
# with open("checkbook.txt", "w") as f:
#     for entry in first_entry:
#         f.writelines(entry +"\t")
        
# with open("checkbook.txt", "r") as f:
#     contents = (f.readlines()[-1])
    
while userinput != '4':
    def debit(amount):
        with open("checkbook.txt", "r") as f:
            contents = (f.readlines())
            balance = float((contents[-1].split("\t", 3)[2]))

        entry[2] = balance - amount
        entry[2] = str(entry[2])
        entry[1] = str(amount)
        e = entry[0]
        with open("checkbook.txt", 'a') as f:
            f.write("\n")
            for e in entry:
                f.writelines(e +"\t")

    if userinput == '2':
        debit_amount_input = input("Enter the debit amount: ")
        debit_amount = float(debit_amount_input)
        debit(debit_amount)
        balance = float(entry[2])
        print(f"\n Debit amount: ${debit_amount}. Your account balance is: ${'%.2f'%balance}\n")


    def credit(amount):
        with open("checkbook.txt", 'r') as f:
            contents = f.readlines()
            balance = float(contents[-1].split("\t", 3)[2])
        entry[2] = balance + amount
        entry[2] = str(entry[2])
        entry[0] = str(amount)
        with open("checkbook.txt", 'a') as f:
            f.write("\n")
            for e in entry:
                f.writelines(e +"\t")            

    if userinput == '3':
        credit_amount_input = input("Enter the credit amount: ")
        credit_amount = float(credit_amount_input)
        credit(credit_amount)
        balance = float(entry[2])
        print(f"\n Credit amount: ${credit_amount}. Your account balance is: ${'%.2f'%balance}\n")


    def view_balance():

        with open("checkbook.txt", "r") as f:
            contents = (f.readlines())
            balance = float((contents[-1].split("\t", 3)[2]))
            print(f"\nYour account balance is: ${'%.2f'%balance}\n")


    if userinput == '1':
        view_balance()

    user_input()
    
if userinput == '4':
    print(" Have a nice day!")


