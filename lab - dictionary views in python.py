#!/usr/bin/env python
# coding: utf-8

# # Dictionary Views

# 1. Create a dictionary named 'codes' with the keys 'left' and 'right', and the values 'red' and 'green'

# In[1]:


codes = {'left':'red','right':'green'}


# 2. Set the variable codes_keys to the keys dictionary view from codes

# In[2]:


codes_keys = codes.keys()
print(codes_keys)


# 3. Set the variable codes_values to the values dictionary view from codes

# In[3]:


codes_values = codes.values()
print(codes_values)


# 4. Set the variable codes_items to the items dictionary view from codes

# In[4]:


codes_items = codes.items()
print(codes_items)


# 5. Update the value of the key 'left' in codes to 'blue'

# In[5]:


codes['left']= 'blue'


# 6. Print the values for codes_keys, codes_values, and codes_items

# In[6]:


print(codes_keys)
print(codes_values)
print(codes_items)


# 7. Notice that the dictionary views have dynamically updated with the new value. Now add a new key-value pair to codes, 'middle' : 'yellow'

# In[7]:


codes['middle'] = 'yellow'


# 8. Print the values for codes_keys, codes_values, and codes_items

# In[8]:


print(codes_keys)
print(codes_values)
print(codes_items)


# Notice that the new key value pairs have been added to the dictionary views.
