#Toby Kerslake
#07-12-2014
#Developemnt Excercise 2

def GetInputFromUser():
    number = int(input("Please enter an odd number"))
    return number



def ValidateOdd(number):
    validate = number % 2
    if validate == 0:
        print("That's Not An Odd Number")
    else:
        DisplayDiamond(number)



def DisplayDiamond(number):
    base = 1
    n = number
    while base < number:
        basenumber = base * "*"
        print("{0:^{1}}".format(basenumber,n))
        base += 2
    while number > 0:
        number2 = number * "*"
        print("{0:^{1}}".format(number2,n))
        number = number - 2



def ShineBrightLikeADiamond():
    Number = GetInputFromUser()
    ValidateOdd(Number)

#Main Program
ShineBrightLikeADiamond()
