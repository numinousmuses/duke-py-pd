#!/usr/bin/env python
# coding: utf-8

# # Essential Python

# 1. The random library has a function `random.randint(a, b)` which takes two arguments, a lower integer and a higher integer, it then returns a random integer not lower than the first and not higher than the second. Use this method, with the arguments `(1, 5)` to create a list of 10 random integers. A list comprehension would be a good solution, but not the only one.

# In[4]:


import random

numbers = []

#for loop
#for i in range(10):
#     numbers.append(random.randint(1,5))

#list comprehension
[numbers.append(random.randint(1,5)) for i in range(10)]
        
numbers


# 2. Use an if statement to check if the number four is in the list. If it is, use the list `.count(a)` method to count the number of occurances of four, and insert this number into the f-string on the second line.

# In[6]:


if 4 in numbers:
    print(f"{numbers.count(4)} fours found")
else:
    print("No fours found")


# 3. Lists have a `sort()` method which will sort the list in place. Use this method to sort the numbers.

# In[7]:


numbers.sort()
numbers


# 4. Lists have a `reverse()` method which will reverse order. Use this method to reverse the order of numbers.

# In[8]:


numbers.reverse()
numbers


# 5. Use the star syntax to assign the first item to the variable `a`, the middle items to the variable `b`, and the last item to variable `c`

# In[9]:


a, *b, c = numbers
print(a)
print(b)
print(c)


# 6. Cast numbers to a set and assign the result to the variable `unique_numbers`.

# In[10]:


unique_numbers = set(numbers)
unique_numbers


# 7. Create a dictionary named `number_records` with the keys 'numbers' and 'unique_numbers' and the values `numbers` and `unique_numbers`.

# In[11]:


number_records = {'numbers':numbers, 'unique_numbers':unique_numbers}
                

number_records


# In[ ]:




