# Q7: Bonus (Optional)
# Take two numbers as input from the user.
# ● Print their sum.
# ● Print whether the first number is greater than the second number or not.

# Solution:

# user sy input function ky zaiye 2 numbers lain. phir unka sum aur comparison karna hai.

num_1: int = int(input("Please enter first number: "))

num_2: int = int(input("Please enter second number: "))

# print their sum
print(f"The sum of {num_1} and {num_2} is: {num_1 + num_2}")

#check karo kya pehla number dosray sy bara hai ya nahi
is_first_greater: bool = num_1 > num_2

print(f"Is the first number ({num_1}) greater than the second number ({num_2})? {is_first_greater}") 