from objects import *
from critical_path import *    
from algo import *
from exception import LoopException

def comp(start_gate:Gate, visited):
    queue = Queue()
    queue.enqueue(start_gate)
    component = []
    visited.add(start_gate)

    while not queue.is_empty():
        gate = queue.dequeue()
        component.append(gate)

        for neighbor_ in gate.input_connections + gate.output_connections:
            neighbor=neighbor_[0]
            if neighbor not in visited:
                visited.add(neighbor)
                queue.enqueue(neighbor)

    return component

def find_connected_components(gates):
    visited = set()
    connected_components = []
    
    for gate in gates:
        if gate not in visited:
            component = comp(gate, visited)
            connected_components.append(component)
    
    return connected_components


def solve(input,output):
    answers={}
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
        delay=int(gate[3])
        newgate=Gate(gate[0],width,height,delay,pins=pinlist)
        for j in range(2,len(pins),2):
            newgate.pins.append(Pin(j//2,int(pins[j]),int(pins[j+1]),gate=newgate,connections=[]))
        gates.append(newgate)
    # pdb.set_trace()
    wire_delay=int(b[y].split(" ")[1])
    for j in range(y+1,len(b)):
        a=b[j].split(" ")
        first=a[1].split(".")
        second=a[2].split(".")
        gate1:Gate=gates[int(first[0][1:])-1]
        gate2:Gate=gates[int(second[0][1:])-1]
        pin1:Pin=gate1.pins[int(first[1][1:])-1]
        pin2:Pin=gate2.pins[int(second[1][1:])-1]
        pin1.connections.append((gate2,gate2.pins[int(second[1][1:])-1]))
        pin2.connections.append((gate1,gate1.pins[int(first[1][1:])-1]))
        if pin1.position[0]==0:
            pin1.type="secondary_input"
        else:
            pin1.type="secondary_output"
        if pin2.position[0]==0:
            pin2.type="secondary_input"
        else:
            pin2.type="secondary_output"
        # pdb.set_trace()
        if pin1.position[0]==0:
            gate1.input_connections.append((gate2,pin2))
        else:
            gate1.output_connections.append((gate2,pin2))
        if pin2.position[0]==0:
            gate2.input_connections.append((gate1,pin1))
        else:
            gate2.output_connections.append((gate1,pin1))
    
    for gate in gates:
        for pin in gate.pins:
            if pin.type is None:
                if pin.position[0]==0:
                    pin.type="primary_input"
                else:
                    pin.type="primary_output"

    visited=set()
    networks=[]
    for gate in gates:
        for pin in gate.pins:
            if pin not in visited:
                visited.add(pin)
                newnet=Network()
                networks.append(newnet)
                pin.network=newnet
                for connection in pin.connections:
                    if connection[1] not in visited:
                        visited.add(connection[1])
                        connection[1].network=newnet

    connected_components = find_connected_components(gates)
    answers={}
    prevx,prevy=1,1
    for gate in gates:
        for neighbor in gate.input_connections+gate.output_connections:
            gate.neighboring_delay+=neighbor[0].delay

    for component in connected_components:
        # component.sort(key=lambda gate: (len(gate.input_connections)+len(gate.output_connections)))
        component.sort(key=lambda gate:(gate.neighboring_delay),reverse=True)
        visited=set()
        newlist=[component[0]]
        visited.add(component[0])
        queue=Queue()
        queue.enqueue(component[0])
        while queue.is_empty()==False:
            gate=queue.dequeue()
            for connection in gate.input_connections+gate.output_connections:
                if connection[0] not in visited:
                    visited.add(connection[0])
                    newlist.append(connection[0])
                    queue.enqueue(connection[0])
        

        ans=algorithm(newlist)
        for key in ans[0]:
            answers[key]=(ans[0][key][0]+prevx,ans[0][key][1]+prevy)
        prevx+=ans[1]
        prevy+=ans[2]
        

    crit_path=0
    pinpath=None
    isloop=True
    dp={}
    for gate in gates:
        if len(gate.input_connections)==0:
            isloop=False
            visited=set()
            temp=critical_path(gate,wire_delay,dp)
            if temp[0]>crit_path:
                crit_path=temp[0]
                pinpath=temp[1]
    if isloop:
            raise LoopException("Given gates contain an infinite loop")
    # print(crit_path)
    # pinpath.reverse()
    # print(pinpath)
    firstgate:Gate=pinpath[0][0].gate
    inputpin=None
    for pin in firstgate.pins:
        if pin.type=="primary_input":
            inputpin=pin
            break
    outputpin_path=[inputpin]
    for pinpair in pinpath:
        if outputpin_path[-1]!=pinpair[0]:
            outputpin_path.append(pinpair[0])
        outputpin_path.append(pinpair[1])

    lastgate=outputpin_path[-1].gate
    outputpin=None
    for pin in lastgate.pins:
        if pin.type=="primary_output":
            outputpin=pin
            break
    outputpin_path.append(outputpin)
    # print(outputpin_path)
    path=' '.join(map(str,outputpin_path))
    print(crit_path)
    with open(output,'w') as f:
        f.write(f"bounding_box {prevx} {prevy}\n")
        f.write(f"critical_path_delay {crit_path}\n")
        f.write(f"critical_path {path}\n")
        for key in answers.keys():
            f.write(f"{key} {answers[key][0]} {answers[key][1]}\n")


solve("input.txt","output.txt")