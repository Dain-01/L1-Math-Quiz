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
questions_completed = 0

# Instructions

# Asks user for number of questions / infinite mode
num_questions = int_check("How many questions would you like? Push <enter> for infinite mode: ")

if num_questions == "infinite":
    mode = "infinite"
    num_questions = 5

# Game loop starts here
while questions_completed < num_questions:

    # Question heading (based on mode)
    if mode == "infinite":
        question_heading = f"\n(❁´◡`❁) Question {questions_completed + 1} (Infinite Mode) (❁´◡`❁)"
    else:
        question_heading = f"\n (●'◡'●) Question {questions_completed + 1} of {num_questions} (●'◡'●)"

    print(question_heading)
    print()

    # get user choice
    user_choice = input()

    # if user choice is exit code, break loop
    if user_choice == "xxx":
        break

    questions_completed += 1

    # if users are in infinite mode, increase number of questions!
    if mode == "infinite":
        num_questions += 1
