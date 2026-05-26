def solve(arr,n):
    l=0
    #arr.sort()
    h=n-1
    k=(sum(arr))/2
    while l<h:
        if arr[l]+arr[h]==k:
            print("Yes")
            return
        elif arr[l]+arr[h]<k:
            l+=1
        else:
            h-=1
    print("No")
    return
t=int(input())
for _ in range(t):
    n=int(input())
    arr=list(map(int, input().split()))
    solve(arr,n)