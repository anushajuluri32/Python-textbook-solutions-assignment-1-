'''
If you have downloaded the source code 
you will find a file named WorldSeriesWinners.txt in the Chapter 07 folder. 
This file contains a chronological list of the 
World Series winning teams from 1903 through 2009. 
(The first line in the file is the name of the team that 
won in 1903, and the last line is the name of the team that won in 2009.
 Note the World Series was not played in 1904 or 1994.)
Write a program that lets the user enter the name of a team, then displays the number of 
times that team has won the World Series in the time period from 1903 through 2009.
TIP: Read the contents of the WorldSeriesWinners.txt file into a list. When the 
user enters the name of a team, the program should step through the list, counting the 
number of times the selected team appears
'''
file1=open("10. WorldSeriesWinners.txt",'r')
winners_list=file1.read()
winners_list=list(winners_list.split('\n'))
file1.close()

name_of_team=input("Enter the name of team: ")
name_of_team=name_of_team.title()
no_of_times=winners_list.count(name_of_team)

if no_of_times>0:
    years=[]
    j=0
    for i in range(1903,2009):
        if i==1904 or i==1994:
            continue
        else:
            if name_of_team==winners_list[j]:
                years.append(i)
            j=j+1
    print(name_of_team,"won",no_of_times,"times","in years",end=" ")
    print(*years)
else:
    print(name_of_team,"has never won match / Invalid Input")



        
        
         
