'''
Problem Statement:
Design a program that asks the user to enter a series of 20 numbers.
 The program should store the numbers in a list 
 then display the following data: 
• The lowest number in the list 
• The highest number in the list 
• The total of the numbers in the list 
• The average of the numbers in the list

'''
print("Enter Series of 20 Numbers: ")
arr=[]
for i in range(20):
    arr.append(int(input()))
lowest=min(arr)
highest=max(arr)
total=sum(arr)
average=total/20
print("the lowest number is: ",lowest)
print("the highest number is: ",highest)
print("the total of all numbers: ",total)
print("the average of all numbers: ",average)
