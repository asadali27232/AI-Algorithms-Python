# %% [markdown]
# # LAB 02: Advance Python

# %% [markdown]
# ## Task 1: Loops and Lists
# 
# Use loops to accept 5 random values inputs from the user and store them in a list. Then, print the list.
# 
# 

# %%
my_list = []

for i in range(5):
    my_list.append(input("Enter any value: "))

print("The given list is: ", end="")
print(my_list)

# %% [markdown]
# ## Task 2: Loops and Lists
# 
# Use loops to accept 5 number inputs from the user and store them in a list. Then, print the sum of value sin the list.
# 

# %%
my_list = []

for i in range(5):
    my_list.append(input("Enter any value: "))

print("The given list is: ", end="")
print(my_list)

sum = 0
for i in my_list:
    sum += int(i)

print("The sum of all the elements in the list is: ", end="")
print(sum)

# %% [markdown]
# ## Task 3: Loops and Lists
# 
# Use loops to accept 5 number inputs from the user and store them in a list. Then, print the list in acsending order.
# 

# %%
my_list = []

for i in range(5):
    my_list.append(input("Enter any value: "))

print("The given list in ascending order is: ", end="")
my_list.sort()
print(my_list)

# %% [markdown]
# ## Task 4: Loops and Lists
# 
# Accept two lists of 5 numbers each from the user. Then, join the two lists.
# 

# %%
list1 = [input("Enter any value: ") for i in range(5)]
list2 = [input("Enter any value: ") for i in range(5)]

print("The given lists are: ")
print(list1, list2, sep="\n")

list3 = list1 + list2
print("The concatenated list is: ", end="")
print(list3)

# %% [markdown]
# ## Task 5: Search in a List
# 
# Accept a list of 5 numbers from the user. Then, accept a number from the user and search it in the list. If the number is found, print its index. Otherwise, print "Not Found".
# 

# %%
list = [input("Enter any value: ") for i in range(10)]
print("The given list is: ", end="")
print(list)

num = int(input("Enter the number to be searched: "))

if num in list:
    print(f"The number {num} is present in the list.")
else:
    print(f"The number {num} is not present in the list.")

# %% [markdown]
# ## Task 6: Functions
# 
# Write a function that takes a person's name as an argument and returns a greeting message.
# 

# %%
def greetings(name):
    print(f"Hello {name}, have a nice day!")


greetings("Asad Ali")
greetings("Asad ur Rehaman")
greetings("Haroon")

# %% [markdown]
# ## Task 7: Palindrome
# 
# Write a function that takes a string as an argument and returns True if the string is a palindrome. Otherwise, return False.
# 

# %%
def palindrome(string):
    string = string.lower()

    if string == string[::-1]:
        return True
    else:
        return False


print(palindrome("madam"))
print(palindrome("hello"))
print(palindrome("woW"))

# %% [markdown]
# ## Task 8: 2D-Lists
# 
# Given a 3x3 matrix as 2d-Lists, print its multiplication matrix.
# 

# %%
a = [[1, 0, 0], [0, 1, 0], [0, 0, 1]]
b = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

result = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]

for i in range(len(a)):
    for j in range(len(a[0])):
        for k in range(len(b)):
            result[i][j] += a[i][k] * b[k][j]

print("The resultant matrix is: ")
for r in result:
    print(r)


