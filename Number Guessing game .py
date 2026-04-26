import random 
low = 1
high = 100
answer = random.randint(low,high)
guesses =0
running = True

while running :
    
    guess = input("Enter the guess : ")
    if guess.isdigit() == True:
        guess=int(guess)
        guesses=guesses + 1
        if guess > high or guess < low:
            print("The enetered input is not correct")
        elif guess > answer:
            print("Too High Try Again")
        elif guess < answer:
            print("Too low Try Again")
        else:
            print("Correct")
            print(f"The number of guesses you took are {guesses}")
            running = False
    else:
        print("You have enetered wrong input")
