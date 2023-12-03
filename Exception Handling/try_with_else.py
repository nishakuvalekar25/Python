# In some situations, we might want to run a certain block of code if the code block inside try runs without any errors.
# For these cases, you can use the optional else keyword with the try statement. 

def divide(x, y): 
    try: 
        result = x // y 
        
    except ZeroDivisionError: 
        print("Sorry ! You are dividing by zero ") 
    else:
        print("Yeah ! Your answer is :", result) 
   
divide(3, 2) 
divide(3, 0)

# Output
# Yeah ! Your answer is : 1
# Sorry ! You are dividing by zero
