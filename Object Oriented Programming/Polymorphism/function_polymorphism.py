# Function Polymorphism
# An example of a Python function that can be used on different objects is the len() function.

# For strings len() returns the number of characters:
x = "Hello World!"
print(len(x))
# Output : 12

# For tuple len() returns the number of items in the tuple
mytuple = ("Nisha","Sonal","Minal")
print(len(mytuple))
# Output : 3

# For dictionaries len() returns the number of key/value pairs in the dictionary:
thisdict = {
  "name": "Nisha Kuvalekar",
  "enroll_no": "FS21IF010",
  "add_year": 2021
}
print(len(thisdict))
# Output : 3