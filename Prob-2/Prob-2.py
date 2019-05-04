# Module 3
#   Programming Assignment 4
#     Prob-2.py

# Jonathan Ciarlo

'''
Your IPO comment goes here
#inputs: persons name, persons hourly wage, persons hours
#process: assign variables (name, wage, hours), print out that information with the assigned parameters i.e. overtime = wages times 1.5 if hours over 40
#outputs: name, reg wages, ovetime wages, total wages, tax withholding, Insurance withholding, take home pay




'''

def main():
    # your code goes here
    import math
   #Inputs
    
    #variables
    name = input("Enter a name: ")
    print("---------------------------")
    wage = eval(input("Enter a wage: "))
    print("---------------------------")
    hours = eval(input("Enter hours: "))
    print("---------------------------")
    #equations for information inputed
    overtimehours = hours - 40
    if overtimehours < 0:
        overtimehours = 0
    regularwage = hours * wage
    overtimewage = (wage * 1.5) * overtimehours
    tax = (regularwage + overtimewage) * 0.20
    medical = (regularwage + overtimewage) * .10
    print()
    print()
    #printing out all above equations
    print("Name: \t\t\t", name)
    print()
    print("Hours: \t\t\t", hours)
    print()
    print("Wage: \t\t\t", wage)
    print()
    print("Regular Wages: \t\t", regularwage )
    print()
    print("Overtime Wages: \t", overtimewage)
    print()
    print("Total Wages: \t\t", regularwage + overtimewage)
    print()
    print("Tax Withholding: \t", tax)
    print()
    print("Medical Withholding: \t", medical)
    print()
    print("Take Home Pay: \t\t", (regularwage + overtimewage) - (tax + medical))  
    #print("Take Home:", take home )
   


main()