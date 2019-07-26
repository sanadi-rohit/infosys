#infosys infytq question
#A game called diamond mine
#map is a 2D matrix
#we start from (0,0) and move to (m-1,n-1) by moving right and down, where m and n are dimensions
#after reaching, we come back to (0,0) by moving up and left.
#values in map, 0 means path, 1 means diamond, -1 means obstacle
#input enter the matrix information
#output: maximum no of diamonds that can be collected

def collectMax(mat):
    r = len(mat)-1
    c = len(mat[0])-1
    if mat[r][c] == -1:
        return 0
    else:
        count=[]
        a=0
        b=0
        flag=1
        reached=0
        repeatr=0
        repeatc=0
        repr=0
        repc=0
        skip=1
        for i in mat:
            i.append(-1)
        l=[]
        for j in range(c):
            l.append(-1)
        mat.append(l)
        print(mat)
        while 1:
            if flag:
                if a==r and b==c:
                    if mat[a][b]==1:
                        print(a,b)
                        print(mat[a][b])
                        count.append(1)
                        mat[a][b]=0
                    flag=0
                    reached=1
                    print("reached")
                elif b<=r and mat[a][b+1]!=-1 and skip:
                    b=b+1
                    print(a,b)
                    if mat[a][b]==1:
                        print(mat[a][b])
                        count.append(1)
                        mat[a][b]=0
                    else:
                        count.append(0)
                    print("-----")
                elif a+1<=c and mat[a+1][b]!=-1:
                    a=a+1
                    print(a,b)
                    skip=1
                    if mat[a][b]==1:
                        print(mat[a][b])
                        count.append(1)
                        mat[a][b]=0
                    else:
                        count.append(0)
                    print("______")
                else:
                    if repeatr<r:
                        print("repeating")
                        repeatr=repeatr+1
                        b=b-1
                        skip=0
                        if len(count)!=0:
                            count.pop()
                    else:
                        if repeatc<c:
                            print("repeating")
                            a=a+1
                            for i in range(c-b):
                                if len(count) != 0:
                                    count.pop()
                        else:
                            print("did not reach end")
                            break
            else:
                print("comming back")
                if a==0 and b==0:
                    break
                elif b-1>=0 and mat[a][b-1]!=-1:
                    b=b-1
                    print(a,b)
                    if mat[a][b]==1:
                        print(mat[a][b])
                        count.append(1)
                        mat[a][b]=0
                    else:
                        count.append(0)
                    print("_____")
                elif a-1>=0 and mat[a-1][b]!=-1:
                    a=a-1
                    print(a,b)
                    if mat[a][b]==1:
                        print(mat[a][b])
                        count.append(1)
                        mat[a][b]=0
                    else:
                        count.append(0)
                    print("------")
                else:
                    if repr>=0:
                        print("repeating")
                        repr = repr + 1
                        b = b - 1
                        if len(count) != 0:
                            count.pop()
                    else:
                        if repc < c:
                            a = a - 1
                            for i in range(c - b):
                                if len(count)!=0:
                                    count.pop()
                        else:
                            print("did not reach end")
                            break

        if reached==1:
            return sum(count)
        else:
            return 0





if __name__ == '__main__':
    mat=[]
    u=int(input("enter no of rows  "))
    print("enter the matrix")
    for i in range(u):
        mat.append([int(x) for x in input("").split(" ")])
    print(collectMax(mat))

