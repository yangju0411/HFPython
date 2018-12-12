import sys
def print_lol(the_list, ident = False, level = 0, fh = sys.stdout):
    #each_item이 리스트면 재귀 그렇지 않으면 출력
    for each_item in the_list:
        if isinstance(each_item, list):
            print_lol(each_item, ident, level + 1, fh)
        else :
            if ident:
                for tab in range(level):
                    print("\t", end = '', file = fh)
                print(each_item, file = fh)
            else:
                print(each_item, file = fh)