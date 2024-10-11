#!/usr/bin/env python
# coding: utf-8

# In[2]:


class Node:
    def __init__(self,data):
        self.data = data
        self.left = None
        self.right = None
        
def pre_order(node):
    if node:
        print(node.data,end = ' ')
        pre_order(node.left)
        pre_order(node.right)
        
def inorder(node):
    if node:
        inorder(node.left)
        print(node.data,end = ' ')
        inorder(node.right)
        
def post_order(node):
    if node:
        post_order(node.left)
        post_order(node.right)
        print(node.data,end = ' ')
        
if __name__ == '__main__':
    obj = Node(10)
    obj.left = Node(20)
    obj.right = Node(30)
    obj.left.left = Node(40)
    obj.left.right = Node(50)
    obj.right.left = Node(60)
    obj.right.right = Node(70)
    
    print('Preorder traversal')
    pre_order(obj)
    print('\nInorder Traversal')
    inorder(obj)
    print('\nPostorder Traversal')
    post_order(obj)


# In[ ]:




