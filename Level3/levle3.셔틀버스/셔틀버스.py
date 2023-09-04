timetable =	["08:00", "08:01", "08:02", "08:03"]	
inttimetable = []	
for i in timetable:
    h = int(i[0:2]) * 60
    m = int(i[3:5])
    inttimetable.append(h+m)
inttimetable = sorted(inttimetable)
start = 540
shuttle = []
lastpeople = 0
for i in range(len(inttimetable)):
    if inttimetable[i] < start:
        shuttle.append(inttimetable[i])
    print(shuttle)
    if len(shuttle) == m:
        print('m')
        print(shuttle[-1])
        shuttle = []
print(lastpeople)