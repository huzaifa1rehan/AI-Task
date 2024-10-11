#!/usr/bin/env python
# coding: utf-8

# In[5]:


class Node:
    def __init__(self,data):
        self.data = data
        self.child = []
        
    def add_child(self,child_node):
        self.child.append(child_node)
        
def dfs_with_stack(start_node):
    stack = [start_node]
    visiter = set()
    
    while stack:
        curr_node = stack.pop()
        if curr_node.data not in visiter:
            print(curr_node.data)
            visiter.add(curr_node.data)
            for child in reversed(curr_node.child):
                if child.data not in visiter:
                    stack.append(child)
                
if __name__ == '__main__':
    node = Node(10)
    node1 = Node(20)
    node2 = Node(30)
    node3 = Node(40)
    node4 = Node(50)
    
    node.add_child(node1)
    node.add_child(node2)
    node1.add_child(node3)
    node1.add_child(node4)
    
    dfs_with_stack(node)


# In[ ]:




