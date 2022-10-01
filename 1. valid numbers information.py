'''
Problem Statement: 
Design a program that uses a loop to build a 
list named valid_numbers that contains only
the numbers between 0 and 100 from the numbers
list below. The program should then determine
and display the total and average of the values
in the valid_numbers list. 
numbers = [74, 19, 105, 20, −2, 67, 77, 124, −45, 38]
'''
import math
numbers=[74,19,105,20,-2,67,77,124,-45,30]
print("List of Numbers:",*numbers)
valid_numbers=[]    #output list
# Traverse 'numbers' list
# if any element is in between 0 to 100, \
# add that element into 'valid_numbers' list
for i in range(len(numbers)):
    if numbers[i]>=0 and numbers[i]<=100:
        valid_numbers.append(numbers[i])
#computing total of all valid numbers 
total=sum(valid_numbers)
#computing average of all valid numbers 
average=sum(valid_numbers)/len(valid_numbers)
#display output
print("List of valid numbers:",*valid_numbers)
print("Total of all valid numbers:",total)
print("Average of all valid numbers:",round(average,4))













