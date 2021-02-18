FUEL=0
def getpath(s,d,path,cities_fuel,road,sumdist,fuel):
    global FUEL
    for c in cities_fuel:
        if c[0]==s and int(c[1])>0:
            fuel=FUEL
    for r in road:
        if r[0] not in path and s==r[1] and fuel>= int(r[2]):
            #path.append(r[0])
            #sumdist+=int(r[2])
            if d==r[0]:
                print (path+[s]+[d],sumdist+int(r[2]))
            else:
                getpath(r[0],d,path+[s],cities_fuel,road,sumdist+int(r[2]),fuel-int(r[2]))
        if r[1] not in path and s==r[0] and fuel>=int(r[2]):
           # path.append(r[1])
            #sumdist+=int(r[2])
            if d==r[1]:
                print (path+[s]+[d],sumdist+(int(r[2])))
            else:
                getpath(r[1],d,path+[s],cities_fuel,road,sumdist+int(r[2]),fuel-int(r[2]))

n= int(input())
cities_fuel=[]
for i in range(n):
    cities_fuel.append(input().split())
m=int(input())
road=[]
for i in range(m):
    road.append(input().split())

s,d=input().split()
FUEL=int(input()) # globaly declare
#print(cities,road,s,d)

sumdist=0
getpath(s,d,[],cities_fuel,road,sumdist,FUEL)
