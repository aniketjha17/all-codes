x=[int(k) for k in input("input the value of x in ascending order ").split()]
y=[int(j) for j in input("input the value of y order ").split()]
num=float(input("enter the required number "))
count=0
for i in range(len(x)):
    if(i==(len(x)-1)):
        break;
    count=count+1 
    if(num>x[i] and num<x[i+1]):
            s=count  
#print(x[s-1],x[s])
#print(y[s-1],y[s])
ans=y[s-1]+(y[s]-y[s-1])/(x[s]-x[s-1])*(num-x[s-1])
#print(y[s]-y[s-1],x[s]-x[s-1],num-x[s-1])
print("The pridicted value is ",ans)
            
        


        
