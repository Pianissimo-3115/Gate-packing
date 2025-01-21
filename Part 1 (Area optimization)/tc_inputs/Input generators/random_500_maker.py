import random

with open("random_500.txt", 'w') as f:
    for i in range(500):
        f.write(f"g{i+1} {random.randint(1,100)} {random.randint(1,100)}\n")