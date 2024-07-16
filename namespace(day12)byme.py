import random
rand=random.randint(1,100)
print(f"Guess the number between 1 to 100 {rand}")
n=5
while n!=0:
    guess=int(input("Guess the no:"))
    if guess==rand:
      print(f"You guessed it right,the answer was {rand}")
      end=True
    elif guess>rand:
      print("Too High")
    elif guess<rand:
      print("Too Low")
    n-=1
   
    if n==0:
     print("you ran out of guesses")
    else:
       print(f"you have {n} attempts left")