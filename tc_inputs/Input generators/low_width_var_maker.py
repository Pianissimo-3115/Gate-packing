import random
with open("low_width_variance.txt",'w') as f:
    for i in range(500):
        f.write(f"g{i+1} {random.randint(20,25)} {random.randint(1,100)}\n")