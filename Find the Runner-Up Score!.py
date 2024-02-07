if __name__ == '__main__':
    n = int(input())
    arr = map(int, input().split())
    
    arr_to_set = sorted(set(arr) , reverse=True)
    print(arr_to_set[1])