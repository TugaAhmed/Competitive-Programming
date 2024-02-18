files_no = int(input())

name_count_dict = {}
files_name = []

for name in range(files_no) :
    name = input()
    if name in name_count_dict :
        name_count_dict[name] += 1
        print(name+str(name_count_dict[name]))
    else :
        name_count_dict[name] = 0
        print('OK')

