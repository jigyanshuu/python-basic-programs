t=int(input())
for _ in range(t):
    n=int(input())
    h={}
    for _ in range(n):
        row1=list(map(int, input().split()))
        for x in row1:
            if x in h:
                h[x]+=1
            else:
                h[x]=1
    boolean=True
    for i in h.values():
        if i>n:
            boolean=False
            break
    if boolean:
        print("YES")
    else:
        print("NO")