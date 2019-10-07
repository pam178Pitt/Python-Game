#Project 1 Intro to Python Created By: Patrick Mayer
#Part 1
from random import randint
car = randint(1, 3)
guess = int(input("Which door would you like to pick: "))
print("The car was behind door #" + format(car))
print("You picked door #" + format(guess))


print("-----------------------------------------------------")
#Part 2


from random import randint
car = randint(1, 3)
guess = int(input("Which door would you like to pick: "))

if car == 1 and guess == 1:
    print("There is a gaot behind door #2")
elif car ==2 and guess ==2:
    print("There is  gaot behind door #3")
elif car == 3 and guess == 3:
    print("There is a gaot behind door #1")
elif guess == 1 and car != 2:
    print("There is a goat behind door #2")
elif guess == 2 and car != 3:
    print("There is a goat behind door #3")
elif guess == 3 and car != 1:
    print("There is a goat behind door #1")
elif guess == 1 and car == 2:
    print("There is a goat behind door #3")
elif guess == 2 and car == 3:
    print("There is a goat behind door #1")
elif guess == 3 and car == 1:
    print("There is a goat behind door #2")
change = int(input("Would you like to change your pick (1 for yes or 2 for no): "))
print("The car was behind door #" + format(car))
if change == 1 and car == guess:
    print("You lost")
elif change == 2 and car == guess:
    print("You won")
elif change == 1 and car != guess:
    print("You won")
elif change == 2 and car != guess:
    print("You lost")

print("-------------------------------------------------------------------------------")
print("Part 3")
from random import randint
wins = 0

def main():
    global wins
    number = int(input("How many rounds of the game would you like to simulate: "))
    while number < 10 or number > 10000:
        print("Must enter number between 10 and 10000")
        number = int(input("Please try again: "))
    choice = input("Would you like to always switch or always stay: ")
    while choice != "switch" and choice != "stay":
        print("ERROR")
        choice = input("Please enter either switch or stay: ")
    if choice == "switch":
        for num in range(number):
            wins = wins + switch_choice()
        print("You won " + str(wins) + "/" + str(number) + " games ")
        print('{0:.0%}'.format(wins/number) + " of games")
    elif choice == "stay":
        for num in range(number):
              wins = wins + stay_choice()
        print("You won " + str(wins) + "/" + str(number) + " games ")
        print('{0:.0%}'.format(wins/number) + " of games")  
              

    
def stay_choice():
    car = randint(1, 3)
    choice = randint(1, 3)
    if car == choice:
        win = True
    else:
        win = False
    if win:
        won = 1
    else:
        won = 0
    return won    
    

def switch_choice():
    change = randint(1, 2)
    car = randint(1, 3)
    choice = randint(1, 3)
    if change == 1 and car == choice:
        win = False
    elif change == 2 and car == choice:
        win = True
    elif change == 1 and car != choice:
        win = True
    elif change == 2 and car != choice:
        win = False
    if win:
        won = 1
    else:
        won = 0
    return won       
        
main()     





             
