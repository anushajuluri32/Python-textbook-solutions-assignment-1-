'''
In a program, write a function named roll 
that accepts an integer argument number_of_throws. 
The function should generate and return 
a sorted list of number_of_throws random numbers between 1 and 6. 
The program should prompt the user to enter a positive integer 
that is sent to the function, and then print the returned list
'''
import random

def checkvalid(n):
    for i in range(len(n)):
        if n[i]<"0" or n[i]>"9":
            return 0
    return 1

def roll(no_of_throws):
    result=[]
    for i in range(no_of_throws):
        face_value=random.randint(1,6)
        result.append(face_value)
    result.sort()
    return result

number_of_throws=input("Enter no of throws you want to roll a die (Note: Enter only positive integers): ")
while(True):
    if checkvalid(number_of_throws)==0:
        print("You have a entered a invalid number")
        print("Please enter a valid input")
        number_of_throws=input("Enter no of throws you want to roll a die (Note: Enter only positive integers): ")
    else:
        number_of_throws=int(number_of_throws)
        break

rolled_values=roll(number_of_throws)
print(*rolled_values)

