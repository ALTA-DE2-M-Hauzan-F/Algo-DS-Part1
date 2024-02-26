def max_sequence(arr):
    l=[]
    n= len(arr)

    # generate semua list dengan index yang berurutan
    for i in range(n):
        for j in range(n-i):
            l.append(arr[j:i+j+1])
    
    # get maximum sum per elemen l
    max_sum=sum(l[0])
    for s in l:
        sumlist=sum(s)
        if max_sum < sumlist:
             max_sum= sumlist
    return max_sum

if __name__ == "__main__":
    print(max_sequence([-2, 1, -3, 4, -1, 2, 1, -5, 4]))  # 6
    print(max_sequence([-2, -5, 6, -2, -3, 1, 5, -6]))    # 7
    print(max_sequence([-2, -3, 4, -1, -2, 1, 5, -3]))    # 7
    print(max_sequence([-2, -5, 6, -2, -3, 1, 6, -6]))    # 8
    print(max_sequence([-2, -5, 6, 2, -3, 1, 6, -6]))     # 12