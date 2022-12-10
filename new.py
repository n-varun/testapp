def a(length,n):
    l = [[1,1,1,1,1,1,0],[0,1,1,0,0,0,0],[1,1,0,1,1,0,1],[1,1,1,1,0,0,1]
        ,[1,1,1,0,0,1,1],[1,0,1,1,0,1,1]
        ,[0,0,1,1,1,1,1],[1,1,1,0,0,0,0],[1,1,1,1,1,1,1],[1,1,1,0,0,1,1]]
    initial = [0,0,0,0,0,0,0]
    count = 0
    for i in range(length):
        for j in range(7):
            if initial[j] != l[int(n[i])][j]:
                count += 1
        for j in range(7):
            initial[j]=l[int(n[i])][j]
    return count


print(a(2,"13"))

