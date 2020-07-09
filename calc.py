# #addition
# def add(x, y):
#     return x + y
# #subtraction
# def subtract(x, y):
#     return x - y
# #multiplication
# def multiply(x, y):
#     return x * y
# #division 
# def divide(x, y):
#     return x / y

# while True:
#     # Take input from the user
#     choice = input("Enter choice(+/-/*//): ")
#     # Check if choice is one of the four options
#     if choice in ('+', '-', "*', '/'):
    #     num1 = float(input("Enter first number: "))
    #     num2 = float(input("Enter second number: "))
    #     if choice == '1':
    #         print(num1, "+", num2, "=", add(num1, num2))
    #     elif choice == '2':
    #         print(num1, "-", num2, "=", subtract(num1, num2))
    #     elif choice == '3':
    #         print(num1, "*", num2, "=", multiply(num1, num2))
    #     elif choice == '4':
    #         print(num1, "/", num2, "=", divide(num1, num2))
    #     break
    # else:
        # print("Invalid Input")


def calculate():
    operation = input('''
Please type in the math operation you would like to complete:
+ to Add
- to Subtract
* to Multiply
/ to Divide 
^ for Exponents
''')
    number_1 = int(input('Please enter the first number:'))
    number_2 = int(input('Please enter the second number:'))
    if operation == '+':
        print('{} + {} = '.format(number_1, number_2))
        print(number_1 + number_2)
    elif operation == '-':
        print('{} - {} = '.format(number_1, number_2))
        print(number_1 - number_2)
    elif operation == '*':
        print('{} * {} = '.format(number_1, number_2))
        print(number_1 * number_2)
    elif operation == '/':
        print('{} / {} = '.format(number_1, number_2))
        print(number_1 / number_2)
    elif operation == '^':
        print('{} ** {} ='.format(number_1, number_2))
        print(number_1 ** number_2)
    else:
        print('Invalid Input.')
    again()
def again():
    calc_again = input('''
Do you want to calculate again?
Please type Y for YES or N for NO.
''')

    if calc_again.upper() == 'Y':
        calculate()
    elif calc_again.upper() == 'N':
        print('See you later.')
    else:
        again()

calculate()


