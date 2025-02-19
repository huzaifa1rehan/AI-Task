#!/usr/bin/env python
# coding: utf-8

# In[3]:


import pandas as pd

df = pd.read_csv('C:\\Users\\user\\Desktop\\mental_health_diagnosis_treatment_.csv')
df


# In[4]:


df.head()


# In[5]:


df.tail()


# In[6]:


df.describe()


# In[7]:


df.info()


# In[11]:


df.isnull().sum()


# In[21]:


df['Patient ID'].mean()


# In[22]:


df['Diagnosis'].mean()


# In[16]:


import matplotlib.pyplot as plt
import numpy as np
df = pd.DataFrame({'Patient ID': range(500)})

df['Patient ID'] = np.random.randint(1, 100, len(df))
df['Diagnosis'] = np.random.randint(1, 100, len(df))

plt.scatter(df['Patient ID'], df['Diagnosis'], color='red')
plt.title('Scatter Plot of Patient ID vs Diagnosis')
plt.xlabel('Patient ID')
plt.ylabel('Diagnosis')
plt.show()


# In[ ]:




