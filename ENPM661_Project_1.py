#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np
#start_node = np.array([[1,0,3],[4,2,5],[7,8,6]])
start_node = ([[1,2,3],[8,4,5],[7,6,0]])


# In[2]:


start_node


# In[3]:


desired_state = ([[1,2,3],[8,0,4],[7,6,5]])


# In[4]:


def search_elm(arr):
    for i in range(len(arr)):
        for j in range(len(arr[0])):
            if arr[i][j] == 0:
                row = i
                column = j
    return row,column


# In[5]:


def swipe_left(parent_nodes):
    parent = np.copy(parent_nodes)
    i,j = search_elm(parent)
    parent[i][j],parent[i][j-1] = parent[i][j-1],parent[i][j]
    return parent
    #parent_nodes.append(parent_nodes)
    
    


# In[6]:


def swipe_right(parent_nodes):
    parent = np.copy(parent_nodes)
    i,j = search_elm(parent)
    parent[i][j],parent[i][j+1] = parent[i][j+1],parent[i][j]
    return parent
    #parent_nodes.append(parent_nodes)
    
  


# In[7]:


def swipe_up(parent_nodes):
    parent = np.copy(parent_nodes)
    i,j = search_elm(parent)
    parent[i][j],parent[i-1][j] = parent[i-1][j],parent[i][j]
    return parent
    #parent_nodes.append(parent_nodes)


# In[8]:


def swipe_down(parent_nodes):
    parent = np.copy(parent_nodes)
    i,j = search_elm(parent)
    parent[i][j],parent[i+1][j] = parent[i+1][j],parent[i][j]
    return parent
    #parent_nodes.append(parent_nodes)


# In[9]:


def compare_node(start_node,desired_state):
    for i in range(3):
        for j in range(3):
            if start_node[i][j]!=desired_state[i][j]:
                return 0;
    return 1;


# In[10]:


parent_nodes = []

if compare_node(start_node,desired_state):
    print("Goal")
