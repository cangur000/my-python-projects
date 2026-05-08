import random
import time 
randomnumber = random.randrange(1,101)

print("Welcome to the number guessing game! Pick a number between 1 and 100")
time.sleep(1.5)
print("Take a guess on the number: ")
def guessinggame():
    number = int(input(" "))
    while number != randomnumber: 
        if number < randomnumber:
            print("Higher!")
            print("Try again: ")
            number = int(input(" "))
        else:
            print("Lower!")
            print("Try again: ")
            number = int(input(" "))
    else:
        print("Congratulations!")
guessinggame()
