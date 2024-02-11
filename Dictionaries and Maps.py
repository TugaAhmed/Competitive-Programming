# https://www.hackerrank.com/challenges/30-dictionaries-and-maps/problem


entry_no = int(input())
phone_dict = {}

for i in range(entry_no):
    entry = list(input().split(" "))
    phone_dict[entry[0]] = entry[1]


query = input()
while query:
    try:
        if query in phone_dict:
            print(query + "=" + phone_dict[query])
        else:
            print("Not found")
        query = input()
    
    except EOFError:
        break
