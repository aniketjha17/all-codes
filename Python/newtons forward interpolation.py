import numpy as np
def u_cal(u,n):
    temp = u
    for i in range(1,n):
        temp=temp*(u-i)
    return temp
def fact (n):
    f=1
    for i in range (2,n+1):
        f=f*i
    return f
n= 18
x=[i for i in range(0,120,7)]
dupy=[-0.11,0.1,0.01,0.06,0.04,-0.26,0.04,0.19,-0.22,-0.2,0.12,0.21,-0.26,-0.3,0.22,0.58,-0.36,0.13]
y=np.zeros((n,n), dtype=float)
for i in range(n):
    y[i][0]=dupy[i]
for i in range (1,n):
    for j in range(n-i):
        y[j][i] = y[j + 1][i - 1] - y[j][i - 1];
for i in range(n):
    print(x[i], end=' ')
    for j in range(n):
        print(y[i][j],end=' ')
    print('\n')
value=int(input())
sum=y[0][0]
u=(value-x[0])/(x[1]-x[0])
for i in range(1,n):
    sum=sum+(u_cal(u,i)*y[0][i])/fact(i)
print(sum)
