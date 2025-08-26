# 📝 Python Assignment – 01  
**Topics:** Variables, Data Types & Operators  

![PIAIC Batch 76](https://img.shields.io/badge/PIAIC-Batch%2076-blue) 
![Python-3.10](https://img.shields.io/badge/Python-3.10-yellowgreen) 
![Status-Completed](https://img.shields.io/badge/Status-Completed-brightgreen)

---

## 👨‍🎓 Student Information  
- **Name:** Muhammad Tayyab  
- **Roll No:** PIAIC233388  
- **Batch:** 76  

---

## 📖 Description  
This repository contains the solutions for **Assignment 01** of the **PIAIC Python course (AI-101)**.  
The main objective of this assignment is to help students practice the **basics of Python**, including variables, data types, and operators.  

---

## ✅ Assignment Questions  

### **Q1: Variables & Data Types**  
1. Create the following variables:  
   - `name` → your full name  
   - `age` → your age  
   - `is_student` → a boolean value (True/False)  
2. Print all variables in one line.  
3. Print the data type of each variable using `type()`.  

---

### **Q2: Arithmetic Operators**  
Let `x = 20` and `y = 6`. Perform and print results of:  
- Addition  
- Subtraction  
- Multiplication  
- Division  
- Floor Division  
- Modulus  
- Exponent  

---

### **Q3: Assignment Operators**  
Let `num = 10`. Perform the following using assignment operators:  
1. Add 5 → `+=`  
2. Multiply by 2 → `*=`  
3. Subtract 4 → `-=`  
4. Print the final value of `num`.  

---

### **Q4: Comparison Operators**  
Take `a = 15` and `b = 12`. Check and print results of:  
- `a > b`  
- `a < b`  
- `a == b`  
- `a != b`  
- `a >= b`  
- `a <= b`  

---

### **Q5: Logical Operators**  
Let `p = True` and `q = False`. Print the result of:  
- `p and q`  
- `p or q`  
- `not p`  
- `not q`  

---

### **Q6: Real-Life Example**  
The price of one notebook is **80 rupees**.  
1. If you buy 7 notebooks, calculate the total price.  
2. If you have 600 rupees, check (using comparison operator) whether your money is enough.  
3. Print the result in a clear message.  

---

### **Q7: Bonus (Optional)**  
Take two numbers as input from the user:  
1. Print their sum.  
2. Print whether the first number is greater than the second number or not.  

---
## 💻 Sample Code Snippets  

## Q1: Variables & Data Types
```python
# Solution:

name: str = "Muhammad Tayyab"

Age: int = 20

is_student: bool = True
# Print all variables in one line.
print(f"Name: {name}, Age: {Age}, Is Student: {is_student}")
# Print the data type of each variable using type().
print(type(name), type(Age), type(is_student), sep='\n')

```

## Q2: Arithmetic Operators
```python
# Solution:

x: int = 20
y: int = 6

# Addition
addition: int = x + y
print("Addition:", addition)

# Subtraction
subtraction: int = x - y
print("Subtraction:", subtraction)

# Multiplication
multiplication: int = x * y	
print("Multiplication:", multiplication)

# Division
division: float = x / y
print("Division:", division)

# Floor Division
floor_division: int = x // y
print("Floor Division:", floor_division)

# Modulus
modulus: int = x % y
print("Modulus:", modulus)

# Exponentiation
exponentiation: int = x ** y
print("Exponentiation:", exponentiation)

```
## Q3: Assignment Operators
```python
# Solution:
num: int = 10

# Add 5 to num using the += operator.
num += 5

# Multiply num by 2 using the *= operator.
num *= 2

# Subtract 4 from num using the -= operator.
num -= 4

# Print the final value of num.
print("Final value of num:", num)
```
## Q4: Comparsion Operators

```python
# Solution:
a: int = 15
b: int = 12

# a is greater tha b (a > b) 
print("a > b (15 greater than 12):", a > b)

# a is less than b (a < b)
print("a < b (15 less than 12):", a < b)

# a is eqaul to b (a === b)
print("a == b:", a == b)

# a is not eqaul to b (a != b)
print("a != b:", a != b)

# a is greater than or eqaul to b (a >= b)
print("a >= b:", a >= b)

# a is less than or eqaul to b (a <= b)
print("a >= b:", a <= b)
```
## Q5: Logical Operators
```python

# Solution:
p: bool = True
q: bool = False

# p and q

print("p and q:", p and q) #(and operator mein dono true honay chaiye phir he result true ayega.warna false ayega)

# p or q 
print("p or q:", p or q) #(or operator mein aik true ho to result true ayega. Dono false honay par hi result false ayega)

# not p
print("not p:", not p) #(not operator true ko false aur false ko true mein convert kar deta hai)

# not q
print("not q:", not q) #(not operator true ko false aur false ko true mein convert kar deta hai)
```
## Q6: Real-Life Example
```python
# Solution:

notebook_price: int = 80

number_of_notebooks: int = 7

available_money: int = 600

total_price = notebook_price * number_of_notebooks

# check karo kya paisay kafi hain ya nahi.
is_money_enough: bool = available_money >= total_price

# this is final result
if is_money_enough:
	print(f"You have enough money to buy {number_of_notebooks} notebooks.")
else:
	print(f"You do not have enough money to buy {number_of_notebooks} notebooks.")

```
## Q7. Input Function
```python
# Solution:

# user sy input function ky zaiye 2 numbers lain. phir unka sum aur comparison karna hai.

num_1: int = int(input("Please enter first number: "))

num_2: int = int(input("Please enter second number: "))

# print their sum
print(f"The sum of {num_1} and {num_2} is: {num_1 + num_2}")

#check karo kya pehla number dosray sy bara hai ya nahi
is_first_greater: bool = num_1 > num_2

print(f"Is the first number ({num_1}) greater than the second number ({num_2})? {is_first_greater}") 
```