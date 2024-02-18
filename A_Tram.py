# https://codeforces.com/contest/116/problem/A

n = int(input())

pass_list = []
max_pass = 0 

for stop in range(n) : 
    out , inn = map(int, input().split())
    max_pass = max_pass - out + inn 
    pass_list.append(max_pass)

print(max(pass_list))