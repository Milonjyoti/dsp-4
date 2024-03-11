#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd


# In[3]:


data = pd.read_csv(r"C:\Users\Milanjyoti\Desktop\Police Data.csv")


# In[4]:


data


# In[8]:


data.isnull( ).sum( )


# In[7]:


data.drop('country_name', axis=1, inplace=True)


# In[9]:


data.drop('search_type', axis=1, inplace=True)


# In[11]:


data


# In[13]:


data[data.violation == 'Speeding']


# In[14]:


data[data.violation == 'Speeding'].driver_gender.value_counts()


# In[15]:


# Does gender affect who gets searched during a stop?
data.groupby('driver_gender').search_conducted.sum()


# In[16]:


data


# In[21]:


#What is the mean stop_duration?
data['stop_duration'] = data['stop_duration'].map({
    '0-15 Min': 7.5, '16-30 Min': 25, '30+ Min':45
})


# In[22]:


data


# In[20]:


data['stop_duration'].mean()


# In[23]:


#Compare the age distributions for each violation
data.groupby('violation').driver_age.describe()


# In[ ]:




