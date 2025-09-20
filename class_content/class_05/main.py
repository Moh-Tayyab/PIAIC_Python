# functions
def sum(num1, num2):#parameters 
    
    num1 + num2
    total = num1 + num2
    return f"The Sum of {num1} and {num2} is equal to {total}"

print(sum(10, 20))

def greet(message: str) -> str:
    message = "hello how are you?"
    
    return f"{message}"

print(greet("ello"))