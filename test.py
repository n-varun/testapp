def interest(k):
    l = [0,2,4,6,8,21,23,25,27,29]
    if k <= 9:
        return l[k]
    k = k - 9
    i=2
    temp = 8
    last = "odd"
    while k > 0:
        curr = l[i] * 10
        if last == "odd":
            for j in range(1,10,2):
                l.append(curr+j)
                k -= 1
                if k == 0:
                    return l[-1]
            if l[i] == temp:
                last = "even"
                temp = l[-1]
        elif last == "even":
            for j in range(0,9,2):
                l.append(curr+j)
                k -= 1
                if k == 0:
                    return l[-1]
            if l[i] == temp:
                last = "odd"
                temp = l[-1]
        i += 1
    return l[k-1]


print(interest(200))





