from sanitize import sanitize
def get_coach_data(filename):
    try:
        with open(filename) as f:
            data = f.readline()
            tmp = data.strip().split(',')
            dic = {'name' : tmp.pop(0), 'dob' : tmp.pop(0), 'times' : tmp}
            print(dic['name'] + '\'s fastest times are: ' + str(sorted(set([sanitize(t) for t in dic['times']]))[0:3]))
    except IOError as ioerr:
        print('File error:' + str(ioerr))
        return(None)
###
get_coach_data('james2.txt')
get_coach_data('julie2.txt')
get_coach_data('mikey2.txt')
get_coach_data('sarah2.txt')