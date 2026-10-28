# #sample.py --> Python script --> Execute


# '''
# Order Managment --> Customers, Products, Billing calculation, Payment Summary, GST Bill, Chat bot

# Seprate --> Project FOlder/Structure


# 1. Order Management
# 2. enTRY pOINT --> APP.PY --> start (printing function) (Output)

# --> ORder Managent
# ===================
# Customer Name :A,B,C
# Products :
# Quantity :
# Final Bill :


# 3.Services --> folder
# businee.py
# products.py
# calculation.py

# (Business logical --> customer info, Billing calculation)

# 4. models :
# products 

# class Products

# Class Customet

# 5. test :

# checking

# 6. requirements.txt
# pip install pandas,
# pip install numpy,
# pip install request




# PROJECT STRUCTURE :
# ==================
# ordermanagement/
# --> app.py
# --> services/
# --> models/
# --> tests/
# --> requirements.txt
# '''

# ORDER MANAGEMENT
# ================

# Enter the Customer Name :
# Enter Product Details :
# Enter Price :
# ENter Quantity :


# YOUR ORDER
# ==========

# Customer Name :
# Product Details :
# Price :
# Quantity :
# Total :

# TASK : Create Project folder -->
# maintain app.py --> custom/user input
# '''print('Order Management')
# print('===============')

# customer='Arun'
# product='Laptop'
# price=50000.00
# quantity=2

# total=price*quantity

# print('ORDER SUMMARY')
# print('-------------')
# print('Final bill',total)


# Theory :
# -=======

# customer --> variable name --> Arun
# product --> variable name --> laptop

# variablename='value1'

# str --> text(a-z, A-Z, Specia; characters)

# price --> variablename--> 50000

# int --> stores numerical related data (0-9)

# float --> decimal 
# '''

# print('Order Management')
# print('===============')

# #syntax for input
#variablename=input('')
customer=input("Enter Customer Name :")
product=input("Enter Product Name :")
price=float(input("Enter Price:"))
quantity=int(input('Enter Quantity :'))

total=price*quantity

print('\n YOUR ORDER')
print('==========')
print("Customer Name :",customer)
print("Product Details :",product)
print("Price:", price)
print("Quantity :", quantity)
print("FInal Bill:",total)