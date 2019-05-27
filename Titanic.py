#!/usr/bin/env python
# coding: utf-8

# In[2]:


get_ipython().run_line_magic('pylab', 'inline')
import pandas as pd 
import numpy as np


# In[10]:


df=pd.read_csv("Desktop/train.csv")


# In[12]:


print(df.head(5))


# In[13]:


print(df.tail(5))


# In[14]:


len(df)


# In[15]:


df.head()


# In[16]:


df.tail()


# In[18]:


df.count()


# In[20]:


df['Age'].min(), df['Age'].max()


# In[22]:


df['Survived'].value_counts()


# In[23]:


df['Survived'].value_counts() *100/ len(df)


# In[25]:


df['Sex'].value_counts()


# In[28]:


df['Pclass'].value_counts()


# In[33]:


get_ipython().run_line_magic('matplotlib', 'inline')
alpha_color=0.5
df['Survived'].value_counts().plot(kind='bar')


# In[36]:


df['Sex'].value_counts().plot(kind='bar',
                              color=['b','r'],
                             alpha=alpha_color)


# In[37]:


df['Pclass'].value_counts().plot(kind='bar',
                                alpha=alpha_color)


# In[38]:


df.plot(kind='scatter', x='Survived' , y='Age')

