#!/usr/bin/env python
# coding: utf-8

# # `BERCHMANS KEVIN S`

#    ### Department of Data Science - Data and Visual Analytics Lab
#  #### Pandas Indexing and Selection

# ## `Simple Series and DataFrames` 
#  
# 
# 
# #### Import necessary modules
#    

# `Create a Series to store Temperature values for 1 week`

# In[1]:


import pandas as pd
temperature_trichy = pd.Series([40.2, 39.8, 36.3, 39.1, 41.3, 32.9, 36.6])


# `show temperature values`

# In[2]:


temperature_trichy


# In[3]:


temperature_trichy.index


# `What is the weather on 2nd day?`

# In[4]:


temperature_trichy[1]


# `Find all days and temperatures where temperature over 40.0 degree Celsius`

# In[5]:


temperature_trichy[temperature_trichy>40.0]


# `Find only day, not temperature where temperature over 40.0 degree Celsius`

# In[6]:


temperature_trichy[temperature_trichy>40.0].index


# ### Create a Dataframe for student details from List

# In[7]:


students = [['DS01', 'Rex', '1msc'], ['DS02', 'peter', '2msc'], ['CS01', 'ann', '3bsc']]
df_stud = pd.DataFrame(students, columns=['rollno', 'name', 'class']) # row index automatically generated


# `show df_stud dataframe`
# 

# In[8]:


df_stud


# `Display all column names of df_stud`

# In[9]:


df_stud.columns


# `Add a new column "address" with values ['Delhi', 'Bangalore', 'Chennai'] to df_stud`

# In[10]:


address = ['Delhi', 'Bangalore', 'Chennai']
df_stud['address'] = address
df_stud


# In[11]:


phonebook = {'rex':[9942002764, 'rex@abc.com'], 'sam':[9932176542, 'sam@xyz.com'], 'peter':[9865323645, 'ann@bhc.com']}
df_phonebook = pd.DataFrame.from_dict(phonebook, orient='index', columns=['mobile', 'email'])


# In[12]:


df_phonebook


# `Exploratory Data Analysis on Video Game Review Dataset`

# #### `Import ign.csv dataset`

# In[13]:


reviews = pd.read_csv("ign.csv")


# In[14]:


reviews


# In[15]:


reviews.head()


# In[16]:


reviews[:5]


# In[17]:


reviews.tail(3)


# In[18]:


reviews.shape


# In[19]:


reviews.dtypes


# In[20]:


reviews.tail()['title'].head()


# In[21]:


reviews[['title', 'genre']].head(10)


# In[22]:


reviews.iloc[:5]


# In[23]:


reviews.iloc[5:, 5:]


# In[24]:


reviews.iloc[:,:1]


# In[25]:


reviews.iloc[[10][:]]


# In[26]:


reviews = reviews.iloc[:,1:]


# In[27]:


reviews.head()


# In[28]:


students = [['DS01','Rex','1msc'],['DS02','peter','2msc'],['CS01','ann','3bsc']]
df_stud = pd.DataFrame(students, columns=['rollno', 'name', 'class'])


# In[29]:


df_stud


# In[30]:


df_stud.loc[:, "name"]


# In[31]:


reviews.loc[0:5]


# In[32]:


reviews.loc[:, 'score_phrase'].head()


# In[33]:


reviews['score_phrase'].head(10)


# In[34]:


some_reviews = reviews.iloc[5:15]


# In[35]:


some_reviews.head()


# In[36]:


some_reviews.loc[5:7, 'score']


# In[37]:


reviews[["score", "genre", "release_year"]].head()


# In[38]:


type(reviews["score"])


# In[39]:


reviews['score'].mean()


# In[40]:


reviews.mean()


# In[41]:


reviews.mean(axis=1).head()


# In[42]:


reviews['score'].median()


# In[43]:


reviews['score'].min()


# In[44]:


reviews['score'].max()


# In[45]:


reviews['score'].std()


# In[46]:


reviews['score'].count()


# In[47]:


reviews.describe()


# In[48]:


reviews.corr()


# In[49]:


(reviews['score'] / 2).head()


# In[50]:


score_filter = reviews["score"] > 7


# In[51]:


score_filter.head()


# In[52]:


filtered_reviews = reviews[score_filter]
filtered_reviews.head()


# In[53]:


filtered_reviews.shape
filtered_reviews['title'].head(10)


# In[54]:


xbox_one_filter = (reviews["score"] > 7) & (reviews["platform"] == "Xbox One")
filtered_reviews2 = reviews[xbox_one_filter]
filtered_reviews2.head()


# In[55]:


filtered_reviews2.shape


# In[56]:


action_reviews = reviews[reviews['genre'] == 'Action']


# In[57]:


action_reviews.head()


# In[58]:


action_reviews.shape


# In[59]:


import matplotlib.pyplot as plt
get_ipython().run_line_magic('matplotlib', 'inline')
reviews[reviews["platform"] == "Xbox One"]["score"].plot(kind="hist")


# In[60]:


reviews[reviews["platform"] == "PlayStation 4"]["score"].plot(kind="hist")


# In[ ]:




