# Check that users have entered a valid
# option based on a list

def int_check(question):
    while True:
        error = "please enter an integer that is 1 or more."

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


# Main Routine Starts here

# Initialize game variables
mode = "regular"
rounds_played = 0

# Instructions

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

    # get user choice
    user_choice = input()

    # if user choice is exit code, break loop
    if user_choice == "xxx":
        break

    rounds_played += 1

    # if users are in infinite mode, increase number of rounds!
    if mode == "infinite":
        num_rounds += 1
