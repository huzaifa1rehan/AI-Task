#!/usr/bin/env python
# coding: utf-8

# In[61]:


import pandas as pd
import numpy as np
import pickle
from sklearn.svm import SVC
from sklearn.preprocessing import LabelEncoder
from sklearn.metrics import accuracy_score,confusion_matrix
from sklearn.model_selection import train_test_split


# In[62]:


df = pd.read_csv(r'C:\Users\user\Downloads\Titanic.csv')


# In[63]:


df


# In[64]:


df.head()


# In[65]:


df.tail()


# In[66]:


df.info()


# In[67]:


df.describe()


# In[68]:


df.columns


# In[69]:


df.count()


# In[70]:


df.nunique()


# In[71]:


df.isnull().sum()


# In[72]:


df


# In[73]:


df.info()


# In[74]:


le = LabelEncoder()
for i in df.select_dtypes(include='object').columns:
    df[i] = le.fit_transform(df[i])


# In[75]:


x = df['PassengerId']
y = df['Survived']


# In[76]:


x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.2)


# In[77]:


print(x_train.shape, x_test.shape, y_train.shape, y_test.shape)


# In[83]:


from sklearn.svm import SVC

x_train_reshaped = x_train.values.reshape(-1, 1)
x_test_reshaped = x_test.values.reshape(-1, 1)

model_svc = SVC()
model_svc.fit(x_train_reshaped, y_train)

model_predictions = model_svc.predict(x_test_reshaped)

print(model_predictions)


# In[85]:


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




