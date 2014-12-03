#Toby Kerslake
#02-12-14
#Functions Revision Exercise 1

def outputSymbols(integer,charSym):
    for count in integer:
        print(charSym)

def integer():
    integer = int(input("Enter an integer:"))
    return integer

def characterSymbol():
    charSym = input("Please enter a character symbol")
    return charSym
    
#main program
intgeger = integer()
charSym = characterSymbol()
outputSymbols(integer,charSym)
