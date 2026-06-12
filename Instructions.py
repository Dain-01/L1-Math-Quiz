
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
(You can also exit from Infinite mode using the word "Exit"!) 
Good luck!""")
# Main routine

want_instructions = yes_no("Do you want instructions vrochacho? ")

# Display the instructions if the user wants to see them . . .

if want_instructions == "yes":
    instructions()