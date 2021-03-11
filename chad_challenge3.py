#!/usr/bin/env python3
# Defince a function that takes an argument

# code that randomly capaitalizes
from random import choice

def spongebobber(stringomobop):
    print(''.join(choice((str.upper, str.lower))(c) for c in stringomobop)) 

spongebobber("Hello World!!!")
