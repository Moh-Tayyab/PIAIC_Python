# lamda function and dictionary

def sum(num1, num2):
    
    return num1 + num2

print(sum(1, 6))
    
sum = lambda num_1, num_2: num_1 + num_2

    
    
# Lambda Function / Anonoymous Function

# def function_name(parameter):
    # return statement / expression / koi bhi kam krna ye value provide karna


# lambda parameters: statement / expression / koi bhi kam krna ye value provide karna

lambda num1, num2: num1 + num2 

# name of function = lambda parameters: expression / koi kam
add = lambda num1, num2: num1 + num2
# print(add(2,5))

result = add(2,5)
print(result)

# Dictionary
user_dict = {
    "name": "ramla",
    "roll_number": "PIAIC1234", 
    "age" : 14
}

# print(f"User data: {user_dict}")
# print(f"User Name is: {user_dict['name']}")
print(f"User Age is: {user_dict['age']}")


# in class task


# create user dictionary which have [name, age, roll_number, email, phone_number, squire using lambda function]

squire = lambda num1: num1 * num1
user_dict = {
    "name": "ramla",
    "roll_number": "PIAIC1234", 
    "age" : 14,
    "email": "ramle.man.ra@gmail.com",
    "phone_number" : "123456789",
    "squire": squire
}

user_data = user_dict["squire"](2)
print(user_data)

# Loops

# for loops
print("with print")
print("=" *20)
print("Ainda Homework kar ke aana hai")
print("Ainda Homework kar ke aana hai")
print("Ainda Homework kar ke aana hai")
print("Ainda Homework kar ke aana hai")
print("Ainda Homework kar ke aana hai")
print("Ainda Homework kar ke aana hai")
print("Ainda Homework kar ke aana hai")
print("Ainda Homework kar ke aana hai")
print("Ainda Homework kar ke aana hai")
print("Ainda Homework kar ke aana hai")

print("=" *20)
print("with loop")
print("=" *20)


for i in range(10):
    print("Ainda Homework kar ke aana hai")
    
    
    