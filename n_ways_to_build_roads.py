"""Write a function that receives an array of roads connecting cities and 
return the no. of ways in which 3 hotels can be constructed keeping in mind 
that the distance between the 3 hotels must be the same"""

import math

def nCr(n,r):
    f=math.factorial
    return int(f(n)/f(r)/f(n-r))

def path(arr,city,accumulator=None):
    if accumulator is None:
        accumulator=[]
    if len(arr)==0:
        return [accumulator]
    else:
        return [l for x in arr for l in path([y 
                                              for y in city[x] if y not in accumulator+[x]],
                                             accumulator+[x])]
def ways(roads):
    cities=dict()
    for row in roads:
        for city in row:
            temp=row.copy()
            temp.pop(temp.index(city))
            try:
                cities[city]+=temp
            except:
                cities[city]=temp

    nodes={}
    for node in path([x for x in cities.keys() if len(cities[x])>2],cities):
            try:
                nodes[node[0]]+=[node[1:]]
            except:
                nodes[node[0]]=[node[1:]]

    for val in nodes.items():
        temp={}
        for row in val[1]:
            for i in range(len(row)):
                try:
                    temp[i+1]+=[row[i]]
                except:
                    temp[i+1]=[row[i]]
        nodes[val[0]]=list(map(lambda x:len(x),temp.values()))
        del temp

    return sum([nCr(n,3) for row in nodes.values() for n in row if n>2])