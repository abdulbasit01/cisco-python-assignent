#question 1
def question1():
    totalSubjects=5
    inittial=1
    totalMarks=0
    while(totalSubjects!=0):
        inputU=input("enter marks of subject\n")
        totalMarks+=float(inputU)
        totalMarks=totalMarks
        print(totalMarks)
        totalSubjects-=1
    totalMarks=(totalMarks/5)
    
    print(totalMarks)
    if (totalMarks <100 and totalMarks>79):
        print("Gradre A+", totalMarks)
    elif (totalMarks <80 and totalMarks>69):
        print("Gradre A", totalMarks)
    elif (totalMarks <70 and totalMarks>59):
        print("Gradre B", totalMarks)
    elif (totalMarks <60 and totalMarks>49):
        print("Gradre C", totalMarks)
    elif (totalMarks <50 and totalMarks>39):
        print("Gradre C", totalMarks)
    else:
        print("you Are fail", totalMarks)
def question2():
    inputNumber=input("Enter number\n")
    if (int(inputNumber)%2==0):
        print("number is even", inputNumber)
    else:
        print("number is odd", inputNumber)
def question3():
    listA=[1,2,3,4,5,6,7,8]
    print(len(listA))
def question4():
    givenList=[1,2,3,"a","b",3,5,6,"hello"]
    initialSum=0
    for i in givenList: 
        if (type(i)!=str):
            initialSum+=i
    print("the total summ of numeric number in the given list is" ,+ initialSum)
def question5():
    listA=[1,5,6,3,2,7,8,-100]
    listA.sort(reverse=True)
    print("The maximun number in the given list is " , listA[0]) 
def question6():
    a=[1,1,2,3,5,8,13,21,34,55,89]
    for i in a :
        if (i<5):
            print(i)

while True:
    questions=input("Which Question You Want to Check \n")
    if(questions==1):
        question1()
        continue
    elif(questions==2):
        question2()
        continue
    elif(questions==3):
        question3()
        continue
    elif(questions==4):
        question4()
        continue
    elif(questions==5):
        question5()
        continue
    elif(questions==6):
        question6()
        continue
    else:
        continue



