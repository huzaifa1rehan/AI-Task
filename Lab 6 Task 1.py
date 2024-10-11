#!/usr/bin/env python
# coding: utf-8

# In[1]:


def bfs(graph,start):
    visited = set()
    
    def level(curr_level):
        if not curr_level:
            return
        next_level = []
        for n in curr_level:
            if n not in visited:
                print(n)
                visited.add(n)
                for near in graph[n]:
                    if near not in visited:
                        next_level.append(near)
        level(next_level)
    level([start])
    
graph = {
    0 : [1,2],
    1 : [0,3,4],
    2 : [0,5],
    3 : [1],
    4 : [1],
    5 : [2]
}
bfs(graph,0)


# In[ ]:




