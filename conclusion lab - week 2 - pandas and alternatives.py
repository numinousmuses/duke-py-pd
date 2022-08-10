#!/usr/bin/env python
# coding: utf-8

# # Pandas and Alternatives

# 1. Import pandas aliased as 'pd' and numpy aliased as 'np'

# In[8]:


import pandas as pd
import numpy as np


# 2. Create a DataFrame named 'df' by reading the file 'USCG.Search.Rescue.Stats.csv' using the pandas read_csv method.

# In[9]:


df = pd.read_csv('USCG.Search.Rescue.Stats.csv')


# 3. View the top 5 rows of data using the DataFrame `head()` method.

# In[12]:


df.head(5)


# 4. View the last 5 rows by using the DataFrame `tail()` method.

# In[13]:


df.tail(5)


# 5. View the values in the 'Cases' column using  dot syntax, bracket syntax, `loc[]` or `iloc[]`.

# In[18]:


df['Cases']


# 6. Use `describe()` to view the summary statistics for the DataFrame.

# In[19]:


df.describe()


# 7. You can filter for particular values by comparing a colum to a value within the square bracket syntax. This creates a mask on the fly. Lets look at all of the rows whose case count is higher than the mean. You can get this number from the summary statistics above. 

# In[20]:


df[df.Cases > 46296.608696]


# 9. Now lets create a NumPy array with the same data. Pandas DataFrames have a `to_numpy()` method. Use this method to create an array named 'np_array'.

# In[21]:


np_array = df.to_numpy()


# 10. Call the shape attribute on the array.

# In[23]:


np_array.shape


# 11. Use the array `reshape()` method to return a 4 x 13 x 9 array (the arguments to the method will be these numbers) .

# In[24]:


np_array.reshape(4, 13, 9)


# 12. Import the dask.dataframe module aliased as 'dd'

# In[25]:


import dask.dataframe as dd


# 13. the `dask.dataframe` module has a `read_csv()` method which works in a similar fasion to the Pandas one. Use this method to read the file 'USCG.Search.Rescue.Stats.csv' into a dask DataFrame named 'ddf'

# In[26]:


ddf = dd.read_csv('USCG.Search.Rescue.Stats.csv')


# 14. Call the DataFrames `std()` method.

# In[27]:


ddf.std()


# 15. Notice that this did not calculate the standard deviation due to dask's use of lazy evaluation. add a `.compute()` after the `std()` to compute the result.

# In[28]:


ddf.std().compute()


# In[ ]:




