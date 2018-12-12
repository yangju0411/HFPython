import pickle
import p163
new_man = []
try:
    with open("C:\Git_project\HFPython\chapter04\man_data.txt", 'rb') as man_data:
        new_man = pickle.load(man_data)
except IOError as err:
    print('File error: ' + str(err))
except pickle.PickleError as perr:
    print('Pickling error:'+ str(perr))

p163.print_lol(new_man)
    