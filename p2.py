n=int(input())
oddsum=0
evensum=0
for i in range(0, n):
        x=int(input())
        if i %2==0:
                evensum+=x
        else:
                oddsum+=x
print(oddsum, evensum)
arr=list(map(int, input().split()))
oddsum=0
evensum=0
for i in range(len(arr)):
        if i % 2==0:
                evensum+=arr[i]
        else:
                oddsum+=arr[i]
print(f"{oddsum} {evensum}")