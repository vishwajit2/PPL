# Program to raise an exception and handle it

try:
    a = int(input("Enter a number : ")) # A non-integer value  will give ValueError
except:
    print("Please enter a integer number only")
