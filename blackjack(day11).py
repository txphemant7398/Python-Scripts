card=[11,2,3,4,5,6,7,8,9,10,10,10]#
#importing random card from the above mentionoo card
import random
r1=random.choice(card)
r2=random.choice(card)
sum=r1+r2
print(f"    Your card: [{r1},{r2}],current score: {sum}")
r4=random.choice(card)
r5=random.choice(card)
computer_sum=r4+r5
print(f"    Computer's first card: {r4}")
#ask user to get another  card
if sum>21:
    print("You have busted")

elif sum<21:
    user=input("You want to draw a new card? (y/n):")
    if user=="y":
        r3=random.choice(card)
        sum=r3+sum
        print(f"    Your card: [{r1},{r2},{r3}],current score: {sum}")
        print(f"    Computer's card: [{r5}]")
        #final answer
        print(f"    Your Final hand: [{r1},{r2},{r3}],current score: {sum}")
        print(f"    Computer's final hand: {r4},{r5}")
        if sum>21:
            print("You went over, you lose")
        elif sum<21 and computer_sum<sum:
            print("You win")
        elif sum<21 and computer_sum>sum:
            print("You lose")
    elif user=="n":
       print(f"    Your Final hand: [{r1},{r2}],final score: {sum}")
       print(f"    Computer's final hand: [{r4},{r5}],final score {computer_sum}")
       if sum>21:
            print("You went over, you lose")
       elif sum<21 and computer_sum<sum:
            print(f"You win as {sum} is greater than {computer_sum} ")
       elif sum<21 and computer_sum>sum:
            print(f"You lose as {sum} is less than {computer_sum}")