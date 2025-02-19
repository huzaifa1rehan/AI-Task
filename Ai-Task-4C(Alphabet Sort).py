#!/usr/bin/env python
# coding: utf-8

# In[7]:


user = input("Enter a Sentence")
word = user.split()

for i in range(len(word)):
    for j in range(0,len(word)-i-1):
        if word[j].lower() >word[j+1].lower():
            word[j],word[j+1] = word[j+1],word[j]
            
sorting = ' '.join(word)
print(sorting)


# In[ ]:




