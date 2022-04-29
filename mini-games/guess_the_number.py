import random

# get name via prompt
name = str(input("Hi! What is your name? "))
print("Hi, ", name +"!")

def play_a_game():
    print("Lets play a game. I'll choose a number between 1 and 100, and you have 10 guesses to find it!")
    number = random.randrange(1,100)
    for x in range(10):
        guess = int(input(f"Guess {x+1}: "))
        heat = abs(guess-number);
        if guess == number:
            print(f"you got it! The number was {number}")
            break
        else:
            print(f"you were {heat} off")

again = False
def play_again():
    global again
    while again == False:
        play = input("Do you want to play again? y/n: ")
        if play == "y".lower():
            play_a_game()
            again = True
        elif play == "n".lower():
            break

play_a_game()
play_again()
if again == True:
    play_a_game()
    again = False
