# %% [markdown]
# # LAB 1: Basic Python
# 

# %% [markdown]
# ## Task 01:
# 
# Print 24 using print() function
# 

# %%
print(24)

# %% [markdown]
# ## Task 02:
# 
# Print 4.5 using print() function
# 

# %%
print(4.5)

# %% [markdown]
# ## Task 03:
# 
# Print 1234 using print() function
# 

# %%
print(1234)

# %% [markdown]
# ## Task 04:
# 
# Take a number in input and print the number.
# 

# %%
num = input("Enter a number: ")
print(num)

# %% [markdown]
# ## Task 05:
# 
# Print a string using print() function
# 

# %%
"Asad Ali"

# %% [markdown]
# ## Task 06:
# 
# Write a comment in Python
# 

# %%
"""This is a comment 
block
."""

# %% [markdown]
# ## Task 07:
# 
# Add two numbers and print the result.
# 

# %%
print(25 + 26)

# %% [markdown]
# ## Task 08:
# 
# Multiply two numbers and print the result.
# 

# %%
print(2 * 3.6)

# %% [markdown]
# ## Task 09:
# 
# Subtract two numbers and print the result.
# 

# %%
print(8 - 9)

# %% [markdown]
# ## Task 10:
# 
# Divide two numbers and print the result.
# 

# %%
print(8 / 4)

# %% [markdown]
# ## Task 11:
# 
# Divide two decimal numbers and print the result.
# 

# %%
print(23.4 / 3.1)

# %% [markdown]
# ## Task 12:
# 
# Divide two decimal numbers and print the result as int using //.
# 

# %%
print(23.4 // 3.1)

# %% [markdown]
# ## Task 13:
# 
# Divide two decimal numbers and print the result as int using int() function.
# 

# %%
print(int(23.4 / 3.1))

# %% [markdown]
# ## Task 14:
# 
# Take modulus of two numbers and print the result.
# 

# %%
print(28 % 5)

# %% [markdown]
# ## Task 15:
# 
# Take power of two numbers and print the result.
# 

# %%
print(4**3)
print(4**10)
print(4**29)
print(4**150)
print(4**1000)

# %% [markdown]
# ## Task 16:
# 
# Check operator precidence in Python.
# 

# %%
print(2 + 3 * 6)
print((2 + 3) * 6)
print(48565878 * 578453)
print(2 + 2)
print((5 - 1) * ((7 + 1) / (3 - 1)))
print(42 + 5 + 2)
# print(5 +)

# %% [markdown]
# ## Task 17:
# 
# String Formatting in Python.
# 

# %%
x = "Nancy"
print(x)

s = "My lucky number is %d, what is yours?" % 7
print(s)

s = "My lucky number is" + str(7) + ", what is yours?"
print(s)

# %% [markdown]
# ## Task 18:
# 
# Taking input in Python.
# 

# %%
name = input("What is your name? ")
print(name)

job = input("What is your job? ")
print(job)

num = input("Enter a number: ")
print("You said: " + str(num))

# %% [markdown]
# ## Task 19:
# 
# Check the given number is even or odd.
# 

# %%
# Check Even or odd
num = int(input("Enter a number: "))
if num % 2 == 0:
    print("The number is even")
else:
    print("The number is odd")

# %% [markdown]
# ## Task 20:
# 
# Print sum of first 10 integers using while loop.
# 

# %%
i = 0
sum = 0
while i <= 10:
    sum = sum + i
    i = i + 1

print(sum)

# %% [markdown]
# ## Task 21:
# 
# Print sum of given number and exit when user enter 0 uisng for loop.
# 

# %%
num = input("Enter five numbers: ").split(" ")

sum = 0
for i in num:
    sum = sum + int(i)

print(sum)

# %% [markdown]
# ## Task 22:
# 
# Print sum of given number and exit when user enter 0 uisng while loop.
# 

# %%
num = int(input("Enter a number: "))

sum = 0

while num != 0:
    num = int(input("Enter a number: "))
    sum = sum + num

print(sum)

# %% [markdown]
# ## Task 23:
# Check the given number is prime or not.

# %%
# check prime number
num = int(input("Enter a number: "))
i = 2

while i < num:
    if num % i == 0:
        print("The number is not prime")
        break
    i = i + 1

if i == num:
    print("The number is prime")

# %% [markdown]
# ## Activity 1: Grading System
# 
# Write a Python code to accept marks of a student from 1-100 and display the grade according to the following formula;
# 
# - Grade F if marks are less than 50
# - Grade E if marks are between 50 to 60
# - Grade D if marksare between 61 to 70
# - Grade C if marks are between 71 to 80
# - Grade B if marks are between 81 to 90
# - Grade A if marks are between 91 to 100
# 

# %%
def grades(marks):
    if marks > 100 and marks < 0:
        return "Invalid marks"

    if marks > 90:
        return "A"
    elif marks > 80:
        return "B"
    elif marks > 70:
        return "C"
    elif marks > 60:
        return "D"
    elif marks >= 50:
        return "E"
    else:
        return "F"


marks = int(input("Enter your marks: "))
print(grades(marks))

# %% [markdown]
# ## Acitivity 2: Factorial Calculator
# 
# Write a program that takes a number from user and calculate factorial of that number.
# 

# %%
def factorial(num):
    if num == 0:
        return 1
    else:
        return num * factorial(num - 1)


num = int(input("Enter a number: "))
print(factorial(num))


