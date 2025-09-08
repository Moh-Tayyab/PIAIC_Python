#List
# A list is a collection which is ordered and changeable. Allows duplicate members.
# Lists are written with square brackets.
# Example:
# index     0 1 2 3 4
num_list = [1,2,3,4,5]
print(num_list)

#indexing
print(num_list[0]) #1
print(num_list[1]) #2
print(num_list[2]) #3
print(num_list[3]) #4
print(num_list[4]) #5


# Python list Methods:

# append  >   List ke end par ek element add karta hai
# extend  >   Do lists ko merge karta hai / ek iterable ke saare elements add kar deta ha
# insert  >   Specific index par element insert karta hai
# remove  >   Pehla matching element delete karta hai
# pop     >   Index se element nikalta hai (default: last)
# index   >   Element ka pehla index return karta hai
# sort(key= , reverse)    >   List ko sort karta hai (in-place)
# reverse >   List ko ulta kar deta hai (in-place)
# clear   >   Pure list empty kar deta hai
# copy    >   List ki shallow copy banata hai
# count   >   Element kitni dafa aaya hai, yeh count karta hai
 

# append
# Adds an element at the end of the list
num_list.append(6)
print(f"Add an element at end of list: {num_list}")

# extend
# Do lists ko merge karta hai / ek iterable ke saare elements add kar deta hai
num_list.extend([6, 7, 8, 9])
print(f"{num_list}")

# insert
# Adds an element at the specified position
num_list.insert(0,0)# index, value
print(f"Add an element at specified position: {num_list}")


# pop 
# Removes the element at the specified position
# if you do not provide index it will remove last element
# if you provide index it will remove that element
num_list.pop(0) # index
print(f"Removes the element at the specified position: {num_list}")

# remove
# Removes the item with the specified value
num_list.remove(3) # value
print(f"Removes the item with the specified value: {num_list}")

# sort
# Sorts the list
num_list.sort()
print(f"Sorts the list: {num_list}")

# Sort have optional parameters:
# reverse=True → descending order
# key=function → custom sorting logic


num_list.sort(reverse=True)
print(f"{num_list}")

fruit_list = ["apple", "banana", "cherry", "kiwi"]
# Sort by length of word
fruit_list.sort(key=len)
print(f"Sort by length of word: {fruit_list}")

# reverse
# List ko ulta kar deta hai (in-place)
print(f"before apply reverse method: {num_list}")
num_list.reverse()

print(f"reverse the list: {num_list}")

# copy
# List ki shallow copy banata hai
num_list.copy()
print(f"Created same list shallow copy: {num_list}")

# count
# Element kitni dafa aaya hai, yeh count karta hai
print(f"Count element in list: {num_list.count(6)}") # 6 is two time in existed list

# clear
# Element kitni dafa aaya hai, yeh count karta hai
# num_list.clear()
# print(f"Pure list empty kar deta hai: {num_list}")





# Python list built in functions (not method)

# len
# max
# min
# sorted

print(len(num_list) + 2) # num_list is 5 and add 2 for test the final output in 7.

# max

print(max(num_list)) # list mein jo num sb sy bara ho ga wo final output ho ge.

# min
print(min(num_list)) # list mein jo num sb sy chota ho ga wo print ho ga

#print(sorted(num_list))