#Toby Kerslake
#02-12-14
#Functions Class Excercise Part 2

def getInformation():
    firstName = input("Please enter your first name:")
    lastName = input("Please enter your last name:")
    gender = input("Please enter your gender (M or F):")
    houseNumber = input("Please enter your house number or name:")
    streetName = input("Please enter your street name:")
    town = input("Please enter your town:")
    postCode = input("Please enter your post code:")
    return firstName, lastName, gender

def calculateTitle(gender):
    if gender == "M" or "m":
        title = "Mr"
    elif gender == "F" or "f":
        title = "Ms"
    return title

def displayInformation(title,firstName,lastName):
    print("Thank you {0} {1} {2}".format(title,firstName,lastName))
       

    

#main program
firstName,lastName,gender = getInformation()
title = calculateTitle(gender)
displayInformation(title,firstName,lastName)

        
        
    
