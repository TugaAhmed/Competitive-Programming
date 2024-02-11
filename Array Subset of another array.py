# https://www.geeksforgeeks.org/problems/array-subset-of-another-array2317/1

def isSubset( a1, a2, n, m):
    
    frequency_dict = {}
    
    for value in a1 : 
        if value in frequency_dict :
            frequency_dict[value] += 1
        else :
            frequency_dict[value] = 1

    for num in a2:
        if num in frequency_dict and frequency_dict[num] > 0:
            frequency_dict[num] -= 1
        else:
            return 'No'
    
    return 'Yes'


#{ 
 # Driver Code Starts
#Initial Template for Python 3


def main():

    T = int(input())

    while(T > 0):
        sz = [int(x) for x in input().strip().split()]
        n, m = sz[0], sz[1]
        a1 = [int(x) for x in input().strip().split()]
        a2 = [int(x) for x in input().strip().split()]
        
        print(isSubset( a1, a2, n, m))

        T -= 1


if __name__ == "__main__":
    main()

# } Driver Code Ends