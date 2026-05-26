def find_pair(nums):
        freq={}
        for n in nums:
                if n in freq:
                        freq[n]+=1
                else:
                        freq[n]=1
        u=sorted(freq.keys())
        size=len(u)
        for i in range(size):
                x=u[i]
                for j in range(i+1, size):
                        y=u[j]
                        if freq[x]!=freq[y]:
                                return [x,y]
        return [-1, -1]
a=list(map(int, input().split()))
print(find_pair(a))