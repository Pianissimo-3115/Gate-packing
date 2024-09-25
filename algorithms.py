# import pdb
# import time
import math


"""
EXAMPLE USAGE:
tetrisalgo("input.txt","output.txt")

and

sleator("input.txt","output.txt")

(this will write (or rewrite) the file output.txt as per the given requirement, taking input.txt 
    according to format mentioned in assignment instructions)
"""
def tetrisalgo(input_file,output_file):


    def new(wlim,gates:list):
        heights=[0]*wlim
        ans={}
        temp1=len(gates)
        h=0
        for i in range(len(gates)):
            if(gates[i][1][0]>wlim/2):
                temp1=i
                break
        for i in range(len(gates)-1,temp1-1,-1):
            ans[gates[i][0]]=(wlim-gates[i][1][0],h)
            h+=gates[i][1][1]
            for w in range(ans[gates[i][0]][0],wlim):
                heights[w]=h
        if(temp1==0):
            return ans,h
        gates=gates[:temp1]
        gates=sorted(gates,key= lambda x:x[1][1], reverse=True)
        a=True
        levels=[]
        temp=[]
        x=0
        # a=True means we're going from left to right
        for i in range(temp1):
            if((not a and x<gates[i][1][0]) or (a and x+gates[i][1][0]>wlim)):
                a=not a
                if a:
                    levels.append(temp[::-1])
                    x=0
                else:
                    levels.append(temp)
                    x=wlim
                temp=[]
            if(a):
                temp.append((i,x))
                x+=gates[i][1][0]
            else:
                x-=gates[i][1][0]
                temp.append((i,x))
        if a:
            levels.append(temp[::-1])
        else:
            levels.append(temp)
        for i in levels:
            for j in i:
                h=max([heights[w] for w in range(j[1],j[1]+gates[j[0]][1][0])])
                ans[gates[j[0]][0]]=(j[1],h)
                for w in range(j[1],j[1]+gates[j[0]][1][0]): 
                    heights[w]=gates[j[0]][1][1]+h
        maxh=max(heights)
        return ans,maxh
    
    
    
    def direct(wlim,gates:list):
        heights=[0]*wlim
        ans={}
        h=0
        a=True
        levels=[]
        temp=[]
        x=0
        for i in range(len(gates)):
            if((not a and x<gates[i][1][0]) or (a and x+gates[i][1][0]>wlim)):
                a=not a
                if a:
                    levels.append(temp[::-1])
                    x=0
                else:
                    levels.append(temp)
                    x=wlim
                temp=[]
            if(a):
                temp.append((i,x))
                x+=gates[i][1][0]
            else:
                x-=gates[i][1][0]
                temp.append((i,x))
        if a:
            levels.append(temp[::-1])
        else:
            levels.append(temp)

        for i in levels:
            for j in i:
                h=max([heights[w] for w in range(j[1],min(j[1]+gates[j[0]][1][0],wlim))])
                ans[gates[j[0]][0]]=(j[1],h)
                for w in range(j[1],min(j[1]+gates[j[0]][1][0],wlim)): 
                    heights[w]=gates[j[0]][1][1]+h
        maxh=max(heights)
        return ans,maxh

    with open(input_file, 'r') as f:
        a=f.readlines()
    # x=time.perf_counter()
    gatees=[]
    minw=-1
    maxw=0
    totarea=0
    for i in a:
        i=i.split()
        gatees.append([i[0],tuple((int(i[1]),int(i[2])))])
        minw=max(minw,int(i[1]))
        maxw+=int(i[1])
        totarea+=int(i[1])*int(i[2])
    gates=sorted(gatees,key=lambda x:x[1][0])   #Sorted by width (increasing order)
    aa={}
    # x=time.perf_counter()
    minans1=-1
    minind1=-1
    # xes=[]
    # yes=[]
    if(len(gatees)>100):
        side=math.sqrt(totarea)
        minw=max(int(2*side/3),minw)
        maxw=min(maxw,int(4*side/3))
    for i in range(minw,maxw+1):
        a,b=new(i,gates)
        # xes.append(i)
        # yes.append(b*i)
        if b*i<minans1 or minans1==-1:
            minans1=b*i
            minind1=i
            aa=a
    cords1=aa
    # y=time.perf_counter()
    gates=sorted(gatees,key=lambda x:x[1][1], reverse=True)
    minans2=-1
    minind2=-1
    # xes=[]
    # yes=[]
    for i in range(minw,maxw+1):
        a,b=direct(i,gates)
        # xes.append(i)
        # yes.append(b*i)
        if b*i<minans2 or minans2==-1:
            minans2=b*i
            minind2=i
            aa=a
    cords2=aa
    # z=time.perf_counter()
    # print(y-x,z-y)
    with open(output_file,'w') as f:
        if(minans1<minans2):
            f.write(f"bounding_box {minind1} {int(minans1/minind1)}\n")
            for i in cords1:
                f.write(f"{i} {cords1[i][0]} {cords1[i][1]}\n")
        else:
            f.write(f"bounding_box {minind2} {int(minans2/minind2)}\n")
            for i in cords2:
                f.write(f"{i} {cords2[i][0]} {cords2[i][1]}\n")
    
def sleator(input_file, output_file):
    with open(input_file) as f:
        rectangles = []
        total_width = 0
        max_width = 0
        lines = f.readlines()
        for line in lines:
            parts = line.split()
            width = int(parts[1])
            height = int(parts[2])
            label = parts[0]
            rectangles.append([height, width, label])
            total_width += width
            max_width = max(max_width, width)

    min_area = float('inf')
    best_width = 0
    best_height = 0
    best_placement = {}

    for width in range(max_width, total_width + 1):
        placement = {}
        h = 0
        wmax = 0
        for rect in rectangles:
            if rect[1] > width // 2:
                placement[rect[2]] = [0, h]
                wmax = max(wmax, rect[1])
                h += rect[0]

        m = [rect for rect in rectangles if rect[1] <= width // 2]
        h1, h2 = h, h
        m.sort(reverse=True)
        f1 = 0
        j = 0
        while j < len(m):
            if h1 <= h2:
                flag = m[j][0]
                w1 = 0
                while j < len(m) and m[j][1] + w1 <= width // 2:
                    placement[m[j][2]] = [w1, h1]
                    w1 += m[j][1]
                    j += 1
                h1 += flag
            else:
                flag = m[j][0]
                if f1 != 0:
                    w1 = width // 2
                f1 = 1
                while j < len(m) and m[j][1] + w1 <= width:
                    placement[m[j][2]] = [w1, h2]
                    wmax = max(wmax, w1 + m[j][1])
                    w1 += m[j][1]
                    j += 1
                h2 += flag

        h = max(h1, h2)
        area = h * wmax
        if area < min_area:
            min_area = area
            best_width = wmax
            best_height = h
            best_placement = placement

    with open(output_file, 'w') as f:
        f.write(f"bounding_box {best_width} {best_height}\n")
        for label, coords in best_placement.items():
            f.write(f"{label} {coords[0]} {coords[1]}\n")

sleator(r"sample_test_case_3-20240814\input.txt","test.txt")