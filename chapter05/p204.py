from sanitize import sanitize
#함수 정의
def unique(player):
    try:
        with open(player+'.txt') as data:
            unique_list = [sanitize(t) for t in data.readline().strip().split(',')]
            print(sorted(set(unique_list))[0:3])
    except IOError as ioerr:
        print('File error:' + str(ioerr))
        return(None)
unique('james')
unique('julie')
unique('mikey')
unique('sarah')