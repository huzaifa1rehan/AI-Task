#!/usr/bin/env python
# coding: utf-8

# In[4]:


def luhn(card_number):
    n = [int(d) for d in card_number]
    last_digit = n.pop()
    
    n.reverse()
    
    for i in range(0,len(n),2):
        n[i] *=2
        
        if n[i] > 9:
            n[i] -=9
            
    total = sum(n)+last_digit
    return total%10==0
card_number = '5555735454545'
if luhn(card_number):
    print('This is a valid card number')
else:
    print('This is not a valid card number')


# In[ ]:




