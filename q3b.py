import json
import glob
from datetime import datetime, timedelta

def time_to_str(time):
    fs = str(time)[:-3]
    if int(fs[:2]) >= 12:
        if int(fs[:2]) > 12:
            fs = str(int(fs[:2])-12) + fs[2:] 
        fs+="PM"
    else:
        fs+="AM"
    return fs

if __name__=="__main__": 
    path = "q3_emp/*"
    emp_files = glob.glob(path)
#     print(emp_files)
    
    enames = []
    edates = []
    eslots = []

    for ef in emp_files:
        f = open(ef,'r')
        fdata = json.loads(f.read().replace("\'", "\""))
#         print(fdata)
        for x in fdata:
            name = x
            date,slots = zip(*fdata[x].items())
            enames.append(name)
            edates.append(date[0])
            eslots.append(slots[0])
            break
#     print(edates)
#     print(eslots)
    
    iphr = float(input().split()[0])
    
    tm_start = datetime.strptime("9:00AM", '%I:%M%p')
    tm_end = datetime.strptime("5:00PM", '%I:%M%p')

    free_slots = []
    all_free_slots = []
    
    for slots in eslots:
        free = []
        allfree = []
        prev = tm_start
        for slot in slots:
            start,end = slot.split('-')
            start = start.strip()
            end = end.strip()
            start = datetime.strptime(start, '%I:%M%p')
            end = datetime.strptime(end, '%I:%M%p')
            if start > prev:
                allfree.append([prev,start])
            if (start-prev).total_seconds()/3600 >= iphr:
                free.append([prev,start])
    #             free.append([prev.time(),start.time()])
            prev = end        
    #         print(start,end)
        if tm_end > prev:
            allfree.append([prev,tm_end])
        if (tm_end-prev).total_seconds()/3600 >= iphr:
            free.append([prev,tm_end])
        free_slots.append(free)
        all_free_slots.append(allfree)
#         print(free)
        
    free = 0
    flag =  False
    common_free_slots = free_slots[0]
    semifinal_free_slots = []
#     print(free_slots)
#     print();
    
    if len(set(edates))==1:
        for i in range(1,len(free_slots)):
            for cfi in range(len(common_free_slots)):
                fs1 = common_free_slots[cfi]
                cfslots = []
                flag = False
                for fs2 in free_slots[i]:
                    if fs1[0]<=fs2[0] and fs1[1]>=fs2[1]:
                        free = fs2
                        flag = True
                    elif fs2[0]<=fs1[0] and fs2[1]>=fs1[1]:
                        free = fs1
                        flag = True
                    elif fs1[0]<=fs2[0] and fs1[1]>=fs2[0]:
                        if (fs1[1]-fs2[0]).total_seconds()/3600 >= iphr:
                            free = fs2
                            flag = True
                    elif fs2[0]<=fs1[0] and fs2[1]>=fs1[0]:
                        if (fs2[1]-fs1[0]).total_seconds()/3600 >= iphr:
                            free = fs1
                            flag = True
                    elif fs1[1]<fs2[0]:
                        break
                    else:
                        continue
                    fs1 = free
#                     cfslots.append(free)
                if flag==True:
                    semifinal_free_slots.append(free)
    
        finalslot = []
        show_slot = "\n\nNo slot available"
#         print(semifinal_free_slots)
        for fs in semifinal_free_slots:
            if (fs[1]-fs[0]).total_seconds()/3600 >= iphr:
                finalslot = [fs[0].time(),(fs[0]+timedelta(hours=iphr)).time()]
                fin_slot = []
                for i in [0,1]:
                    fts = time_to_str(finalslot[i])
                    fin_slot.append(fts)
#                 print(fin_slot)
                show_slot = "\n\nSlot Duration: "+str(iphr)+" hour\n"+str({edates[0]:fin_slot})
                break;
                
    slots_str = ""
    for i in range(len(enames)):
        sl = []
        for fs in all_free_slots[i]:
            f = time_to_str(fs[0].time())+" - "+time_to_str(fs[1].time())
            sl.append(f)
        slots_str += enames[i]+": "+str(sl)+"\n"
#         print(sl)
#         slots_str += "Employee"+str(i+1)+": "+str(sl)+"\n"
    slots_str = slots_str.strip()
#     print(slots_str)

    output = "Available slot\n"+slots_str+show_slot
    print(output)
    
    f = open("output.txt", "w")
    f.write(output)
    f.close()