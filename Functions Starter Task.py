#Toby Kerslake
#13-11-2014
#Functions Starter Task

def calculatePay ():
    hours,pay = inputHoursAndPay()
    totalPay = calculateTotalPay(hours,pay)
    displayTotalPay(totalPay)

def calculateBasicPay(hours,pay):
    total = hours * pay
    return total

def calculateOvertimePay(hours,pay):
    total = ((hours - 40) * (pay * 1.5)) + (pay * 40)
    return total

def calculateTotalPay(hours,pay):
    if hours > 40:
        total = calculateOvertimePay(hours,pay)
    else:
        total = calculateBasicPay(hours,pay)
    return total

def inputHoursAndPay():
    workHours = int(input("Enter the amount of hours you have worked: "))
    workPay = float(input("Enter your pay rate: £"))
    return workHours,workPay

def displayTotalPay(total):
    print("Your total is £{0}".format(total))
    

#main program
calculatePay()

