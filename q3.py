import json
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
    f = open('Employee1.txt','r')
    fdata = json.loads(f.read().replace("\'", "\""))
    e1_date,e1_slots = zip(*fdata['Employee1'].items())
    e1_date = e1_date[0]
    e1_slots = e1_slots[0]
    # print(e1_date)
    # print(e1_slots)

    f = open('Employee2.txt','r')
    fdata = json.loads(f.read().replace("\'", "\""))
    e2_date,e2_slots = zip(*fdata['Employee2'].items())
    e2_date = e2_date[0]
    e2_slots = e2_slots[0]
    # print(e2_date)
    # print(e2_slots)

    iphr = float(input().split()[0])
    # iphr = int(iphr)%10 + 0.60*(iphr-iphr//1)
    # print(iphr)

    if e1_date!=e2_date:
        print("No slot available")
        exit(0) 

    tm_start = datetime.strptime("9:00AM", '%I:%M%p')
    tm_end = datetime.strptime("5:00PM", '%I:%M%p')

    free_slots = []
    all_free_slots = []

    for slots in [e1_slots,e2_slots]:
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
    #     print(free)

    free = 0
    flag =  False
    for fs1 in free_slots[0]:
        for fs2 in free_slots[1]:
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
            if flag:
                break
        if flag:
            break

    if flag==False:
        print("No slot available")
        exit(0)

    #print(free[0].time(),free[1].time())
    finalslot = [free[0].time(),(free[0]+timedelta(hours=iphr)).time()]
    #print(finalslot)

    slots_str = ""
    for i in [0,1]:
        sl = []
        for fs in all_free_slots[i]:
            f = time_to_str(fs[0].time())+" - "+time_to_str(fs[1].time())
            sl.append(f)
    #     print(sl)
        slots_str += "Employee"+str(i+1)+": "+str(sl)+"\n"
    slots_str = slots_str.strip()
    print(slots_str)

    fin_slot = []
    for i in [0,1]:
        fs = time_to_str(finalslot[i])
        fin_slot.append(fs)
    # print(fin_slot)

    show_slot = {e1_date:fin_slot}
    print(show_slot)
    
    f = open("output.txt", "w")
    f.write(slots_str+"\n"+str(show_slot))
    f.close()
