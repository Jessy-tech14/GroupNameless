def main():
    print("Welcome to the Indentation Race!")
    for i in range(5):
        print("Current number:", i)
        if i % 2 == 0:
            print("Even number.")
        else:
            print("Odd number.")
print("Race completed!")
main()
    
#  Challenge 2: Total cost calculator

def calculate_total_price(item_price, quantity):
    item_total = item_price * quantity
    tax_rate = 0.07
    tax_amount = item_total * tax_rate
    total_price = item_total + tax_amount
    discount = 0.1
    discounted_price = total_price - (total_price * discount)
    return discounted_price

item_price = 25.0
quantity = 4

print("Total Price:", calculate_total_price(item_price, quantity))