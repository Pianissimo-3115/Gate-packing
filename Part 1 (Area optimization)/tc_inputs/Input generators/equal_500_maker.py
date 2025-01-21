import random

with open("equal_500.txt", 'w') as f:
    for i in range(500):
        f.write(f"g{i+1} 47 47\n")