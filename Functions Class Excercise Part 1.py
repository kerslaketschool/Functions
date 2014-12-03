# functions improvement exercise
# times-table tester

import random

def timesTable():
    print("Times-table tester")
    print()
    testTable = input("Which times-table do you want to be tested on? ")
    testTable = int(testTable)
    return testTable

def questionComplete(testTable):
    for questions in range(1,6):
        userAns, Ans2 = question(testTable)
        displayCorrect(userAns, Ans2)
        
def question(testTable):
    Num1 = testTable
    Num2 = random.randrange(2,13)
    Ans = Num1 * Num2
    UserAnswer = input(str(Num1) + ' x ' + str(Num2) + ' = ? ')
    UserAnswer = int(UserAnswer)
    return UserAnswer, Ans
    
def displayCorrect(UserAnswer,Ans):
     if UserAnswer == Ans:
        print('Well done, you got the correct answer!')
        print()
     else:
        print('Sorry, you got the answer wrong. The correct answer is',Ans)
        print()
              
def timesTableTester():
    tableTest = timesTable()
    questionComplete(tableTest)

#main program
timesTableTester()
    


    

