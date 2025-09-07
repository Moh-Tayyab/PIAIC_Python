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
num_list.pop(0) #if you do not provide index it will remove last element
print(f"Removes the element at the specified position: {num_list}")

#remove
