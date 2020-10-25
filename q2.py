import re
f = open("date_calculator.txt", "r")
sdt = []
for i in [0,1]:
    fline = f.readline()
    edt = fline.split(':')[1].strip()
    sdt.append(edt)
# print(sdt)
dt_day=[]
dt_mon=[]
dt_year=[]
mon_small = ['jan','feb','mar','apr','may','jun','jul','aug','sep','oct','nov','dec']
mon_big = ['january','february','march','april','may','june','july','august','september','october','november','december']
rgxlist1 = [r'\d{1,2}-\d{1,2}-\d{4}',r'\d{1,2}\/\d{1,2}\/\d{4}',r'\d{1,2}\.\d{1,2}\.\d{4}']
for s in sdt:
    if any(re.match(rgx,s) for rgx in rgxlist1):
        day,mon,year = re.split('[-./]',s)
    else:
        day,mon,year = s.split()
        day = re.split('["st""nd""rd""th"]',day)[0]
        mon = mon[:len(mon)-1]
        mon = ([int(i)+1 for i,val in enumerate(mon_small) if val==mon.lower()] or [int(i)+1 for i,val in enumerate(mon_big) if val==mon.lower()])[0]

    dt_day.append(int(day))
    dt_mon.append(int(mon))
    dt_year.append(int(year))
# print(dt_day,dt_mon,dt_year)
num_mons = [31,28,31,30,31,30,31,31,30,31,30,31]
num_days=[]
for i in [0,1]:
#     print("--------")
    nd = (dt_year[i]-1)*365
#     print(nd)
    for m in range(0,dt_mon[i]-1):
        nd += num_mons[m]
#     print(nd)
    nd += dt_day[i]
#     print(nd)
    dtyr = dt_year[i]
    if dt_mon[i]<2 or (dt_mon[i]==2 and dt_day[i]<29):
        dtyr -= 1
#     print(nd)
    nd += dtyr//4 - dtyr//100 + dtyr//400
#     print(nd)
    num_days.append(int(nd))
# print(num_days)
diff = abs(num_days[0]-num_days[1])

output = ""
if diff<2:
    output = "Date Difference:"+str(diff)+" day"
    print(output)
else:
    output = "Date Difference:"+str(diff)+" days"
    print(output)

f = open("output.txt", "w")
f.write(output)
f.close()
