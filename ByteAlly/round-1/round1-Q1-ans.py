def getpath(s,d,path,road,sumdist):
    for r in road:
        if r[0] not in path and s==r[1]:
            if d==r[0]:
                print (path+[s]+[d],sumdist+int(r[2]))
            else:
                getpath(r[0],d,path+[s],road,sumdist+int(r[2]))
        if r[1] not in path and s==r[0]:
            if d==r[1]:
                print (path+[s]+[d],sumdist+(int(r[2])))
            else:
                getpath(r[1],d,path+[s],road,sumdist+int(r[2]))

n= int(input())
cities=[]
for i in range(n):
    cities.append(input())
m=int(input())
road=[]
for i in range(m):
    road.append(input().split())

s,d=input().split()

sumdist=0
getpath(s,d,[],road,sumdist)
