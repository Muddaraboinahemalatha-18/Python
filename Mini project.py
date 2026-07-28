'''while True:
    Account = 100000
    card = input("Enter the card : ")
    if card == "c":
        print("Welcome Hemalatha")
    else:
        print("Invalid card")
        pwd = int(input("Enter the Password : "))
        if pwd == 1234:
            options = input("Options : ")
            if options == "Balance Enq":
                print("Account balance is : ",Account)
            elif options == "Withdraw":
                money = int(input("Enter the amount : "))
                print("Remaining account balance is : ",Account - money)
            else:
                print("Invalid option")
        else:
            print("Incorrect password")'''


# Basic ATM Management System 
'''while True:
    amount = 100000
    card = input("Insert the card:")
    if card == "c":
        print("Welcome Hemalatha")
        pwd = input("Enter the password:")
        if pwd == "12345":
            option = int(input("Enter your option: 1. Balance enquiry 2. Withdraw : "))
            if option == 1:
                print("Balance enquiry:",amount)
            elif option == 2:
                money = int(input("Enter the amount:"))
                print(money)
                balance = amount - money
                print("Remaining account balance is:", balance)
            else:
                print("Invalid option")
        else:
            print("Incorrect password")
    else:
        print("Invalid card")'''

#Attendence Report
n = int(input("No of Students: "))
c1 = 0
c2 = 0
for i in range(1,n+1):
    s = input(f"Student {i} (p/a) : ")
    if s == "p":
        c1 += 1
        i += 1
    else:
        c2 += 1
        i += 1
print("Total students : ",n)
print("Total presenties : ",c1)
print("Total absenties : ",c2)

        
        























    
        
