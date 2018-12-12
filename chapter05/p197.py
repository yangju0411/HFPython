from sanitize import sanitize
with open('C:\Git_project\HFPython\chapter05\james.txt') as james_data:
    James = sorted([sanitize(t) for t in james_data.readline().strip().split(',')])
    Unique_James = []
    for each_t in James:
        if each_t not in Unique_James:
            Unique_James.append(each_t)
    print(Unique_James[0:3])
            