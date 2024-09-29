#!/usr/bin/env python
# coding: utf-8

# In[5]:


import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns


# In[2]:


data=pd.read_csv("heart.csv")


# In[3]:


data.head()


# In[4]:


data.info()


# In[7]:


sns.displot(data['Age'], kde=True)


# In[9]:


sns.distplot(data['RestingBP'], kde=True, color='blue')


# In[11]:


sns.distplot(data['Cholesterol'], kde=True)


# In[12]:


sns.distplot(data['MaxHR'], kde=True)


# # Pie Charts For Categorical Values

# In[15]:


data.groupby('Sex').size().plot(kind='pie',autopct='%.1f')


# In[16]:


data.groupby('ChestPainType').size().plot(kind='pie',autopct='%.1f')


# In[17]:


data.groupby('RestingECG').size().plot(kind='pie',autopct='%.1f')


# # Violinplots

# In[21]:


sns.violinplot(y=data['Sex'],x=data['HeartDisease'])


# In[22]:


sns.violinplot(y=data['Age'],x=data['HeartDisease'])


# In[ ]:




