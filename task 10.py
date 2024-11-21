#!/usr/bin/env python
# coding: utf-8

# In[117]:


import pandas as pd
import numpy as np
import pickle
from sklearn.impute import KNNImputer
from sklearn.svm import SVC
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, mean_absolute_error, r2_score
from sklearn.preprocessing import LabelEncoder
from sklearn.model_selection import train_test_split


# In[118]:


df = pd.read_csv(r'C:\Users\user\Downloads\dataset.csv')


# In[119]:


df


# In[120]:


df.head()


# In[121]:


df.tail()


# In[122]:


df.info()


# In[123]:


df.describe()


# In[124]:


df.columns


# In[125]:


df.count()


# In[126]:


df.nunique()


# In[127]:


df.isnull().sum()


# In[128]:


df = df.drop('date',axis = 1)


# In[129]:


df


# In[130]:


df.info()


# In[131]:


impute = KNNImputer()
for i in df.select_dtypes(include = 'number').columns:
    df[i] = impute.fit_transform(df[[i]])


# In[132]:


df


# In[133]:


df.info()


# In[134]:


le = LabelEncoder()


# In[135]:


for i in df.select_dtypes(include = 'object').columns:
    df[i] = le.fit_transform(df[i])


# In[136]:


df


# In[137]:


df.info()


# In[138]:


df.isnull().sum()


# In[139]:


df = df.astype('int64')


# In[140]:


df.info()


# In[141]:


x = df.drop(columns = ['price'])
y = df['price']


# In[142]:


x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.2)


# In[143]:


print(x_train.shape, x_test.shape, y_train.shape, y_test.shape)


# In[144]:


model = LinearRegression()

model.fit(x_train, y_train)
y_pred = model.predict(x_test)


# In[145]:


y_pred


# In[146]:


mse = mean_squared_error(y_test, y_pred)
rmse = np.sqrt(mse)
mae = mean_absolute_error(y_test, y_pred)
r2 = r2_score(y_test, y_pred)

print("Mean Squared Error:", mse)
print("Root Mean Squared Error:", rmse)
print("Mean Absolute Error:", mae)
print("R-squared:", r2)


# In[ ]:




