from random import randint
no_of_turn=5
no_of_easy=10

turn=0
#Funtion to check user's guess no to the actual no.
def check_answer(guess,answer,turn):
 
    if guess>answer:
        print("Too high")
        return turn-1
    elif guess < answer:
        print("Too low")
        return turn-1
    else:
        print(f"You got it! The answer was {answer}")

#make a funtion to set difficulty level
def set_dificulty():
  level=input(" chose the dificulty level .type 'hard' or 'easy':")        
  if level=="hard":
    return no_of_turn
  else:
     return no_of_easy
#chose a random between 1 and 100
def game():
    print("Welcome to the number guessing Game!")
    print("I'm thinking of a number between 1 and 100")
    answer=randint(1,100)
    print(answer)
    turn=set_dificulty()
    




    #let the user guess a no
    guess=0
    while guess!=answer:
        print(f"you have {turn} attempts remaining to guess the no.")
        guess=int(input("Make a guess:"))
        turn=check_answer(guess,answer,turn)
        if turn==0:
           print("You've run out of guesses, you lose")
           return
        elif guess!=answer:
           print("Guess again")
game()

# Track the no turns and reduce by 1 if they get it wrong 




# repeat the guessing funtonality if the get it wrong 
