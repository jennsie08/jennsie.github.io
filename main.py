# Jennie He
# This program is meant to help an indecisive user choose whether to
# study or play today.
# importing system allows me to quit the program within the code
import sys

name = input("Please enter your name: ")
# This is the introduction to the program.
# The operation ("~"*80) repeats "~" 80 times, or the length of the window,
# creating a visually appealing separator.
print("~" * 80)
# The arithmetic operation "+" prevents a space between user's name and "!"
print("Welcome,", name + "!")
print("This program exists to help you decide what to do today.")
print("From here on out, please respond to questions with either")
print("  'Yes' or 'No' (with the uppercase)")
print("  unless it does not satisfactorily answer the question.")
# This checks for understanding before beginning the program
# to prevent user error.
answer1 = input("Do you understand? : ")
if answer1 != "Yes":
    # This stops program to prevent user error.
    sys.exit("Ending program. Please restart.")
else:
    # This begins the program.
    print("~" * 80)
    print("Starting new program.")
    # This checks which path to take (study or play).
    exam = input("Do you have an exam coming up within seven days? : ")
    print("~" * 80)
    # What to do if user does not have exams.
if exam == "No":
    print("Yay! You have the option to pick whether to study for")
    print("a future exam or enjoy yourself.")
    no_exam = input("Would you like to enjoy yourself? : ")
    print("~" * 80)
    # If the user has no exams and wants to enjoy themselves.
    if no_exam == "Yes":
        print("Good for you! Everyone deserves a rest every once "
              "in a while.")
        repeat1 = int(input("How many activities have you been putting off "
                            "doing because of exams? : "))
        # Uses the input to variable "repeat1" to decide how many times
        # to ask this question.
        # The variable "retry" keeps track of how many times the for loop
        # has repeated.
        for retry in range(repeat1 + 1):
            print("Please respond to the following with lowercase letters.")
            action = input("What have you recently craved doing? : ")
            person = input("With who? (It's okay to say 'myself') : ")
            print("~" * 80)
            if person == "myself":
                # Since there is a different grammar format, I used an
                # if statement.
                print("Then by all means, please enjoy", action,
                      "by yourself!")
            else:
                print("Then by all means, please enjoy", action, "with",
                      person + "!")
            # Subtracts the total times the for loop will repeat by the
            # repetition number, telling the user how many times it will
            # now repeat.
            print("Alright,", repeat1 - (retry + 1), "more times!")
    # If the user has no exams and does not want to reward themselves.
    elif no_exam == "No":
        print("Woah, you're quite dedicated! Good for you!")
        print("Okay, let's find you something to study.")
        subject = input("What subject are you most confused on? : ")
        credit_hr = int(input("How many credit hours "
                              "is this subject? : "))
        difficulty = int(
            input("Rank the difficulty of this subject from 1 to 5: "))
        print("~" * 80)
        # The "*" multiplies the subject's credit hours with its difficulty.
        # The "//" divides the previous value by 7, spreading the studying
        # across the week. It also rounds down so that the number is not
        # outrageously long.
        print("Please study", subject, "for",
              int(credit_hr) * int(difficulty) // 7, "hours.")
# What to do if user does have exams.
elif exam == "Yes":
    # "sep=""" removes the separation between "O," "M," and "G."
    # "end="!"" adds an exclamation mark at the end of "OMG."
    print("O", "M", "G", sep="", end="!")
    print(" How unfortunate :(")
    while exam == "Yes":
        subject = input("What subject is the exam on? : ")
        # "Base" refers to base knowledge.
        base = int(
            input("Rate how well you know this subject from 1 to 10 : "))
        difficulty = int(
            input("Rank the difficulty of this subject from 1 to 5 : "))
        days = int(input("How many days away is the exam? : "))
        # Prof asked what would happen if the user ignored "within seven days"
        # statement.
        if days > 7:
            print("~" * 80)
            print("Hey! Did I or did I not say 7 days??")
            print("Whatever, I'll let it slide this time...")
        # "Base" is subtracted from ten to find how much the user does NOT know
        # the subject, which is then multiplied by difficulty, then multiplied
        # by 0.5 to calculate how much time is needed if half an hour is given
        # per the previous value. This is then divided by the number of days
        # the user has left to study.
        time = (((10 - base) * difficulty) * 0.5) / days
        print("~" * 80)
        print("Try to study", subject, "for", time,
              "hours a day until your exam!")
        print("Good luck!")
        exam = input("Would you like to ask about another exam? : ")
print("~" * 80)


# Defines the function "num_pies" with the parameter "apples."
# I was hungry and I saw apples on my counter, thus leading to this function.
def num_pies(apples):
    # Six apples are needed for one pie.
    pies = apples / 6
    return pies


# Defines where this program begins
def main():
    print("Hey, now that that's finished, could you help me on something "
          "real quick?")
    apples = int(input("How many apples could you offer, if I asked for them "
                       "right now? : "))
    # Uses the function num_pies to find how many pies can be made with the
    # number given by the user.
    pies = num_pies(apples)
    print("~" * 80)
    # If the user is useless.
    if pies == 0:
        print("Aw man... never mind then. Catch you later.")
    # If the user is useful.
    elif not pies < 0 and pies > 3:
        print("Woah! Perfect! I'm hosting a Halloween party, and we're making"
              "\napple pies for the attendees. If you'll send me those apples,"
              "\nI might be able to get you an invite!")
    # If the user has too many or a negative amount of apples, respectively
    elif pies < 0 or pies > 3:
        print("That's an odd number of apples... If you need someone to talk"
              "\nto, I'm always here, you know?")
    else:
        print("Bro how did you even get here")


# Calls the function.
if __name__ == '__main__':
    main()
print("~" * 80)
print("The program has finished. It was a pleasure talking to you!"
      "\nGoodbye for now!")
