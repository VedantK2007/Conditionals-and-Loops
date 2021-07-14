# Warm Up



# Loops

# While Loop

# While loop takes in a boolean expression (T/F)

# Boolean operators
# -----------------

# Comparison Operators
# let x = 3
# x < 5 (Less than) True
# x > 5 (Greater than) False
# let x = 5
# x <= 5 (Less than or equal to) True
# x >= 5 (Greater than or equal to) True
# x == 5 (Equality) True
# x != 5 (Not equal to) False

# Logical Operators
# let x = 5 and y = 5
# and if x is 5 and if y is 5 True
# let x = 5 and y = 6
# if x is 5 and if y is 5 False
# or
# let x = 5 and y = 6
# if x is 5 or if y is 5 True
# if x is 8 or if y is 5 False
# not
# let x = 5
# if x is not 5 False
# if x is not 7 True

# While Loop
# While loop takes in a boolean expression (T/F)
# A while loop will only run if the boolean expression is true
# Infinite loop ! Watch out for these!
# For Loops


# range(5) => 0, 1, 2, 3, 4.
# range(0,5) => 0, 1, 2, 3, 4
# The range function is inclusive for the left parameter and exclusive for the right parameter


# List of numbers

# Get the sum of all the numbers.
# ------------------------------

# Conditionals
# ------------------------------
# Definition: if x then y
# Ex. If I go to school then I learn
# Ex. If I go to the restaurant then I will eat 
# Ex. If I drink and drive I will get into an accident

# If statements are used for decision making. If statements only run if the boolean expression is true.

# Template: if <boolean expression>:
# Template: else


# Different seasons Activity
# Winter, Spring, Summer, Fall
# Depending on what season the user says it is, we want to tend to our garden.
# Winter: print => stay inside
# Spring: print => plant trees
# Summer: print => water trees
# Fall: print => pick apples



# Guess the Number Project

import random
computerNumber = random.randint(0,10)
numberOfTries = 5
Win = False
Play = True

while Play == True:
  while numberOfTries > 0:
    playerNumber = input("Enter a number between 0-10:")
    playerNumber = int(playerNumber)
    if playerNumber > 10 or playerNumber < 0:
        print("Bad Number")
        break
    else:
       if playerNumber > computerNumber:
         print("Number is too big")
         numberOfTries = numberOfTries - 1
         print("You have " + str(numberOfTries) + " tries left")
       elif playerNumber < computerNumber:
         print("Number is too small")
         numberOfTries = numberOfTries - 1
         print("You have " + str(numberOfTries) + " tries left")
       else:
         print("You got the correct number!")
         Win = True
         break
    if Win == True:
     print("Congrats you won at " + str(numberOfTries) + " tries")
    else:
     print("Out of Tries")
     print("The number was " + str(computerNumber))
     break

    answer = input("Do you want to play again? (Y/N)")
    if answer.upper() == "N":
     print("Bye bye!")
     Play = False
    else:
     Win = False
     numberOfTries = 5 

      
