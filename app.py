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

'''print('Order Management') 
print('===============') 
 
customer='Arun' 
product='Laptop' 
price=50000.00 
quantity=2 
 
total=price*quantity 
 
print('ORDER SUMMARY') 
print('-------------') 
print('Final bill',total) 
 
 
Theory : 
-======= 
 
customer --> variable name --> Arun 
product --> variable name --> laptop 
 
variablename='value1' 
 
str --> text(a-z, A-Z, Specia; characters) 
 
price --> variablename--> 50000 
 
int --> stores numerical related data (0-9) 
 
float --> decimal  
''' 
''' 
print('Order Management') 
print('===============') 
 

syntax for input 
variablename=input('') 
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
 
 
''' 
'''prompt 
 
 var=input('Enter the value')
print () 
 
 
print('Enter the value') 
customer=input() 
 

user --> wait''' 
 

'''typeof -- print(type(customer)) 
 

print(type(customer)) 
print(type(quantity)) 
print(type(price))''' 
 

#Operators ==>  
''' 
value 1 
 
value 2 
 

1. Arithmetic Operators  
addition --> + 
subtraction --> - 
multiplication --> * 
division --> / 
modulo division --> // 
''' 
 
a=10 
b=20 
a=30 
print('basic calculator') 
print('----------------') 
 
print('Addition Operator') 
print(a+b) 
 
print('Subtraction Operator') 
print(a-b) 
 
print('Multiplication Operator') 
print(a*b) 
 
print('Division Operator') 
print(a/b) 
 
print('Floor Division Operator') 
print(a//b) 
 
print('Power Operator') 
print(a**b) 
 

#2. Assignment Operators: = 
 
'''
1. a=10, 
a+=10 
 

a-=10 
 
 

Comparison Operators 
a==10 
 

Logical Operator --> AND, OR, NOT, XOR 
 
 

2. Assignment Operator --> used to assign/update 
 
price=50000 
 

= --> Assignment Oper 
 
''' 
Value 50000 --> Assign to --> price 
 
variable=value 
 
amount=1000 
 
amount=amount+500 
amount+=500''' 
 
amount=1000 
 

amount=amount+500 
amount+=500 
print("Updated : ",amount) 
 
 
amount=1000 
amount-=500 
print('Minus',amount) 
 

amount=amount-500 
 
'''= --> assign 
+= --> Add and Assign 
-= --> Subtract and Assign 
 
TASK --> 
*= --> Multiply and Division 
/= --> Divide and Assign''' 
 
 

3. Comparison Operator --> two or more values, return either TRUE, False 
print('Comparison') 
print(10>5) 
print(10<5) 
 
 
 

value1 comoperator value2 
 
''' 
>  
< 
>= 
<= 

=
==''' 
 
a=10 
b=20 
 
 
print('COMPARSION OPERATOR') 
print('===================') 

False 
print(a>b)  

True 
print(a<b) 

False 
print(a==b) 

True 
print(a!=b) 

True 
print(b!=a) 
 

= --> update, assign == --> check/compare  
 
 
'''if --> keyword 
 
condition  -- a>b 
 
: --> beginning of block 
 
print(true) 
if condition: 
    print('A is greater than B') 
else (condition2): 
    print('b is gretaer than A') 
 
if condition: 
    print() 
     
a=10 
b=20 
print('Conditional using IF ELSE') 
if a>b: 
    print('A is Greater than B') 
else: 
    print('False') 
 
number=50 
if number>10: 
    print('True') 
else: 
    print('False') 
 

TASK --> /= --> Divide and Assign' 
TASK --> *= --> Multiply and Division   
Basic Calculator (Arithmetic Operator)