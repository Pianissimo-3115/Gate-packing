from objects import *
# import time
# import pdb
def algorithm(gates:list[Gate]):
    # 
    newlen=0
    visited=set()
    networks=[]
    for gate in gates:
        for pin in gate.pins:
            if pin not in visited:
                visited.add(pin)
                # if len(pin.connections)==0: continue
                newnet=Network()
                networks.append(newnet)
                pin.network=newnet
            for (_,newpin) in pin.connections:
                if newpin not in visited:
                    visited.add(newpin)
                    newpin.network=pin.network
    # 
    # pdb.set_trace()
    perimeter=set()
    answers={}
    answers[gates[0]]=(0,0)
    for i in range(gates[0].dimensions[1]):
        perimeter.add((0.5,i+0.5))
        perimeter.add((gates[0].dimensions[0]-0.5,i+0.5))
    for i in range(gates[0].dimensions[0]):
        perimeter.add((i+0.5,0.5))
        perimeter.add((i+0.5,gates[0].dimensions[1]-0.5))
    xrange=[0,gates[0].dimensions[0]]
    yrange=[0,gates[0].dimensions[1]]
    for pin in gates[0].pins:
        pin.network.addpin(pin,(pin.position[0],pin.position[1]))
    # 
    for gate in gates[1:]:
        if gate.id=='g1':
            # pdb.set_trace()
            pass
        minchange=float('inf')
        mincords=None
        startpt=(xrange[0]-gate.dimensions[0],yrange[0]-gate.dimensions[1])
        while (startpt[0]+gate.dimensions[0]+0.5,startpt[1]+gate.dimensions[1]+0.5) not in perimeter:
            startpt=(startpt[0],startpt[1]+1)
        move_dir=(0,1)
        beginning=True
        start=startpt

        # debug_count=0

        # pdb.set_trace()
        while True:
            # if gate.id=='g6' and move_dir==(1,0):
            #     pdb.set_trace()
            # debug_count+=1
            # if debug_count>100:
            #     print("ERROR")
                
            # 
            # time.sleep(0.2)
            change=0
            for pin in gate.pins:
                change+=pin.network.check_pin((startpt[0]+pin.position[0],startpt[1]+pin.position[1]))
            if change<minchange:
                minchange=change
                mincords=startpt



            if move_dir==(0,1):
                onee=False
                for i in range(gate.dimensions[1]):
                    if (startpt[0]+gate.dimensions[0]+0.5,startpt[1]+i+0.5) in perimeter:
                        onee=True
                        break
                if not onee and not beginning:
                    move_dir=(1,0)
                    beginning=True
                    continue
                else:
                    dirchange=False
                    for i in range(gate.dimensions[0]):
                        if (startpt[0]+i+0.5,startpt[1]+gate.dimensions[1]+0.5) in perimeter:
                            dirchange=True
                            break
                    if dirchange:
                        onee=False
                        for i in range(gate.dimensions[1]):
                            if (startpt[0]-0.5,startpt[1]+i+0.5) in perimeter:
                                onee=True
                            if onee:
                                break
                        if onee:
                            move_dir=(0,-1)
                            beginning=True
                        else:
                            move_dir=(-1,0)
                            beginning=True
                        continue
                    startpt=(startpt[0],startpt[1]+1)
                    beginning=False
                    if (startpt==start) or (minchange==0): break
                    continue
            
            elif move_dir==(0,-1):
                onee=False
                for i in range(gate.dimensions[1]):
                    if (startpt[0]-0.5,startpt[1]+i+0.5) in perimeter:
                        onee=True
                        break
                if not onee and not beginning:
                    move_dir=(-1,0)
                    beginning=True
                    continue
                else:
                    dirchange=False
                    for i in range(gate.dimensions[0]):
                        if (startpt[0]+i+0.5,startpt[1]-0.5) in perimeter:
                            dirchange=True
                            break
                    if dirchange:
                        twoo=False
                        for i in range(gate.dimensions[1]):
                            if (startpt[0]+gate.dimensions[0]+0.5,startpt[1]+i+0.5) in perimeter:
                                twoo=True
                            if twoo:
                                break
                        if twoo:
                            move_dir=(0,1)
                            beginning=True
                        else:
                            move_dir=(1,0)
                            beginning=True
                        continue
                    startpt=(startpt[0],startpt[1]-1)
                    beginning=False
                    if (startpt==start) or (minchange==0): break
                    continue

            elif move_dir==(1,0):
                onee=False
                for i in range(gate.dimensions[0]):
                    if (startpt[0]+i+0.5,startpt[1]-0.5) in perimeter:
                        onee=True
                        break
                if not onee and not beginning:
                    move_dir=(0,-1)
                    beginning=True
                    continue
                else:
                    dirchange=False
                    for i in range(gate.dimensions[1]):
                        if (startpt[0]+gate.dimensions[0]+0.5,startpt[1]+i+0.5) in perimeter:
                            dirchange=True
                            break
                    if dirchange:
                        twoo=False
                        for i in range(gate.dimensions[0]):
                            if (startpt[0]+i+0.5,startpt[1]+gate.dimensions[1]+0.5) in perimeter:
                                twoo=True
                            if twoo:
                                break
                        if twoo:
                            move_dir=(-1,0)
                            beginning=True
                        else:
                            move_dir=(0,1)
                            beginning=True
                        continue
                    startpt=(startpt[0]+1,startpt[1])
                    beginning=False
                    if (startpt==start) or (minchange==0): break
                    continue
            
            else:
                assert move_dir==(-1,0), ValueError("move_dir is not a valid value")
                onee=False
                for i in range(gate.dimensions[0]):
                    if (startpt[0]+i+0.5,startpt[1]+gate.dimensions[1]+0.5) in perimeter:
                        onee=True
                        break
                if not onee and not beginning:
                    move_dir=(0,1)
                    beginning=True
                    continue
                else:
                    dirchange=False
                    for i in range(gate.dimensions[1]):
                        if (startpt[0]-0.5,startpt[1]+i+0.5) in perimeter:
                            dirchange=True
                            break
                    if dirchange:
                        onee=False
                        for i in range(gate.dimensions[0]):
                            if (startpt[0]+i+0.5,startpt[1]-0.5) in perimeter:
                                onee=True
                            if onee:
                                break
                        if onee:
                            move_dir=(1,0)
                            beginning=True
                        else:
                            move_dir=(0,-1)
                            beginning=True
                        continue
                    startpt=(startpt[0]-1,startpt[1])
                    beginning=False
                    if (startpt==start) or (minchange==0): break
                    continue
        
        # print(perimeter)
        check=set()
        # pdb.set_trace()
        for j in range(gate.dimensions[1]):
            if (mincords[0]-0.5,mincords[1]+j+0.5) in perimeter:
                check.add((mincords[0]-0.5,mincords[1]+j+0.5))
            if (mincords[0]+gate.dimensions[0]+0.5,mincords[1]+j+0.5) in perimeter:
                check.add((mincords[0]+gate.dimensions[0]+0.5,mincords[1]+j+0.5))
        for j in range(gate.dimensions[0]):
            if (mincords[0]+j+0.5,mincords[1]-0.5) in perimeter:
                check.add((mincords[0]+j+0.5,mincords[1]))
            if (mincords[0]+j+0.5,mincords[1]+gate.dimensions[1]+0.5) in perimeter:
                check.add((mincords[0]+j+0.5,mincords[1]+gate.dimensions[1]))

        # print(check)
        for i in range(gate.dimensions[1]):
            if (mincords[0]-0.5,mincords[1]+i+0.5) in check:
                perimeter.remove((mincords[0]-0.5,mincords[1]+i+0.5))
            else:
                perimeter.add((mincords[0]+0.5,mincords[1]+i+0.5))
            if (mincords[0]+gate.dimensions[0]+0.5,mincords[1]+i+0.5) in check:
                perimeter.remove((mincords[0]+gate.dimensions[0]+0.5,mincords[1]+i+0.5))
            else:
                perimeter.add((mincords[0]+gate.dimensions[0]-0.5,mincords[1]+i+0.5))
        for i in range(gate.dimensions[0]):
            if (mincords[0]+i+0.5,mincords[1]-0.5) in check:
                perimeter.remove((mincords[0]+i+0.5,mincords[1]-0.5))
            else:
                perimeter.add((mincords[0]+i+0.5,mincords[1]+0.5))
            if (mincords[0]+i+0.5,mincords[1]+gate.dimensions[1]+0.5) in check:
                perimeter.remove((mincords[0]+i+0.5,mincords[1]+gate.dimensions[1]+0.5))
            else:
                perimeter.add((mincords[0]+i+0.5,mincords[1]+gate.dimensions[1]-0.5))
        
        if mincords[0]<xrange[0]:
            xrange[0]=mincords[0]
        if (mincords[0]+gate.dimensions[0])>xrange[1]:
            xrange[1]=mincords[0]+gate.dimensions[0]
        if mincords[1]<yrange[0]:
            yrange[0]=mincords[1]
        if (mincords[1]+gate.dimensions[1])>yrange[1]:
            yrange[1]=mincords[1]+gate.dimensions[1]
        answers[gate]=mincords
        for pin in gate.pins:
            pin.network.addpin(pin,(mincords[0]+pin.position[0],mincords[1]+pin.position[1]))
        wire_len=0
        for network in networks:
            wire_len+=network.wire_length
        newlen=wire_len
    # pdb.set_trace()
    return (normalized(answers),(xrange[1]-xrange[0]),(yrange[1]-yrange[0]),newlen)

def normalized(answers:dict[Gate,tuple[int,int]]):
    minx=float('inf')
    miny=float('inf')
    for val in answers.values():
        if val[0]<minx:
            minx=val[0]
        if val[1]<miny:
            miny=val[1]
    for key in answers:
        answers[key]=(answers[key][0]-minx,answers[key][1]-miny)
    return answers


