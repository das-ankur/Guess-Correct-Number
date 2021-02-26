import random
def computer_guess(num):
    x=num
    count=0
    r=random.randint(0, x+1)
    while(True):
        if r<x:
            print("Onkur's guessed number is low.")
            x=r+1
            count+=1
            r=random.randint(0, x+1)
        elif r>x:
            print("Onkur's guessed number is high.")
            x=r-1
            count+=1
            r=random.randint(x, 101)
        else:
            print("Congrats to Onkur!")
            break
    return count
def user_guess(num):
    x=num
    count=0
    r=int(input("Guess a number:"))
    while(True):
        if r<x:
            print("Your guessed number is low.")
            count+=1
            r=int(input("Guess a number:"))
        elif r>x:
            print("Your guessed number is high.")
            count+=1
            r=int(input("Guess a number:"))
        else:
            print("Congrats, You guessed the correct number!")
            break
    return count
#driver_program
if __name__=="__main__":
    print("Welcome to the Game of Guessing. Try your luck!")
    print("Computer's Turn:")
    num=int(input("Enter a secret number(0-100): Trust me Onkur can't see it!"))
    ccount=computer_guess(num)
    print("Onkur took "+str(ccount)+" times to guess the correct number.")
    num=random.randint(0,101)
    print("Onkur selects a secret number.")
    print("Your's Turn:")
    pcount=user_guess(num)
    print("Onkur took "+str(pcount)+" times to guess the correct number.")
    if pcount<ccount:
        print("Congrats! You have won the match.")
    elif pcount>ccount:
        print("Sorry! Onkur have won the match.")
    else:
        print("Congrats both of you. The game is draw.")