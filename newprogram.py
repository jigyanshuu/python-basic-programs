def solve(n, s):
        def solve2(string):
                res=""
                for char in string.lower():
                        if char.isalnum():
                                res+=char
                return res
        q=solve2(s)
        totalmoves=0
        firstindex=-1
        lastindex=-1
        for i in range(len(n)):
                tag=solve2(n[i])
                if tag.startswith(q):
                        totalmoves+=1
                        if firstindex==-1:
                                firstindex=i
                        lastindex=i
        return [totalmoves, firstindex, lastindex]
n=int(input())
N=list(map(str, input().split()))
s=input()
res=solve(N, s)
for x in res:
        print(x)