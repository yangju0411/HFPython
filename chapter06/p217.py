from get_coach import get_coach_data
from sanitize import sanitize
###
sarah = get_coach_data('sarah2.txt')
sarah_dic = {'name' : sarah[0], 'dob' : sarah[1], 'times' : sarah[2:]}
print(sarah_dic['name'] + '\'s fastest times are: ' + str(sorted(set([sanitize(t) for t in sarah_dic['times']]))[0:3]))