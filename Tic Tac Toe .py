#!/usr/bin/env python
# coding: utf-8

# In[9]:


def sum(a,b,c):
    return a + b + c
def Board(x,y):
    zero = 'x' if x[0] else ('0' if y[0] else 0)
    one = 'x' if x[1] else ('0' if y[1] else 1)
    two = 'x' if x[2] else ('0' if y[2] else 2)
    three = 'x' if x[3] else ('0' if y[3] else 3)
    four = 'x' if x[4] else ('0' if y[4] else 4)
    five = 'x' if x[5] else ('0' if y[5] else 5)
    six = 'x' if x[6] else ('0' if y[6] else 6)
    seven = 'x' if x[7] else ('0' if y[7] else 7)
    eight = 'x' if x[8] else ('0' if y[8] else 8)
    print(f'{zero} | {one} |{two}')
    print(f'--|---|---')
    print(f'{three} | {four} |{five} ')
    print(f'--|---|---')
    print(f'{six} | {seven} |{eight} ')
    
def checkwin(x,y):
    xwin = [[0,1,2],[3,4,5],[6,7,8],[0,3,6],[1,4,7],[2,5,8],[0,4,8],[2,4,6]]
    for win in xwin:
        if(sum(x[win[0]],x[win[1]],x[win[2]]) == 3):
            print('X Win')
            return 1
        if(sum(y[win[0]],y[win[1]],y[win[2]]) == 3):
            print('Y Win')
            return 0
    return -1
        
if __name__ == '__main__':
    x = [0,0,0,0,0,0,0,0,0]
    y = [0,0,0,0,0,0,0,0,0]
    turn = 1
    print('Welcom to Tic Tac Toe Game')
    while True:
        Board(x,y)
        if (turn == 1):
            print("X's chance")
            value = int(input('Please Enter a value'))
            x[value] = 1
        else:
            print("O's chance")
            value = int(input('please enter a value'))
            y[value] = 1
        cwin = checkwin(x,y)
        if(cwin!=-1):
            print('Match over')
            break
            
        turn = 1 - turn
        
        


# In[ ]:




