import random
letters = ['A',"B","C","D","E","F","G","H","I","J","K","L","M","N","O","P",'Q','R','S','T','U','V','W','X','Y','Z']

num =['0','1','2','3','4','5','6','7','8','9']
symbol=['!','#','$','%','&','(',')','*','+']

print("welcome to the py password generator !")

nr_letters = int(input("how many letters would you like in your password?\n"))
nr_symbols = int(input("how many symbols would you like?\n"))
nr_numbers = int(input("how many numbers would you like?\n"))
#Eazy Level - Order not randomised:
#e.g. 4 letter, 2 symbol, 2 number = JduE&
#Hard Level - Order of characters randomised:
#e.g. 4 letter, 2 symbol, 2 number = g^2jk
password = ""
for char in range(1,nr_letters+1):
    password += random.choice(letters)
for char in range(1,nr_numbers+1):
    password += random.choice(num)
for char in range(1,nr_symbols+1):
 password += random.choice(symbol)

print(password)
# random.shuffle(password)
# print(password) 
    