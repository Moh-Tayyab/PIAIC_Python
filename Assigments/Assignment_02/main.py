# calculator

num_1 = int(input("Please Enter First Number: "))
num_2 = int(input("Please Enter Second Number: " ))
operator = input("Please Enter Operator (+, -, /, *): ")

def calculator(num_1, num_2, operator):
    if operator == "+":
        return f"The Sum Of {num_1} and {num_2} is {num_1 + num_2}"
    elif operator == "-":
        return f"The Difference of {num_1} and {num_2} is {num_1 - num_2}"
    elif operator == "*":
        return f"The Product of {num_1} and {num_2} is {num_1 * num_2}"
    elif operator == "/":
        if num_2 != 0:
            return f"The Division of {num_1} and {num_2} is {num_1 / num_2}"
        else:
            return "Error: Division by zero is not allowed"
    else:
        return "Please choose a correct operator (+, -, *, /)"
    
    
print(calculator(num_1, num_2, operator))    