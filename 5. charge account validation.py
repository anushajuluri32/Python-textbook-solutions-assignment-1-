'''
Problem Statement
If you have downloaded the source code from the Premium Companion Website
you will find a file named charge_accounts.txt in the Chapter 07 folder.
This file has a list of a company's valid charge account numbers.
Each account number is a seven-digit number, such as 5658845. 
Write a program that reads the contents of the file into a list.
The program should then ask the user to enter a charge account number. 
The program should determine whether the number is 
valid by searching for it in the list. 
If the number is in the list, the program should 
display a message indicating the number is valid. 
If the number is not in the list, 
the program should display a message indicating the number is invalid. 
(You can access the Premium Companion Website at www.pearsonglobaleditions.com/gaddis.)
'''

'''
charge account numbers list:
[5658845, 4520125, 7895122, 8777541, 8451277, 1302850, 
8080152, 4562555, 5552012, 5050552, 7825877, 1250255, 
1005231, 6545231, 3852085, 7576651, 7881200, 4581002]
'''

file1=open("5. charge_accounts.txt",'r')
valid_charge_accounts=file1.readlines()
valid_charge_accounts=list(map(int,valid_charge_accounts))
file1.close()

while(1):
    charge_account_input=input("Enter a charge account number: ")
    if charge_account_input.isnumeric() and len(charge_account_input)==7:
        break
    else:
        print("Invalid Input")
        print("Please enter correct input")
if int(charge_account_input) in valid_charge_accounts:
    print("Account number is Valid")
else:
    print("Account number is Invalid")

