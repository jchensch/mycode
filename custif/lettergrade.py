#!/usr/bin/env python3

message = 'Here is your Letter Grade '

# wrap connection in a float() to accept decimals as numbers
score = float(input("What is your Test Score?"))

# if input value was higher or equal to 90
if score > 100:
    print("YOU ARE A CHEATER!!!")
elif score >= 90:
    message = message + 'A'
elif score >= 80:
    message = message + 'B'
elif score >= 70:
    message = message + 'C'
elif score >= 60:
    message = message + 'D'
elif score <= 59:
    message = message + 'F'
print(message)

