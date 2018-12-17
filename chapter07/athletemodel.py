import pickle
from athletelist import AthleteList
#get_coach_data함수
def get_coach_data(filename):
    try:
        with open(filename) as f:
            data = f.readline()
            tmp = data.strip().split(',')
            return(AthleteList(tmp.pop(0), tmp.pop(0), tmp))
    except IOError as ioerr:
        print('File error:' + str(ioerr))
        return(None)

def put_to_store(file_list):#file_list는 선수들의 파일이름 리스트
    all_athletes = {}
    for p in file_list:
        player_athlete = get_coach_data(p)
        all_athletes[player_athlete.name] = player_athlete
    try:
        with open('coachdata.pickle', 'wb') as coachsavedata:
            pickle.dump(all_athletes, coachsavedata)
    except IOError as err:
        print('File error: ' + str(err))
    return(all_athletes)

def get_from_store():
    all_athletes = {}
    try:
        with open('coachdata.pickle', 'rb') as coachrestoredata:
            all_athletes = pickle.load(coachrestoredata)
    except IOError as err:
        print('File error: ' + str(err))
    return(all_athletes)        
        
