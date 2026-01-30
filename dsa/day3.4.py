#Two sum
def ts(n,t):
    seen={}

    for i in range(len(n)):
        c=n[i]
        w=t-c
        if w in seen:
            return[seen[w],i]
        seen[c]=i
n = [2, 7, 11, 15]
t = 9
r=ts(n,t)
print(r)


def ts(n,t):
    seen={}

    for i in range(len(n)):
        c=n[i]
        w=t-c

        if w in seen:
            return (seen[w],i)
        
        seen[c]=i

n = [2, 7, 11, 15]
t = 9

r = ts(n, t)
print(r)