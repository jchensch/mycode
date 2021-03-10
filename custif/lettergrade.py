#!/usr/bin/env python3

message = 'Here is your Letter Grade '

# wrap connection in a float() to accept decimals as numbers
score = float(input("What is your Test Score?"))

# if input value was higher or equal to 90
if score > 100:
    message = 'YOU ARE A CHEATER!!!'
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

# I really like this!

# To challenge you a bit more, I think you should try to make cheaters not get the message printed out, and maybe play around with some more output options. Good job!
