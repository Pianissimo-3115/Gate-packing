with open("inputnew.txt",'w') as f:
    f.write(f"g1 10 10\n")
    f.write(f"pins g1 10 5\n")
    for i in range(2,50):
        f.write(f"g{i} 10 10\n")
        f.write(f"pins g{i} 0 5 10 5\n")
    f.write(f"g50 10 10\n")
    f.write(f"pins g50 0 5\n")
    f.write(f"wire g1.p1 g2.p1\n")
    for i in range(2,50):
        f.write(f"wire g{i}.p2 g{i+1}.p1\n")