#함수 정의
def print_lol(the_list):
    #each_item이 리스트면 재귀 그렇지 않으면 출력
    for each_item in the_list:
        if isinstance(each_item, list):
            print_lol(each_item)
        else :
            print(each_item)