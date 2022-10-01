'''
 Population Data
If you have downloaded the source code 
you will find a file named USPopulation.txt in the Chapter 07 folder.
 The file contains the midyear population of the United States, 
 in thousands, during the years 1950 through 1990. 
 The first line in the file contains the population for 1950, 
 the second line contains the population for 1951, and so forth.
Write a program that reads the file’s contents into a list.
 The program should display the following data:
• The average annual change in population during the time period
• The year with the greatest increase in population during the time period
• The year with the smallest increase in population during the time period
'''
file1=open("9. USPopulation.txt",'r')
population_list=file1.read()
population_list=list(map(int,population_list.split('\n')))
file1.close()

start_year=1950
annual_changes_list=[]
for i in range(0,len(population_list)-1):
    annual_change=population_list[i+1]-population_list[i]
    annual_changes_list.append(annual_change)

average_change=sum(annual_changes_list)/len(annual_changes_list)
greatest_increase=max(annual_changes_list)
gi_index=annual_changes_list.index(greatest_increase) 
smallest_increase=min(annual_changes_list)
si_index=annual_changes_list.index(smallest_increase)

print("The average annual change in population from 1950 to 1990 is",average_change)
print("The year with the greatest increase in population is from",gi_index+1950,"to",gi_index+1951)
print("The year with the smallest increase in population is from",\
    si_index+1950,"to",si_index+1951)

    



