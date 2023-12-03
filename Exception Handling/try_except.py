a = 10
b = 0

# The try block contains the code that might generate an exception
try:
    result = a/b
    print(result)
    
# When an exception occurs, it is caught by the except block. 
# The except block cannot be used without the try block.
except:
    print("Error: Denominator cannot be 0.")

# Output: Error: Denominator cannot be 0.   
