import random

with open("two_powers.txt", 'w') as f:
    a=64
    count=1
    while(a>=1):
        sum=a
        while(sum<=64):
            f.write(f"g{count} {int(a)} {int(a)}\n")
            sum+=a
            count+=1
        a/=2