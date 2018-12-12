#함수 정의
def print_lol(the_list, ident = False, level = 0):
    #each_item이 리스트면 재귀 그렇지 않으면 출력
    for each_item in the_list:
        if isinstance(each_item, list):
            print_lol(each_item, ident, level + 1)
        else :
            if ident:
                for tab in range(level):
                    print("\t", end = '')
                print(each_item)
            else:
                print(each_item)