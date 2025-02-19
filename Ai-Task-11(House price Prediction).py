#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import numpy as np
import pickle
from sklearn.impute import KNNImputer
from sklearn.svm import SVC
from sklearn.metrics import accuracy_score,confusion_matrix
from sklearn.preprocessing import LabelEncoder
from sklearn.model_selection import train_test_split


# In[2]:


df = pd.read_csv(r'C:\Users\user\Downloads\dataset.csv')


# In[3]:


df


# In[4]:


df.head()


# In[5]:


df.tail()


# In[6]:


df.info()


# In[7]:


df.describe()


# In[8]:


df.columns


# In[9]:


df.count()


# In[10]:


df.nunique()


# In[11]:


df.isnull().sum()


# In[12]:


df = df.drop('date',axis = 1)


# In[13]:


df


# In[14]:


df.info()


# In[15]:


impute = KNNImputer()
for i in df.select_dtypes(include = 'number').columns:
    df[i] = impute.fit_transform(df[[i]])


# In[16]:


df


# In[17]:


df.info()


# In[18]:


le = LabelEncoder()


# In[19]:


for i in df.select_dtypes(include = 'object').columns:
    df[i] = le.fit_transform(df[i])


# In[20]:


df


# In[21]:


df.info()


# In[22]:


df.isnull().sum()


# In[23]:


df = df.astype('int64')


# In[24]:


df.info()


# In[25]:


x = df.drop(columns = ['price'])
y = df['price']


# In[26]:


x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.2)


# In[27]:


print(x_train.shape, x_test.shape, y_train.shape, y_test.shape)


# In[29]:


model_svc = SVC()
model_svc.fit(x_train, y_train)

print(model_svc)


# In[30]:


model_predictions = model_svc.predict(x_test)


# In[33]:


model_predictions


# In[34]:


model_accuracy_score = accuracy_score(y_test, model_predictions)

print("-- Model Accuracy Score: ", end='')
print(round(model_accuracy_score,3))


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




