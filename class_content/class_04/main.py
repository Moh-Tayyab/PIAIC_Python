#List
# A list is a collection which is ordered and changeable. Allows duplicate members.
# Lists are written with square brackets.
# Example:
#index      0 1 2 3 4
num_list = [1,2,3,4,5]
print(num_list)

#indexing
print(num_list[0]) #1
print(num_list[1]) #2
print(num_list[2]) #3
print(num_list[3]) #4
print(num_list[4]) #5

#List Methods
#append
#insert
#remove
#pop
#sort
#reverse
#len


#append
#Adds an element at the end of the list
num_list.append(6)
print(f"Add an element at end of list: {num_list}")

#insert
#Adds an element at the specified position
num_list.insert(0,0)# index, value
print(f"Add an element at specified position: {num_list}")


#pop 
#Removes the element at the specified position
#if you do not provide index it will remove last element
#if you provide index it will remove that element
num_list.pop(0) #index
print(f"Removes the element at the specified position: {num_list}")

#remove
#Removes the item with the specified value
num_list.remove(3) #value
print(f"Removes the item with the specified value: {num_list}")

#sort
#Sorts the list
num_list.sort()
print(f"Sorts the list: {num_list}")

#Sort have optional parameters:
#reverse=True → descending order
#key=function → custom sorting logic


num_list.sort(reverse=True)
print(f"{num_list}")

fruit_list = ["apple", "banana", "cherry", "kiwi"]
# Sort by length of word
fruit_list.sort(key=len)
print(f"Sort by length of word: {fruit_list}")

#len

print(len(num_list) + 2) #num_list is 5 and add 2 for test the final output in 7.