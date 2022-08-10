#!/usr/bin/env python
# coding: utf-8

# # Selecting Data
# 1. Run the cell below to setup this notebook

# In[18]:


import pandas as pd
import numpy as np
import random

num_rows = 100
colors = ['Red', 'Blue', 'Green']

df = pd.DataFrame( {'color': [colors[random.randint(0,2)] for _ in range(num_rows)],
                    'integers': [random.randint(0,15) for _ in range(num_rows)],
                    'floats': [random.random() for _ in range(num_rows)]})
df.head()


# 2. Create a mask named 'red_mask' with `True` for all rows where the color is equal to 'Red'. Remember that the equals operator is a double equals `==`.

# In[19]:


red_mask = df.loc[:,'color']=='Red'
red_mask


# 3. New create a DataFrame named 'red_df' by using the mask with the data frame `df`. You can use the mask in the simple bracket syntax to filter the DataFrame.

# In[22]:


red_df = df[red_mask]
red_df


# 4. Columns have a method, `.unique()`, which will return all unique values in that column. Call this method on the `red_df.color` to confirm that it only contians 'Red' values.

# In[23]:


red_df.color.unique()


# 5. Now use the not operator, `~`, in combination with `red_mask`, to create a new DataFrame named 'no_red'. Simply put `~` in front of the mask to negate it.

# In[25]:


no_red = df[~red_mask]
no_red


# 6. Now check the values of `no_red.color` using the `.unique()` method to confirm that there are no 'Red' values.

# In[26]:


no_red.color.unique()


# 7. Create a new mask named 'three_mask' for all rows where `integers <= 3`.

# In[27]:


three_mask = df.loc[:,'integers'] <= 3


# 8. Create a new DataFrame named 'mixed_df' containing only rows whose color is 'Red' and whose integer value is equal or less than 3 by using the 'and' operator, `&` between that masks. 

# In[29]:


mixed_df = df[three_mask]
mixed_df


# 9. Now use `.unique()` to check the values of the 'color' column

# In[31]:


mixed_df.color.unique()


# 10. Use `.unique()` to check the values of the 'integer' column, confirming that they are all less than or equal to 3.

# In[33]:


mixed_df.integers.unique()


# In[ ]:




