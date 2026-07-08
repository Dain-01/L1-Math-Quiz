import random

# Initializes total to 0
total = 0

# Takes two random numbers
one = random.randint(1, 20)
two = random.randint(1, 20 )


# Gives a random sign
sign_list = ["+", "-", "*", "/"]
sign = random.choice(sign_list)

# Assigns sign to equation format
if sign == "+":
    total = one + two

if sign == "-":
    total = one - two
else:
    if one < two:
        one, two = two, one

if sign == "/":
    total = one / two

if sign == "*":
    total = one * two

#Output the results

print(f" {one} {sign} {two} = {total} ")

