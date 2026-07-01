import random

# Initializes total to 0
answer = 0

# Takes two random numbers
num1 = random.randint(1, 10)
num2 = random.randint(1, 10)


# Gives a random sign
sign_list = ["+", "-", "*", "/"]
sign = random.choice(sign_list)

# Assigns sign to equation format
if sign == "+":
    answer = num1 + num2

elif sign == "-":
    if num1 < num2:
        num1, num2 = num2, num1

    answer = num1 - num2

elif sign == "*":
    answer = num1 * num2

elif sign == "/":
    answer = random.randint(1, 10)
    num2 = random.randint(1, 10)
    num1 = answer * num2

# Prints out question
print(f"{num1} {sign} {num2}")

# Compares user input to answer
user_answer = int(input("Answer: "))
if user_answer == answer:
    print("Correct!")
else:
    print(f"Incorrect! Answer: {answer}")



