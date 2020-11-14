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

def gt_iphr(time):
    if time.total_seconds()/3600 >= iphr:
        return True
    else:
        return False

def extract_info():
    path = "q3_emp/*"
    emp_files = glob.glob(path)    
    enames = []
    edates = []
    eslots = []
    for ef in emp_files:
        f = open(ef,'r')
        fdata = json.loads(f.read().replace("\'", "\""))
        for x in fdata:
            name = x
            date,slots = zip(*fdata[x].items())
            enames.append(name)
            edates.append(date[0])
            eslots.append(slots[0])
            break
    return enames,edates,eslots

def find_all_free_slots(iphr,eslots):
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
            if gt_iphr(start-prev):
                free.append([prev,start])
            prev = end 
        if tm_end > prev:
            allfree.append([prev,tm_end])
        if gt_iphr(tm_end-prev):
            free.append([prev,tm_end])
        free_slots.append(free)
        all_free_slots.append(allfree)
    return all_free_slots, free_slots

def partly_overlap(fs1,fs2):
    free = []
    if fs1[0]<=fs2[0] and fs1[1]>=fs2[0] and gt_iphr(fs1[1]-fs2[0]):
        free = [fs2[0],fs1[1]]
    elif fs2[0]<=fs1[0] and fs2[1]>=fs1[0] and gt_iphr(fs2[1]-fs1[0]):
        free = [fs1[0],fs2[1]]
    return free

def get_if_common(fs1,fs2):
    free = []
    if fs1[0]<=fs2[0] and fs1[1]>=fs2[1]:
        free = fs2
    elif fs2[0]<=fs1[0] and fs2[1]>=fs1[1]:
        free = fs1
    else:
        free = partly_overlap(fs1,fs2)
    return free

def find_common_slots(iphr,free_slots,edates):
    free = 0
    flag =  False
    common_free_slots = free_slots[0]
    semifinal_free_slots = free_slots[0]
    for i in range(1,len(free_slots)):
        common_free_slots = semifinal_free_slots
        cmlen = len(common_free_slots)
        semifinal_free_slots = []
        for fi in range(len(free_slots[i])):
            fs1 = free_slots[i][fi]
            for ci in range(cmlen):
                fs2 = common_free_slots[ci]
                free = get_if_common(fs1,fs2)
                if free:
                    semifinal_free_slots.append(free)
                elif fs1[1]<fs2[0]:
                    break
                else:
                    continue                    
    return semifinal_free_slots

def get_final_common_slot(iphr,semifinal_free_slots):
    finalslot = []
    for fs in semifinal_free_slots:
        if gt_iphr(fs[1]-fs[0]):
            finalslot = [fs[0].time(),(fs[0]+timedelta(hours=iphr)).time()]
            fin_slot = []
            for i in [0,1]:
                fts = time_to_str(finalslot[i])
                fin_slot.append(fts)
            break
    return fin_slot

def write_output(enames,edates,fin_slot,iphr):
    show_slot = "\n\nNo slot available"
    if fin_slot:
        show_slot = "\n\nSlot Duration: "+str(iphr)+" hour\n"+str({edates[0]:fin_slot})
    slots_str = ""
    for i in range(len(enames)):
        sl = []
        for fs in all_free_slots[i]:
            f = time_to_str(fs[0].time())+" - "+time_to_str(fs[1].time())
            sl.append(f)
        slots_str += enames[i]+": "+str(sl)+"\n"
    slots_str = slots_str.strip()
    output = "Available slots\n"+slots_str+show_slot
    print(output)
    f = open("output.txt", "w")
    f.write(output)
    f.close()

enames,edates,eslots = extract_info()
iphr = float(input().split()[0])
all_free_slots, free_slots = find_all_free_slots(iphr,eslots)
fin_slot = []
if len(set(edates))==1:
    semifinal_free_slots = find_common_slots(iphr,free_slots,edates)
    fin_slot = get_final_common_slot(iphr,semifinal_free_slots)
write_output(enames,edates,fin_slot,iphr)
    
