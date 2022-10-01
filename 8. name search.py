'''
If you have downloaded the source code 
you will find the following files in the Chapter 07 folder:
•	 GirlNames.txt This file contains a list 
of the 200 most popular names given to girls 
born in the United States from the year 2000 through 2009.
•	 BoyNames.txt This file contains a list o
f the 200 most popular names given to boys 
born in the United States from the year 2000 through 2009
Write a program that reads the contents of the two files into two separate lists. 
The user should be able to enter a boy’s name, a girl’s name, or both, and the application will display 
messages indicating whether the names were among the most popular.
(You can access the Premium Companion Website at www.pearsonglobaleditions.com/gaddis.
'''
girl_names_file=open("8. GirlNames.txt",'r')
girls_list=girl_names_file.read()
girls_list=girls_list.split("\n")
girl_names_file.close()

boy_names_file=open("8. BoyNames.txt",'r')
boys_list=boy_names_file.read()
boys_list=boys_list.split("\n")
boy_names_file.close()

print("Enter list of names: ")
names=list(input().split())
for i in range(len(names)):
    names[i]=names[i].title() #capitaizes each word
    if names[i] in girls_list:
        print(names[i],"is one of the most popular girl's name")
    elif names[i] in boys_list:
        print(names[i],"is one of the most popular boy's name")
    else:
        print(names[i],"is not among most popular names of girls and boys")
    
    


