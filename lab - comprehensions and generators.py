#!/usr/bin/env python
# coding: utf-8

# # Comprehensions and Generators

# 1. Write a list comprehension which returns the square of each number from 0 to 15

# In[1]:


[x**2 for x in range(16)]


#  2. The expression `x%4==0` will return `True` if 4 is a factor of `x`. Write a list comprehension which will return numbers from 0 to 20 which have 4 as a factor. 

# In[10]:


#for loop function
ls = []
for x in range(21):
    if x%4==0:
        ls.append(x)

print(ls)

#list comprehension
[x for x in range(21) if x%4==0]


# 3. Write a generator function which will return the string 'foo' every fifth call, and 'moo' otherwise.

# In[3]:


def foo_moo():
    i = 0
    while True:
        if i%5==0:
            yield 'foo'      
        else:
            yield 'moo'
        i += 1
    
fm = foo_moo()

for _ in range(11):
    print(next(fm))


# 4. A comprehension using curly brackets will produce a dictionary. Set the variable 'name' to your name and use it to create a dictionary 

# In[4]:


name = 'Joshua'
items = zip(list(name), list(range(len(name))))

{x:y for x,y in items}


# In[ ]:




