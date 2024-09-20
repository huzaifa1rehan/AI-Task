#!/usr/bin/env python
# coding: utf-8

# In[8]:


class Multiple_reflex_agent:
    def __init__(self):
        self.room_condition = {}
        
    def add_room(self,room,desire_temp):
        self.room_condition[room] = {
            'desire_temp' : desire_temp,
            'heater_on' : False
        }
    def percept(self,room,curr_temp,heater_status):
        self.curr_room = room
        self.curr_temp = curr_temp
        self.curr_heater_status = heater_status
        
    def act(self):
        desire_temp = self.room_condition[self.curr_room]['desire_temp']
        if self.curr_temp > desire_temp and self.curr_heater_status:
            return f'Turn off heater in {self.curr_room}'
        elif self.curr_temp < desire_temp and not self.curr_heater_status:
            return f'Turn onn heater in {self.curr_room}'
        else:
            return f'no action is a needed in {self.curr_room}'
agent = Multiple_reflex_agent()
agent.add_room('Living room',4)
agent.add_room('Bedroom',3)
agent.add_room('Kitchen',5)

rooms = {
    'Living room': (29,True),
    'Bedroom' : (16,False),
    'Kitchen' : (34,True)
}
for room, (temp,heater_status) in rooms.items():
    agent.percept(room,temp,heater_status)
    print(f'{room}: {temp}°C, Heater {"on" if heater_status else "off"} ==> {agent.act()}')


# In[ ]:




