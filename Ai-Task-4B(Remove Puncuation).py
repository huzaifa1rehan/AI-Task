#!/usr/bin/env python
# coding: utf-8

# In[2]:


n = input('Enter a String with pumctuation')
punctuations = ['.', ',', '!', '?', ';', ':', '-', '_', '"', "'"]

result = ''
for i in n:
    if i not in punctuations:
        result +=i
        
print(result)


# In[ ]:




