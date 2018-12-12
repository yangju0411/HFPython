from sanitize import sanitize
with open('C:\Git_project\HFPython\chapter05\james.txt') as james_data:
    James = sorted([sanitize(t) for t in james_data.readline().strip().split(',')])
    Unique_James = []
    for each_t in James:
        if each_t not in Unique_James:
            Unique_James.append(each_t)
    print(Unique_James[0:3])
with open('C:\Git_project\HFPython\chapter05\julie.txt') as Julie_data:
    Julie = sorted([sanitize(t) for t in Julie_data.readline().strip().split(',')])
    Unique_Julie = []
    for each_t in Julie:
        if each_t not in Unique_Julie:
            Unique_Julie.append(each_t)
    print(Unique_Julie[0:3])
with open('C:\Git_project\HFPython\chapter05\mikey.txt') as Mikey_data:
    Mikey = sorted([sanitize(t) for t in Mikey_data.readline().strip().split(',')])
    Unique_Mikey = []
    for each_t in Mikey:
        if each_t not in Unique_Mikey:
            Unique_Mikey.append(each_t)
    print(Unique_Mikey[0:3])
with open('C:\Git_project\HFPython\chapter05\sarah.txt') as Sarah_data:
    Sarah = sorted([sanitize(t) for t in Sarah_data.readline().strip().split(',')])
    Unique_Sarah = []
    for each_t in Sarah:
        if each_t not in Unique_Sarah:
            Unique_Sarah.append(each_t)
    print(Unique_Sarah[0:3])