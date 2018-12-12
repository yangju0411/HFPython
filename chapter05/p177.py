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

print(sorted(James))
print(sorted(Julie))
print(sorted(Mikey))
print(sorted(Sarah))
