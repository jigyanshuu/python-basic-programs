n=int(input())
arr=list(map(int, input().split()))
dict1={1:'one',2:'two',3:'three',4:'four',5:'five',6:'six',7:'seven',8:'eight',9:'nine',10:'ten',100:'hundred'}
list1=[]
list2=[]
for i in range(len(arr)):
        if arr[i] in dict1.keys():
                list1.append(arr[i])
print(list1)