
def sum():
  print(2 + 2)
  print("hello world")
sum()


def sum(num1, num2):
  print(num1 + num2)
sum(5,19)



def sum(num1, num2):
  return num1 + num2
result = sum(5,10)
print(result)
final_result = result * 5
print(final_result)


#def sum(num1, num2):
  #return num1 + num2

sum = lambda num1, num2: num1 + num2
print(sum(99,150))


#for i in range(10):
     # print("ainda exam tayyari ke sath attend krenga!")
# loops
# for loop
# while loop

num_list = [1,2,3,4,5,6,7,8,9,10]
#for num in num_list:
for num in range(1,11):
  #print("num value is",num)
 # list(range(1,11))
    print(num)
    

for i in range(1, 6):
  for j in range(1, 6):
    print(i / j)
    

#while condition
num =1
while num < 11:
  print(num)
  num = num + 1
  

user_input = input("please enter your value:")

while user_input != "quit":
  print("game is continue")
  user_input = input("please enter your value:")          