import random

def int_check(question):
    """Checks that users have entered and integer = 1 or more"""
    while True:
        error = "please enter an integer that is 1 or more. Or click enter for infinite mode."

        to_check = input(question)

        # check for infinite mode
        if to_check == "":
            return "infinite"

        try:

            response = int(to_check)

            # Check if the number is more then or equal to 1
            if response < 1:
                print(error)

            else:
               return response

        except ValueError:
            print(error)

def  yes_no(question):

    # check user response to a question is yes / no (y/n), returns 'yes' or 'no'

    while True:

        response =input(question).lower()

        if response == "yes" or response == "y":
            return "yes"
        elif response == "no" or response == "n":
            return "no"
        else:
            print("please enter yes / no")

def instructions():
    """Prints instructions"""

    print("""
*** Instructions ***

Choose either a certain amount of rounds or infinite mode!

Then solve the questions! 

They can range from;
- Multiplication
- Division
- Subtraction
- Addition 
(You can also exit from Infinite mode by typing "xxx") 
Good luck!""")

# Main Routine Starts here

# Initialize game variables
mode = "regular"
rounds_played = 0

answer = 0

correct = 0

incorrect = 0

# Instructions
want_instructions = yes_no("Do you want instructions vrochacho? ")

# Display the instructions if the user wants to see them . . .

if want_instructions == "yes":
    instructions()

# Asks user for number of rounds / infinite mode
num_rounds = int_check("How many rounds would you like? Push <enter> for infinite mode: ")

if num_rounds == "infinite":
    mode = "infinite"
    num_rounds = 5

# Game loop starts here
while rounds_played < num_rounds:

    # Rounds headings (based on mode)
    if mode == "infinite":
        round_heading = f"\n(❁´◡`❁) Round {rounds_played + 1} (Infinite Mode) (❁´◡`❁)"
    else:
        round_heading = f"\n (●'◡'●) Round {rounds_played + 1} of {num_rounds} (●'◡'●)"

    print(round_heading)
    print()


    # Main routine

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
        answer = random.randint(1, 12)
        num2 = random.randint(2, 12)
        num1 = answer * num2

    # Print question
    print(f"{num1} {sign} {num2}")

    # ask user for answer
    user_answer = input("Answer: ")

    # if user choice is exit code, break loop
    if user_answer == "xxx":
        print("\nyou left")
        break

    try:
        user_answer = int(user_answer)
    except ValueError:
        print("Not a number dude, skipping to the next question.")
        continue

    # Compares user input to answer
    if user_answer == answer:
        print("Correct!")
        correct += 1
    else:
        print(f"Incorrect! Answer: {answer}")
        incorrect += 1


    rounds_played += 1

    # if users are in infinite mode, increase number of rounds!
    if mode == "infinite":
        num_rounds += 1

# Asks if user wants to see their stats / score
want_stats =yes_no("Do you wanna see your score/stats?")

if want_stats == "yes":
    print("\n --- Stats ---")
    print(f"Score: {correct} / {correct + incorrect}")
    print(f"you got {correct} out of {correct + incorrect}")
if want_stats == "no":
    print("Thanks for playing!")
else:
    print("Thanks for playing!")
