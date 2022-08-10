#!/usr/bin/env python
# coding: utf-8

# # Looking at DataFrame Data

# 1. Run the cell below to import required libraries and create a DataFrame

# In[2]:


import pandas as pd
import numpy as np
import random

num_rows = 100
colors = ['Red', 'Blue', 'Green']

df = pd.DataFrame( {'color': [colors[random.randint(0,2)] for _ in range(num_rows)],
                    'integers': [random.randint(0,15) for _ in range(num_rows)],
                    'floats': [random.random() for _ in range(num_rows)]})
df


# 2. Use the DataFrame `head()` method to view the top five rows. Try giving it a number as an argument to control how many rows are displayed.

# In[3]:


df.head(7)


# 3. View summary statistics using the DataFrame `describe()` method.

# In[4]:


df.describe()


# 4. The `decribe()` method accepts some optional arguments, including 'include' and 'exclude'. By default, `describe()` only shows statistics for columns with numerical data, but if you add the argument `include=np.object`, it will display statistics for columns with string data. Try this.

# In[5]:


df.describe(include=np.object)


# 5. If you change the argument to `include='all'`, it will display statistics for all columns in the data frame, inserting `NaN` (not a number) when the data type is not appropriate for the statistic. Try viewing statistics for all frames using `describe()`.

# In[6]:


df.describe(include='all')


# ## Selecting Data
# 6. You can select a column using bracket syntax very similar to that used with dictionaries. Put the column name, as a string, in brackets after the DataFrame name. Try this with the column 'color'

# In[7]:


df['color']


# 7. Try selecting the columns 'color' and 'floats' by supplying them as a list of strings in the same bracket syntax.

# In[8]:


df[['color','floats']]


# 8. The bracket syntax in DataFrames is overloaded to select rows as well. Selecting rows uses the syntax we used to select slices in Sequences: a start number, a colon, and an upper bound number. Try selecting three rows from the DataFrame using the slice `10:13`

# In[9]:


df[10:13]


# 9. Now let's try the `.loc[]` syntax. It also uses bracket syntax, but in this case you will specify both rows and columns to select. Select all of the rows by supplying a lone colon as the first argument, and the column 'color' by supplying it as a second argument (remember that arguments must be separted by a comma).

# In[10]:


df.loc[:,'color']


# 10. Now specify a slice, `10:13`, for the first argument and a list of columns, `['color', 'integers']`, as a second, to select **four** rows (the upper bound in `loc[]` is included) and two columns.

# In[11]:


df.loc[10:13 , ['color', 'integers']]


# 11. Now try the `iloc[]` syntax. This used the position of rows and columns to determine selection. In this DataFrame, the labels for the rows are the same as their position, so we can use the same slice `10:13` as the first argument. For the second, use the slice `0:2` to select the first two columns. Notice that with `iloc[]`, the upper bound is not inclusive, so you will get three rows and two columns.

# In[12]:


df.iloc[10:13 , 0:2]


# In[ ]:




