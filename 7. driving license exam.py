'''
The local driver’s license office has asked you to create an application
 that grades the written portion of the driver’s license exam.
  The exam has 20 multiple-choice questions. Here 
are the correct answers:
1. A 
2. C
3. A
4. A
5. D
6. B
7. C
8. A
9. C
10. B
11. A
12. D
13. C
14. A
15. D
16. C
17. B
18. B
19. D
20. A
Your program should store these correct answers in a list.
 The program should read the student’s answers 
 for each of the 20 questions from a text file and 
 store the answers in another list. 
 (Create your own text file to test the application.)
  After the student’s answers 
have been read from the file, the program should display a
 message indicating whether the 
student passed or failed the exam. 
(A student must correctly answer 15 of the 20 questions to pass the exam.)
 It should then display the total number of correctly answered questions, 
the total number of incorrectly answered questions, 
and a list showing the question numbers of the incorrectly answered question
'''
file1=open("7. driving licence exam mcqs.txt",'r')
print(file1.read())
file1.close()

print("Enter your answers ")
print("Options lie in [A,B,C,D]")
student_answers=[]
key='ACAADBCACBADCADCBBDA'
wrongly_answeres_qns=[]
no_of_crct_answers=0
for i in range(20):
    while(1):
        print(i+1,end=". ")
        ans=input()
        if ans=='A' or ans=='B' or ans=='C' or ans=='D':
            break
        else:
            print("Enter valid option (Note:Correct Option is one of A,B.C and D)")
    student_answers.append(ans)
    if ans==key[i]:
        no_of_crct_answers+=1
    else:
        wrongly_answeres_qns.append(i+1)
print("You have Scored",no_of_crct_answers,"marks")
if no_of_crct_answers>=15:
    print("You have passed this exam")
else:
    print("You have failed in this exam")
if no_of_crct_answers!=20:
    print("You answers are incorrect for following questions: ")
    print(*wrongly_answeres_qns)



    
