def check(cnt_a,cnt_b):
    for i in range(26):
        if cnt_a[i]<cnt_b[i]:
            return False
    return True

def solve(a,b,n,m):
    cnt_b = [0]*26
    for i in a:
        cnt_b[ord(i)-ord('a')]+=1
    ans = n+m+1
    p1,p2,cnt_a=0,0,[0]*26
    while p2<n:
        cnt_a[ord(b[p2])-ord('a')]+=1
        while check(cnt_a,cnt_b):
            ans = min(ans,p2-p1+1)
            cnt_a[ord(b[p1])-ord('a')]-=1
            p1+=1
        p2+=1
    return ans  if ans!=n+m+1 else -1

t = int(input())
for _ in range(t):
    a,b = input().split()
    print(solve(a,b,len(b),len(a)))