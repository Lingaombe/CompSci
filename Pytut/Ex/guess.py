print("Guess a number between 1 and 100")

Guess = int(input("Enter Number"))

def guess(Guess):
    import random
    Answer = random.randint(1,100)
    
    if Guess == Answer:
        print("Good Guess! Youre correct")
    else:
        while Guess != Answer:
            if Guess > Answer:
                print("Guessed higher there")
                Guess = int(input("Guess Again"))
            elif Guess < Answer:
                print("Guessed lower there")
                Guess = int(input("Guess Again"))

    print("Correct!!, ", Answer, " is the number!")
guess(Guess)        