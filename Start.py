#This is a test script

# I need a cummit

Hello = 'Hallo World'

print(Hello + '!')

def line_seb():
    for i in range(3):
        print('')

line_seb()

play_time = True

while play_time:

    print("Lets play a 'little' game!!!")

    import random
    random_no = random.randint(0,100)

    line_seb()

    print('Guess a number between 0 and 100')
    line_seb()

    dims = True

    while dims:
        guess_true = True
        while guess_true:
            try:
                guess_no = int(input("What's your guess? "))
                guess_true = False
            except ValueError:
                print("Please enter a valid number.")
                guess_true = True

        if guess_no < random_no:
            line_seb()
            print("You're too low, guess again!")

        elif guess_no > random_no:
            line_seb()
            print("You're too high, guess again!")

        elif guess_no == random_no:
            line_seb()
            print("That's right!!! You're correct!!!")
            dims = False

    line_seb()
    play_again = input("Do you wanna play again? Yes/No: ")

    if play_again.lower() == "yes" or play_again.lower() == "y":
        print("Great lets play again!")
        
        play_time = True
    else:
        play_time = False
