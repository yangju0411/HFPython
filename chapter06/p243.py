from sanitize import sanitize
class AthleteList(list):
    def __init__(self, a_name, a_dob = None, a_times = []):
        list.__init__([])
        self.name = a_name
        self.dob = a_dob
        self.extend(a_times)
    def top3(self):
        return(sorted(set(sanitize(t) for t in self))[0:3])
def get_coach_data(filename):
    try:
        with open(filename) as f:
            data = f.readline()
            tmp = data.strip().split(',')
            return(AthleteList(tmp.pop(0), tmp.pop(0), tmp))
    except IOError as ioerr:
        print('File error:' + str(ioerr))
        return(None)
###
james = get_coach_data('james2.txt')
print(james.name + '\'s fastest times are: ' + str(james.top3()))
james.append('1.3')
james.extend(['1.1', '1.2'])
print(james.name + '\'s fastest times are: ' + str(james.top3()))

julie = get_coach_data('julie2.txt')
print(julie.name + '\'s fastest times are: ' + str(julie.top3()))
mikey = get_coach_data('mikey2.txt')
print(mikey.name + '\'s fastest times are: ' + str(mikey.top3()))
sarah = get_coach_data('sarah2.txt')
print(sarah.name + '\'s fastest times are: ' + str(sarah.top3()))