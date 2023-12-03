# In Python, the finally block is always executed no matter whether there is an exception or not.

a = 10
b = 0

try:
    result = a/b
    print(result)

except:
    print("Error: Denominator cannot be 0.")

finally:
        print("This is always executed..")

# Output

# Error: Denominator cannot be 0.
# This is always executed..