array_no = int(input())
a = list(map(int , input().split())) 
b = list(map(int , input().split())) 
c = list(map(int , input().split())) 
count = 0 
c_b_dict = {}

for i in range(array_no) :
    c_b_dict[str(i)] = b[c[i] - 1]

for i in range(array_no) :
    ai = a[i]
    for value in c_b_dict.values() :
        if ai == value :
            count += 1  
            
print(count)