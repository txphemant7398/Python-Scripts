target = int(input())

# Write your code here 👇
even=0
for number in range(2,target+1,2):
  even+=number
print( "sum of even numbers:"+str(even))
  