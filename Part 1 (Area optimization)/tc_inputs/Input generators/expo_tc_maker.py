import numpy as np

lambda_param = 1.5
samples = np.random.exponential(1/lambda_param, 200)
f=open("exponential_tc.txt","w")
c=0
for i in range(200):
    if int(samples[i]*100)==0 or int(samples[i]*100)>100:
        continue
    c+=1
    if c%2==0:
        f.write(f"g{c} {int(samples[i]*100)} {int(samples[i]*100)}\n")
    else:
        f.write(f"g{c} {int(samples[i]*100)} {int(samples[i]*100)}\n")
f.close()