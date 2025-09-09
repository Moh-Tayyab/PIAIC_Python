
# percentage = int(input("please enter your percentage: "))

# if percentage >= 90 and percentage <= 100:
#     print("Your grade is A+")
# elif percentage >= 80 and percentage < 90:
#     print("Your grade is A")
# elif percentage >= 70 and percentage < 80:
#     print("your grade is B")
# elif percentage >= 60 and percentage < 70:
#     print("your grade is C")
# else: 
#     print("sorry try again")
    
    
 #if else condition for practice
 
user = input("Please Enter Your Role: ").lower()
 
password = input("Please enter your password according to your role: ")
 
if user in "admin" and password in "123":
    print("welcome admin")
    if user != "admin" and password in "123":
        print(f"your role {user} is incorrect. your password {password} is correct but role {user} is incorrect.")
    elif password != "123" and user in "admin":
        print(f"your password {password} is wrong. your role {user} is correct but your {password} is incorrect.")
    
elif user in "frontend developer" and password in "456":
      print(f"Welcome {user} and your pasword is {password}")
      if user != "frontend developer" and password in "456":
          print(f"your role {user} is incorrect. your password {password} is correct but role {user} is incorrect.")
      elif password in "456" and user != "frontend developer":
          print(f"your password {password} is wrong. your role {user} is correct but your {password} is incorrect.") 
          
elif user in "backend developer" and password in "789":
    print(f"Welcome {user} and your password is {password}")
    if user != "backend developer" and password in "789":
        print(f"your role {user} is incorrect. your password {password} is correct but role {user} is incorrect.")
    elif password != "789" and user in "backed developer":
        print(f"your password {password} is wrong. your role {user} is correct but your {password} is incorrect.")
    
elif user in "graphic designer" and password in "1011":
    print(f"Welcome {user} and your password is {password}")
    if user != "graphic designer" and password in "1011":
        print(f"your role {user} is incorrect. your password {password} is correct but role {user} is incorrect.")
    elif password != "1011" and user in "graphic designer":
        print(f"your password {password} is wrong. your role {user} is correct but your {password} is incorrect.")
        
    
else:
    print("Something went wrong.Please enter correct user role and password.")           
    
            