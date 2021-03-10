# Calculator
# Input
# if/elif/else
# functions
# while loops

# Start of Addition function
def add(num1, num2):
    addemup= num1 + num2
    return addemup

# Start of Subtraction function
def subtract(num1, num2):
    subemup= num1 - num2
    return subemup

# Start of Multiply function
def multiply(num1, num2):
    multemup= num1 * num2
    return multemup

# Start of Divide Function
def divide(num1, num2):
    divemup= num1 / num2
    return divemup

# Print Arithmetic choice for User
print("Please select operation -\n" \
        "1. Add\n" \
        "2. Subtract\n" \
        "3. Multiply\n" \
        "4. Divide\n")


# Take input from the user
select = int(input("Select operations form 1, 2, 3, 4 :"))

number_1 = int(input("Enter first number: "))
number_2 = int(input("Enter second number: "))

if select == 1:
    print(number_1, "+", number_2, "=",
                    add(number_1, number_2))

elif select == 2:
    print(number_1, "-", number_2, "=",
                    subtract(number_1, number_2))

elif select == 3:
    print(number_1, "*", number_2, "=",
                    multiply(number_1, number_2))

elif select == 4:
    print(number_1, "/", number_2, "=",
                    divide(number_1, number_2))
else:
    print("Invalid input")
