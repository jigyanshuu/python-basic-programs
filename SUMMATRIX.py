t=int(input())
for i in range(t):
        n=int(input())
        if n==0:
                print(0)
        s=""
        while n>0:
                s=str(n%2)+2
                n=n//2
        print(s)