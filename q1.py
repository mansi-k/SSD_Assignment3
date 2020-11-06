import json
with open('org.json') as f:
    orgdata = json.load(f)
# print(data)
# e1 = 220
# e2 = 750
empno_inp_list = [x.strip() for x in input().split()]
if len(empno_inp_list) < 2:
    print("Enter atleast 2 employees")
    exit(0)

flat_orgdata = [] # dict for all levels
l = 0
emplev_inp_list = [-1 for x in empno_inp_list]

for level in orgdata:
    lev_dict = {} # dict per level
    if -1 in emplev_inp_list: # if any input emp is still not parsed 
        for emp in orgdata[level]:
            if (not emp['name'].isdecimal()) or len(emp['name'])!=3 or int(emp['name'])<1 or int(emp['name'])>999:
                print("Employee name",emp['name'],"is not a number in range 001-999")
                exit(0)
            if 'parent' in emp:
                lev_dict[emp['name']] = emp['parent']
            else:
                lev_dict[emp['name']] = -1
            if -1 in emplev_inp_list:
                for i in range(len(empno_inp_list)):
                    if emplev_inp_list[i]==-1 and empno_inp_list[i]==emp['name']:
                        emplev_inp_list[i] = l
            else:
                break
        l+=1
        flat_orgdata.append(lev_dict)
    else:
        break

# print(flat_orgdata)
# print(emplev_inp_list) 

parents = {}

for i in range(len(empno_inp_list)):
    p = empno_inp_list[i]
    l = emplev_inp_list[i]
    filter_parents = {}
    while l>0:
        p = flat_orgdata[l][p]
        l -= 1
        if i==0:
            filter_parents[p] = l
        elif p in parents:
            filter_parents[p] = l
    parents = filter_parents
#     print(filter_parents)
# print(parents)

maxlev = -1
commonboss = ''
for p in parents:
    l = parents[p]
    if l>maxlev:
        maxlev = l
        commonboss = p

if maxlev==-1:
    print("No common leader")
else:
    print(commonboss)
    for i in range(len(empno_inp_list)):
        print(commonboss,"is",emplev_inp_list[i]-maxlev,"levels above",empno_inp_list[i])
