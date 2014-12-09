#Toby Kerslake
#02-12-14
#Functions Revision Exercise 1


def outputSymbols(Integer,CharSym):
    print(Integer * CharSym)

def integer():
    integer = int(input("Enter an integer:"))
    return integer

def characterSymbol():
    charSym = input("Please enter a character symbol")
    return charSym

def mainProgram():
    Integer = integer()
    CharSym = characterSymbol()
    outputSymbols(Integer,CharSym)
    
#main program
mainProgram()
