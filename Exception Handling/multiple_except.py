# For each try block, there can be zero or more except blocks. 
# Multiple except blocks allow us to handle each exception differently.

try:
    
    even_numbers = [2,4,6,8]
    print(even_numbers[5])

except ZeroDivisionError:
    print("Denominator cannot be 0.")
    
except IndexError:
    print("Index Out of Bound.")

# Output: Index Out of Bound
