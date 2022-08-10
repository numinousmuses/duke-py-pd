#!/usr/bin/env python
# coding: utf-8

# # Creating DataFrames

# 1. Use the dictionary `data` to create a DataFrame.

# In[2]:


data = { 'col1': ['v1', 'v2', 'v3'],
         'col2': [ 0,    1,    2 ]}
import pandas as pd

pd.DataFrame(data)


# 2. Use this list of lists to create a DataFrame

# In[3]:


data = [[ 'v1', 0 ],
        [ 'v2', 1 ],
        [ 'v3', 2 ]]

pd.DataFrame(data)


# 3. Use the Pandas `read_csv()` function to read the file 'USCG.Search.Rescue.Stats.csv'. The file is located in the current directory, so no additional path needs to be pre-pended to it.

# In[4]:


pd.read_csv('USCG.Search.Rescue.Stats.csv')


# In[ ]:




