from sanitize import sanitize
with open('C:\Git_project\HFPython\chapter05\james.txt') as james_data:
    data = james_data.readline()
James = data.strip().split(',')
with open('C:\Git_project\HFPython\chapter05\julie.txt') as julie_data:
    data = julie_data.readline()
Julie = data.strip().split(',')
with open('C:\Git_project\HFPython\chapter05\mikey.txt') as mikey_data:
    data = mikey_data.readline()
Mikey = data.strip().split(',')
with open('C:\Git_project\HFPython\chapter05\sarah.txt') as sarah_data:
    data = sarah_data.readline()
Sarah = data.strip().split(',')
New_James = []
New_Julie = []
New_Mikey = []
New_Sarah = []
for each_item in James:
    New_James.append(sanitize(each_item))
for each_item in Julie:
    New_Julie.append(sanitize(each_item))
for each_item in Mikey:
    New_Mikey.append(sanitize(each_item))
for each_item in Sarah:
    New_Sarah.append(sanitize(each_item))
print(sorted(New_James))
print(sorted(New_Julie))
print(sorted(New_Mikey))
print(sorted(New_Sarah))