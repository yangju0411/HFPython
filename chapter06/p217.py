from get_coach import get_coach_data
from sanitize import sanitize
###
sarah = get_coach_data('sarah2.txt')
sarah_dic = {'name' : sarah.pop(0), 'dob' : sarah.pop(0), 'times' : sarah}
print(sarah_dic['name'] + '\'s fastest times are: ' + str(sorted(set([sanitize(t) for t in sarah_dic['times']]))[0:3]))