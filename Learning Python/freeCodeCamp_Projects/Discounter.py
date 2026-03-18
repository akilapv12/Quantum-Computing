# Discounter

price = input("Original price: ")  # Input is not directly taken as float so that program
discount = input("Discount%: ") #    does not crash due to ValueError.

def apply_discount(price, discount):
    try:                               # Try/Except lets us change the code but keep running
        price = float(price) #           if any error occurs by running 'except code' 
        discount = float(discount)  # input is str by default, converted to float to carry out function.
    except ValueError:
        print("Both price and discount should be numbers.")
        return # Ends the function if ValueError after printing message
    if price<=0:
        print("The price should be more than 0.")
    elif discount<0 or discount>100:
        print("The discount% should be between 0 and 100.")
    else:
        discounted_value = price - (price * (discount/100))
        print(f"Discounted value: {discounted_value}")

apply_discount(price, discount)