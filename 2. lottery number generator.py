'''
Problem Statement:
Design a program that generates a seven-digit lottery number.
 The program should generate seven random numbers, 
 each in the range of 0 through 9, 
 and assign each number to a list element. 
 (Random numbers were discussed in Chapter 5.) 
 Then write another loop that displays the contents of the list.
'''
import random
#randint(m,n) will generate integers from m to n
lottery_number=""
for i in range(7):
    ith_digit=random.randint(0,9)
    lottery_number+=str(ith_digit)
print("Generated 7 digit Lotter Number is: ",lottery_number)
