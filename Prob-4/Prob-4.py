# Module 3
#   Programming Assignment 4
#     Prob-4.py

# Jonathan Ciarlo

# Author: Bruce Elgort
# Date: July 12, 2017

"""
The Elgorte coffee shop sells coffee at $16.50 a pound
plus the cost of shipping. Each order ships for $0.76
per pound plus $1.25 fixed cost for overhead. If the
number of pounds of the coffee order exceeds 10, then
the shipping cost is waived. Write a program that
calculates the cost of an order. Name your function
coffeeProcessor()
"""
#Added quotation to line 27
#Added a second parenthesis to line 27
#Add colon to line 35 after else
#Add quotation to line 43 after, "The cost of the order is:"
#Line 24 add go before coffeeProessor
#Change Evaluate to eval line 32
#line 42 change quntity to quantity 
def gocoffeeProcessor():

    # define variables
    overHead = 1.25
    priceOfCoffee = 16.50

    # get number of pounds from user
    quantity = eval(input("How many pounds of coffee would you like to order?"))
    
    # Check number of pounds ordered
    # If less than or equal to 10 pounds we must charge for shipping
    if quantity <= 10:
        shippingPerPound = .76
    else:
        shippingPerPound = 0      

    # Calculate cost of order
    costOfOrder = (quantity * priceOfCoffee) + (quantity * shippingPerPound) + overHead

    # Print result
    print("The cost of the order is:",costOfOrder)

# start the program
gocoffeeProcessor()