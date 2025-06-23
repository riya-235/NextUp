while True:
    try:
        number = int(input("Please think of a number between 0 and 100!"))
    except:
        print("Sorry, I did not understand your input.")
        continue
    if 0<= number <100:
        break
    else:
        print("Sorry, I did not understand your input.")
guess = 50
high = 100
low = 0
while True:
    ask = input("Is your secret number 50? \nEnter 'h' to indicate the guess is too high. Enter 'l' to indicate the guess is too low. Enter 'c' to indicate I guessed correctly. ")
    if ask == "h" or ask == "l" or ask == "c":
        break
    else:
        print("Sorry, I did not understand your input.")
while ask != "c":
    if ask == "l":
        low = guess
        guess = (guess+high)/2
        guess = round(guess)
    else:
        high = guess
        guess = (guess+low)/2
        guess = round(guess)
    ask = input("Is your secret number " + str(guess) + "? \nEnter 'h' to indicate the guess is too high. Enter 'l' to indicate the guess is too low. Enter 'c' to indicate I guessed correctly. ")
print("Game over. Your secret number was: " + str(guess))