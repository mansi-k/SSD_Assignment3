
# coding: utf-8

# In[58]:


# import json


# In[77]:


import json
with open('org.json') as f:
    data = json.load(f)
# print(data)


# In[83]:


# e1 = 220
# e2 = 750
e1,e2 = [x.strip() for x in input().split()]
flat_emp = []
l = 0
e1l = -1
e2l = -1
for level in data:
    le_dict = {}
    if e1l<0 or e2l<0 :
        for emp in data[level]:
            if 'parent' in emp:
                le_dict[emp['name']] = emp['parent']
            else:
                le_dict[emp['name']] = -1
            if e1l<0 or e2l<0:
                if emp['name']==e1:
                    e1l = l
                if emp['name']==e2:
                    e2l = l
            else:
                break;
        l+=1
        flat_emp.append(le_dict)
# print(flat_emp)
# print(e1l,e2l) 


# In[85]:



parent = {}
# parent[e1] = e1l
l=e1l
p=e1

while l>0:
    p = flat_emp[l][p]
    l-=1
    parent[p] = l

# print(parent)
    
l=e2l-1
p=flat_emp[e2l][e2]

while l>=0 and (p not in parent):
    p = flat_emp[l][p]
    l-=1
    
if l<0:
    print("No common leader")
else:
    print(p)
    print(p,"is",e1l-l,"levels above",e1)
    print(p,"is",e2l-l,"levels above",e2)

