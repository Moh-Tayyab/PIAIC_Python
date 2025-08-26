# Q6: Real-Life Example
# The price of one notebook is 80 rupees.
# ● If you buy 7 notebooks, calculate the total price.
# ● If you have 600 rupees, check (using comparison operator) whether your money is
# enough to buy them or not.
# ● Print the result in a clear message.

# Solution:

notebook_price: int = 80

number_of_notebooks: int = 7

available_money: int = 600

total_price = notebook_price * number_of_notebooks

# check karo kya paisay kafi hain ya nahi.
is_money_enough: bool = available_money >= total_price

# this is final result
print(f"Total price for {number_of_notebooks} notebooks is: {total_price} rupees.")

