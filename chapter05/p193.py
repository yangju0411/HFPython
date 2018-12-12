from sanitize import sanitize
with open('C:\Git_project\HFPython\chapter05\james.txt') as james_data:
    James = sorted([sanitize(t) for t in james_data.readline().strip().split(',')])
    print(James)