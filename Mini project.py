# Basic ATM Management System 
while True:
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
present = 0
absent = 0
for i in range(1,n+1):
    s = input(f"Student {i} (p/a) : ")
    if s == "p":
        present += 1
        i += 1
    else:
        absent += 1
        i += 1
print("Total students : ",n)
print("Total presenties : ",present)
print("Total absenties : ",absent)

#BMI Calculator
while True:
    height = float(input("Enter the height: "))
    weight = float(input("Enter the weight: "))
    bmi = weight/(height)**2
    print("bmi : ",bmi)
    if bmi <= 18.5:
        print("Under weight")
    elif bmi > 18.5 and bmi <= 24.5:
        print("Healthy weight")
    elif bmi > 24.5 and bmi <= 29.5:
        print("Over weight")
    else:
        print("obesity")        
        























    
        
