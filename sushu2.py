from math import sqrt
j=2
while j<=100:
    i=2
    k=sqrt(j)
    while(i<=k):
        if j%i==0:break
        i=i+1
    if(i>k):
        print(j),
    j=j+1