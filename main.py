class Item:

    pay_rate = 0.8  # The pay rate after 20% discount (global class attribute)

    def __init__(self, name: str, price: float, quantity: int):
        # Run validations to the received arguments
        assert price >= 0, f"Price {price} is not greater than or equal to 0!"
        assert quantity >= 0, f"Quantity {quantity} is not greater than or equal to 0!"


        # Assign to self objct
        self.name = name
        self.price = price
        self.quantity = quantity

    def calculate_total_price(self):
        return self.price * self.quantity
    

item1 = Item("Phone", 100, 5)
print("name:", item1.name)
print("price:", item1.price)
print("quantity:", item1.quantity)
print("total price:", item1.calculate_total_price())

# try to find attribute at instance level, and not found
# then try to find it at class level
print(item1.pay_rate)

print()