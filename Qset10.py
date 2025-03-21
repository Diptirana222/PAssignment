# 1. Write a Python program that checks if a number entered by the user is positive. If it is, print "The number is positive."
a = int(input("Enter the number:"))
if a>0:
    print("The number is positive.")
else:
    print("The number is not positive/negative.")  

# 2. Write a Python program that checks if a user is 18 years or older. If yes, print "You are eligible to vote."
age = int(input("Enter your age:"))
if age>=18:
    print("You are eligible to vote.")
else:
    print("You are not eligible to vote.")

# 3. Write a Python program that asks the user to enter a temperature. If the temperature is greater than 30°C, print "It's a hot day!"
tem = int(input("Enter a temperature in °C:"))
if tem>30:
    print("It's a hot day!")
else:
    print("It's not a hot day!")

# 4. Write a Python program that checks if a variable x is equal to 10. If it is, print "x is exactly 10."
x = int(input("Enter the value:"))
if x == 10:
    print("x is exactly 10.")
else:
    print("x is not exactly 10.")


# 5. Write a Python program that takes an integer input from the user and prints "Even number detected!" only if the number is divisible by 2.
O = int(input("Enter the integer:"))
if O%2==0:
    print("Even number detected!.")
else:
    print("nothing.")

# 6. Write a Python program that asks the user to enter their marks. If the marks are greater than or equal to 40, print "You have passed the exam!"  
mark = int(input("Enter your marks:"))
if mark>=40:
    print("You have passed the exam!.")
else:
    print("Shutt Failed!!!...." )

#7. Write a Python program that checks if a user's input is equal to 'Python'(case-sensitive). If it is, print "Correct! Python is awesome!"  
Pio = (input("Enter your word:"))
if Pio == 'python':
    print("Correct! python is awesome!")
else:
    print("oww noo....! that's wrong!")

#8. Write a Python program that asks the user for their age. If the age is less than 13, print "You are a child." 
bol = int(input("bhai apni age btao:"))
if bol<13:
    print("You are a child.")
else:
    print("you are adult.")

#9. Write a Python program that asks the user to enter a password If the password is "admin123", print "Access granted!"  
k = (input("Bhai password Enter kar:"))
if k == 'admin123':
    print("Access granted!.")
else:
    print("Wrong!. Wrong!.")
 

#10. Write a Python program that takes an integer input from the user. If the number is negative print "The number is negative."
e = int(input("Enter your best number:"))
if e<0:
    print("The number is negative.")
else:
    print("not negative.")
# 11