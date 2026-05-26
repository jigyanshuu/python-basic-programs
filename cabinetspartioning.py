def check(arr, n, k, mid):
        peoplecount=1
        workload=0
        for tasks in arr:
                if workload+tasks<=mid:
                        workload+=tasks
                else:
                        peoplecount+=1
                        workload=tasks

                        if peoplecount>k:
                                return False
        return True
def solve(arr, n, k):
        low=max(arr)
        high=sum(arr)
        ans=high
        while low<=high:
                mid=(low+high)//2
                if check(arr, n, k, mid):
                        ans=mid
                        high=mid-1
                else:
                        low=mid+1
        return ans 
t=int(input())
for _ in range(t):
        n,k=map(int, input().split())
        arr=list(map(int, input().split()))
        b=solve(arr, n, k)
        print(b)