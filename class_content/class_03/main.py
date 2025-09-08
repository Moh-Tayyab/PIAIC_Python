
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
 
if user == "admin" and password == "123":
    print("welcome admin")
    if user != "admin":
        print("please check your role is incorrect")
    elif password != "123":
        print("your password is wrong")
    
elif user == "frontend developer" and password == "456":
      print(f"Welcome {user} and your pasword is {password}")
      if user != "frontend developer":
          print("please check role your is incorrect ")
      elif password == "456" and user != "frontend developer":
          print(f"your password is {password} correct but your role is not correct!")    
      elif password != "456":
          print(f"role is {user}. your password is wrong")    
    
elif user == "backend developer" and password == "789":
    print(f"Welcome {user} and your password is {password}")
elif user == "graphic designer" and password == "1011":
    print(f"Welcome {user} and your password is {password}")
else:
    print("Something went wrong.Please enter correct user role and password.")           
    
            