def filter_list(list):
    print([i for i in list if not isinstance(i,str)])

list = ['abc',1,1,3,3,4,'zzz','y']
filter_list(list)

