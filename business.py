customer = input("Enter Customer Name :")
product = input("Enter Product Name :")
price = float(input("Enter Price :"))
quantity = int(input("Enter Quantity :"))
total = price * quantity

print("your order")
print("============")
print("Customer Name :", customer)
print("Product Details :", product)
print("Price :", price)
print("Quantity :", quantity)
print("Final Bill :", total)