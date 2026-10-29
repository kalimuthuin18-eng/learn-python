'''customer = input("Enter Customer Name :")
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

a=10 
b=20

if a>b:
    print("a is greater than b")
else:
    print("b is greater than a")'''

'''TASK --> 
*= --> Multiply and Division 
/= --> Divide and Assign''' 
 

'''amount = 2000
amount**=2
print('updated amount for multiply and division:', amount)

amount = 2000
amount//=100
print('updated amount for divide and assign:', amount)'''

print('Basic calculator')
print('----------------')

a=float(input('Enter the value of a:'))
c=input('Enter the operation you want to perform (+, -, *, /, %, **, //):')
b=float(input('Enter the value of b:'))
print('The result of', a, c, b, 'is:', eval(str(a)+c+str(b)))

'''print('/n Select the operation you want to perform')
print('1. Addition(+)')
print('2. Subtraction(-)')
print('3. Multiplication(*)')
print('4. Division(/)')
print('5. Modulus(%)')
print('6. Exponent(**)')
print('7. Floor Division(//)')

choice = int(input('Enter your choice(1/2/3/4/5/6/7):'))

match choice:
    case 1:
        print('Addition of a and b is:', a+b)
    case 2:
        print('Subtraction of a and b is:', a-b)
    case 3:
        print('Multiplication of a and b is:', a*b)
    case 4:
        print('Division of a and b is:', a/b)
    case 5:
        print('Modulus of a and b is:', a%b)
    case 6:
        print('Exponent of a and b is:', a**b)
    case 7:
        print('Floor Division of a and b is:', a//b)
    case _:
        print('Invalid choice')'''