else:
    print("continuing")
    i,j = search_elm(start_node)
    print("Empty tile found at",(i,j))
    parent_nodes.append(start_node)
    print("parent_nodes=",parent_nodes)
    count = 1
    k=0
    while(k<count):
        current_parent_node = parent_nodes[k]
        print("current parent node=", current_parent_node)
        i,j = search_elm(current_parent_node)
        print("Empty tile found at",(i,j))
        if i == 0:
            flag = 1
            print("swiping down")
            print("current parent node=",current_parent_node)
            child_node = swipe_down(current_parent_node)
            print("swipe down=",child_node)
            print("parent_node", parent_nodes)
            if compare_node(child_node,desired_state):
                parent_nodes.append(child_node)
                print("Parent nodes=",parent_nodes)
                print("Goal")
                break
            for t in range(len(parent_nodes)):
                if(child_node == parent_nodes[t]).all():
                    flag = 0
                print("present do not add")
                    
            if(flag == 1):
                parent_nodes.append(child_node)
                print("Appending parent node")
                print(parent_nodes)
            count = count+1
            print("count =",count)
            
        if i == 1:
            flag = 1
            print("swiping up")
            print("current parent node=",current_parent_node)
            child_node_1 = swipe_up(current_parent_node)
            print("swipe up=",child_node_1)
            print("parent_node=",parent_nodes)
            if compare_node(child_node_1,desired_state): 
                parent_nodes.append(child_node_1)
                print("Parent nodes=",parent_nodes)
                print("Goal")
                break
            for t in range(len(parent_nodes)):
                if(child_node_1 == parent_nodes[t]).all():
                    flag = 0
                print("present do not add")
            if(flag==1):
                parent_nodes.append(child_node_1)
                print("Appending parent node")
                print(parent_nodes)
           
            count = count+1
            print("count=",count)
            flag = 1
            print("swiping down")
            print("current parent node=",current_parent_node)
            child_node_2 = swipe_down(current_parent_node)
            if compare_node(child_node_2,desired_state):
                parent_nodes.append(child_node_2)
                print("Goal")
                break
            for t in range(len(parent_nodes)):
                if(child_node_2 == parent_nodes[t]).all():
                    flag = 0
                print("present do not add")
                    
            if(flag == 1):
                parent_nodes.append(child_node_2)
                print("Appending parent node")
                print(parent_nodes)
           
            count = count+1
            print("count=",count)
            
        if i == 2:
            flag = 1
            print("swiping up")
            print("current parent node=", current_parent_node)
            
            child_node_3 = swipe_up(current_parent_node)
            
            print("swipe up=",child_node_3)
            print("parent_node", parent_nodes)
            
            if compare_node(child_node_3, desired_state):
                parent_nodes.append(child_node_3)
                print("Parent nodes=",parent_nodes)
                print("Goal")
                break
                
            for t in range(len(parent_nodes)):
                if(child_node_3 == parent_nodes[t]).all():
                    flag = 0
                print("present do not add")
                    
            if(flag == 1):
                parent_nodes.append(child_node_3)
                print("Appending parent node")
                print(parent_nodes)
                
            count = count+1
            print("count =",count)
            
            
        if j == 0:
            flag = 1
            print("Swiping right")
            print("Current parent node=",current_parent_node)
            child_node_4 = swipe_right(current_parent_node)
            print("swipe up=",child_node_4)
            print("parent_mode=",parent_nodes)
            if compare_node(child_node_4,desired_state):
                parent_nodes.append(child_node_4)
                print("Parent nodes=",parent_nodes)
                print("Goal")
                break
            for t in range(len(parent_nodes)):
                if(child_node_4 == parent_nodes[t]).all():
                    flag = 0
                print("present do not add")
            if(flag==1):
                parent_nodes.append(child_node_4)
                print("Appending parent node")
                print(parent_nodes)
            count = count+1
            print("count =",count)
        if  j == 1:
            flag = 1
            #i,j = search_elm(current_parent_node,0)
            print("swiping left")
            print("current parent node=",parent_nodes[k])
            child_node_5 = swipe_left(current_parent_node)
            print("swipe_left =",child_node_5)
            print("parent_mode=",parent_nodes)
            if compare_node(child_node_5,desired_state):
                parent_nodes.append(child_node_5)
                print("Parent nodes=",parent_nodes)
                print("Goal")
                break
            for t in range(len(parent_nodes)):
                if(child_node_5 == parent_nodes[t]).all():
                    flag = 0
                print("present do not add")
            if(flag==1):
                parent_nodes.append(child_node_5)
                print("Appending parent node")
                print(parent_nodes)
            count = count+1
            print("count =",count)
            print("swiping right")
            print("current parent node=",parent_nodes[k])
            child_node_6 = swipe_right(current_parent_node)
            print("swipe_right =",child_node_6)
            print("parent_node=",parent_nodes)
            if compare_node(child_node_6,desired_state):
                parent_nodes.append(child_node_6)
                print("Parent nodes=",parent_nodes)
                print("Goal")
                break
            for t in range(len(parent_nodes)):
                if(child_node_6 == parent_nodes[t]).all():
                    flag = 0
                print("present do not add")
            if(flag==1):
                parent_nodes.append(child_node_6)
                print("Appending parent node")
                print(parent_nodes)
            count = count+1
            print("count =",count)
        if j == 2:
            flag = 1
            
            print("swiping left")
            print("current parent node=",current_parent_node)
            child_node_7 = swipe_left(current_parent_node)
            print("swipe_left =",child_node_7)
            print("parent_mode=",parent_nodes)
            if compare_node(child_node_7,desired_state):
                parent_nodes.append(child_node_7)
                print("Parent nodes=",parent_nodes)
                print("Goal")
                break
            for t in range(len(parent_nodes)):
                if(child_node_7 == parent_nodes[t]).all():
                    flag = 0
                print("present do not add")
            if(flag==1):
                parent_nodes.append(child_node_7)
                print("Appending parent node")
                print(parent_nodes)
            count = count+1
            print("count =",count)
        k = k+1
        print("K=",k)



            
    
stack = np.vstack(parent_nodes)
flat_list = [item for sublist in stack for item in sublist]
new_list = []
for i in range(int(len(flat_list)/9)):
    new_list.append(flat_list[i:i+8])
    #new_list.append('\n')


with open('k_file.txt', 'w') as f:
    for item in new_list:
        f.write("%s\n" % item)


