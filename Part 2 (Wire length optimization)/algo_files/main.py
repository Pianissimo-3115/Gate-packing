from algo import algorithm
from objects import *
import pdb


from collections import deque

def FindClusters(gates: list[Gate]) -> list[list[Gate]]:
    clusters = []
    visited = set()

    for gate in gates:
        if gate not in visited:
            cluster = [gate]
            visited.add(gate)
            queue = deque([gate])

            while queue:
                current_gate = queue.popleft()
                for connection in current_gate.connections:
                    if connection not in visited:
                        cluster.append(connection)
                        visited.add(connection)
                        queue.append(connection)
            clusters.append(cluster)
    
    return clusters


def solve(input,output):
    answers={}
    wire_length=0
    gates:list[Gate]=[]

    with open(input,'r') as f:
        b=f.readlines()

    y=-1

    for i in range(len(b)):
        b[i]=b[i].strip()

    for i in range(0,len(b),2):
        if b[i][:4]=="wire":
            y=i
            break
        pinlist=[]
        gate=b[i].split()
        pins=b[i+1].split()
        width=int(gate[1])
        height=int(gate[2])
        newgate=Gate(gate[0],width,height,pins=pinlist)
        for j in range(2,len(pins),2):
            newgate.pins.append(Pin(j//2,int(pins[j]),int(pins[j+1]),gate=newgate,connections=[]))
        gates.append(newgate)
    # pdb.set_trace()
    for j in range(y,len(b)):
        a=b[j].split(" ")
        first=a[1].split(".")
        second=a[2].split(".")
        gate1=gates[int(first[0][1:])-1]
        gate2=gates[int(second[0][1:])-1]
        gate1.pins[int(first[1][1:])-1].connections.append((gate2,gate2.pins[int(second[1][1:])-1]))
        gate2.pins[int(second[1][1:])-1].connections.append((gate1,gate1.pins[int(first[1][1:])-1]))
        # pdb.set_trace()
        gate1.connections.add(gate2)
        gate2.connections.add(gate1)
    # for gate in gates:
        # print(len(gate.connections))
    clusters=FindClusters(gates)
    prevx,prevy=1,1
    # print(clusters)
    for i in range(len(clusters)):
        cluster=clusters[i]
        assert isinstance(cluster,list)
        cluster.sort(key=lambda gate:(len(gate.connections),(gate.dimensions[0]*gate.dimensions[1])),reverse=True)
        # pdb.set_trace()
        # print([(gate.id,len(gate.connections)) for gate in cluster])
        visited=set()
        newlist=[cluster[0]]
        visited.add(cluster[0])
        queue=deque([cluster[0]])
        while queue:
            current_gate=queue.popleft()
            for connection in current_gate.connections:
                if connection not in visited:
                    newlist.append(connection)
                    visited.add(connection)
                    queue.append(connection)
        assert len(newlist)==len(cluster), ValueError("Cluster not connected")
        # print(newlist)
        (ans,xrange,yrange,wire_leng)=algorithm(newlist)
        # print(newlist)
        # print("done")
        assert isinstance(ans,dict)
        assert isinstance(xrange,int)
        assert isinstance(yrange,int)
        assert isinstance(wire_leng,int)
        wire_length+=wire_leng
        for key in ans:
            answers[key]=(ans[key][0]+prevx,ans[key][1]+prevy)
        prevx+=xrange+1
        prevy+=yrange+1
    with open(output,'w') as f:
        f.write(f"bounding_box {prevx-1} {prevy-1}\n")
        for gate in answers:
            f.write(f"{gate.id} {answers[gate][0]} {answers[gate][1]}\n")
        f.write(f"wire_length {wire_length}\n")
import time
a=time.perf_counter()
solve("inputnew.txt","output.txt")
print(time.perf_counter()-a)