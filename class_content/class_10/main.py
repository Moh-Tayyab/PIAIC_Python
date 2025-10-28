# For loop

students = ["Ali", "Osama", "Sara"]
for student in students:
    print(student)

# While loop

num = 1
while num < 11:
  print(num)
  num = num + 1
  
# Tuple

colours_tuple = ("Green", "Yellow", "Red")
print(colours_tuple)      

# Set 

fruits_set = {"apple", "mango", "apple", "grapes", "apple"}
print(fruits_set)

# Exception Handling

try:
    first_name = "Hamza"

    print(10 / 0)
except Exception as e:
    print(e)