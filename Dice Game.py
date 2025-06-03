import random
import time

# Global variable
roll_again = "yes"

while roll_again == "yes" or roll_again == "y":
  print("Rolling the dice...")
  # make a delay of 1 second
  time.sleep(1)
  # create a random number b/w 1 to 6
  dice = random.randint(1, 6)
  # print the number
  print("Dice: ", dice)
  # ask the user to roll_again or not
  roll_again = input("Do you want to roll again? (yes/y)")
  # if the user entered "yes" or "y", the loop continues

# else, if the user entered anything besides "yes" or "y", the loop breaks and game ends
print("You ended the game!")