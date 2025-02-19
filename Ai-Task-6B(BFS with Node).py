#!/usr/bin/env python
# coding: utf-8

# In[4]:


class Node:
    def __init__(self,data):
        self.data = data
        self.next = []
        
    def add_near(self,near_node):
        self.next.append(near_node)
        
def BFS(start_node):
    visited = set()
    queue = [start_node]
    
    while queue:
        curr_node = queue.pop(0)
        if curr_node not in visited:
            print(curr_node.data)
            visited.add(curr_node)
            
            for near in curr_node.next:
                if near not in visited:
                    queue.append(near)
                    
node1 = Node('A')
node2 = Node('B')
node3 = Node('C')
node4 = Node('D')
node5 = Node('E')

node1.add_near(node2)
node1.add_near(node3)
node2.add_near(node4)
node3.add_near(node5)

BFS(node1)


# In[ ]:




