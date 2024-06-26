def threesquares(m):
    for a in range(m):
        for b in range(m):
            if (m == (8*b + 7)*4**a):
                return False
    else:
        return True


def refree(s):
    for a in range(len(s)):
        for b in range(a+1, len(s)):
            if s[a] == s[b]:
                return False
    return True

print(refree("Chaitanya"))


def hillvalley(l):
    n = len(l)
    if n == 0 or n == 1 or n == 2:
        return False
    valley, hill = 0, 0
    for i in range(1, n-1):
        # if its valley
        if l[i-1] > l[i] < l[i+1]:
            valley+=1
        # if its hill
        if l[i-1] < l[i] > l[i+1]:
            hill+=1
    return (valley == 1 and hill == 0) or (valley == 0 and hill == 1)
