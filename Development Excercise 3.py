#Toby Kerslake
#07-12-2014
#Development Excercise 3

def CurrencyConverter():
    _convertFrom, _convertTo, _convertQuantity = UserInput()
    WhichConversion(_convertFrom, _convertTo, _convertQuantity)
    _conversion = ConvertToPounds(_convertFrom,_convertQuantity)
    _conversion = ConvertToDollars(_convertFrom,_convertQuantity)
    _conversion = ConvertToEuros(_convertFrom,_convertQuantity)
    DisplayConversion(_convertTo, _conversion)

def UserInput():
    convertFrom = input("Which currency do you want to convert from(£,€,$):")
    convertTo = input("Which currency do you want to convert to(£,€,$):")
    convertQuantity = float(input("How many {0} do you want to convert into {1}:".format(convertFrom, convertTo)))
    return convertFrom, convertTo, convertQuantity

def WhichConversion(convertFrom, convertTo, convertQuantity):
    if convertTo == "£":
        ConvertToPounds(convertFrom,convertQuantity)
    elif convertTo == "$":
        ConvertToDollars(convertFrom,convertQuantity)
    else:
        ConvertToEuros(convertFrom,convertQuantity)

def ConvertToPounds(convertFrom,convertQuantity):
    if convertFrom == "€":
        conversion = convertQuantity * 0.814
    elif convertFrom == "$":
        conversion = convertQuantity * 0.625
    else:
        conversion = convertQuantity
    return conversion
        
def ConvertToDollars(convertFrom,convertQuantity):
    if convertFrom == "£":
        conversion = convertQuantity * 1.601
    elif convertFrom == "€":
        conversion = convertQuantity * 1.302
    else:
        conversion = convertQuantity
    return conversion

def ConvertToEuros(convertFrom,convertQuantity):
    if convertFrom == "£":
        conversion = convertQuantity * 1.229
    elif convertFrom == "$":
        conversion = convertQuantity *0.768
    else:
        conversion = convertQuantity
    return conversion

def DisplayConversion(convertTo,conversion):
    print(convertTo,conversion)



#Main Program
CurrencyConverter()

