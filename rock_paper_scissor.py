import random
user_choice=int(input("what do you choose? Type \n 0 for Rock\n 1 for Paper\n 2 for Scissors."))

computer_choice=random.randint(0,2)
print(f"computer choose {computer_choice}")

if user_choice >3 or user_choice <0:
    print("you typed an invalid number, you lose!")
elif computer_choice==user_choice:
    print("It's a tie")
elif computer_choice==0 and user_choice==1:
    print("You win")
elif computer_choice==0 and user_choice== 2:
    print("You lose")
elif computer_choice==1 and user_choice==0:
    print("You lose")
elif computer_choice==1 and user_choice==2:
    print("You win")
elif computer_choice==2 and user_choice==0:
    print("You win")
else :
    print("You lose")
