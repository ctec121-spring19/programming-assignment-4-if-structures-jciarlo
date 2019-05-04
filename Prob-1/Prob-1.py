# Module 3
#   Programming Assignment 4
#     Prob-1.py

# Jonathan Ciarlo

def shippingCost(orderSubTotal):
    shippingCost = 2.99
    # enter code here to test for free
    if orderSubTotal >= 10.00:
        shippingCost = 0.00

    return shippingCost

def unitTest():
    print("Expected value: 2.99 - Shipping cost if subtotal < 10.00:\t", shippingCost(5.99))
    # enter additional test code here
    print("Expected value: 0.0 - Shiping cost if subtotal > 10.00:\t", shippingCost(11.00))
    print("Expected value: 0.0 - Shipping cost if subtotal = 10.00:\t", shippingCost(10.00))

if __name__ == "__main__":
    unitTest()