import p163
###
man = []
other = []
try:
    data = open('C:\Git_project\HFPython\chapter04\sketch.txt')
    for each_line in data:
        try:
            (role, line_spoken) = each_line.split(':')
            ###
            line_spoken = line_spoken.strip()
            if role == 'Man':
                man.append(line_spoken)
            else:
                other.append(line_spoken)
        except ValueError:
            pass
    data.close()
except IOError:
    print('The datafile is missing!')
try:
    with open("C:\Git_project\HFPython\chapter04\man_data.txt", 'w') as man_data, open("C:\Git_project\HFPython\chapter04\other_data.txt", 'w') as other_data:
        p163.print_lol(man, fh = man_data)
        p163.print_lol(other, fh = other_data)
except IOError as err:
    print('File error' + str(err))
