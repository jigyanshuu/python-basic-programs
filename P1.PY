rows=int(input())
cols=int(input())
mat=[]
for i in range(rows):
        row=list(map(int, input().split()))
        mat.append(row)
zigzagsum=0
for i in range(rows):
        if i%2==0:
                for j in range(cols):
                        print(mat[i][j], end=" " "\n")
                        print("\n")
                        zigzagsum+=mat[i][j]
        else:
                for j in range(cols-1, -1, -1):
                        print(mat[i][j], end=" ")
                        print("\n")
                        zigzagsum+=mat[i][j]
print(zigzagsum)