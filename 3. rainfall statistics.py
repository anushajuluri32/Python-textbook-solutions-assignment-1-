'''
Problem Statement:
Design a program that lets the user enter the total rainfall 
for each of 12 months into a list. 
The program should calculate and display 
the total rainfall for the year, 
the average monthly rainfall, 
the months with the highest and lowest amounts.
'''
rainfall=[]
months=['January','February','March','April','May',\
    'June','July','August','September',\
        'October','November','December']

print("Enter rainfall in mms")
for i in range(12):
    print("Enter rainfall measure in",months[i],end=": ")
    level=int(input())
    rainfall.append(level)

#the total annual rainfall = sum of rainfall in all twelve months
total=sum(rainfall)

#the average monthly rainfall = the total annual rainfall / 12
average=total/12

#the month with the highest rainfall
highest_rainfall=rainfall[0]
highest_rainfall_month=months[0]
for i in range(1,12):
    if rainfall[i]>highest_rainfall:
        highest_rainfall=rainfall[i]
        highest_rainfall_month=months[i]

#the month with lowest rainfall
lowest_rainfall=rainfall[0]
lowest_rainfall_month=months[0]
for i in range(1,12):
    if rainfall[i]<lowest_rainfall:
        lowest_rainfall=rainfall[i]
        lowest_rainfall_month=months[0]

print("The total annual rainfall: ",total,"mm")
print("The average monthly rainfall: ",round(average,2),"mm")
print("The month with highest rainfall: "\
    ,highest_rainfall_month,"with",highest_rainfall,"mm")
print("The month with lowest rainfall: "\
    ,lowest_rainfall_month,"with",lowest_rainfall,"mm")
