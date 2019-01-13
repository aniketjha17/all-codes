# import copy
# n,m=map(int,input().split());s=[];r=[]
# a=list(map(int,input().split()))
# b=list(map(int,input().split()))
# x=copy.deepcopy(a)
# y=copy.deepcopy(b)
# x.sort();y.sort()
# p=[];q=[]
# for i in a:
#         c=x.index(i)
#         p.append(c)
# for i in b:
#         c=y.index(i)
#         q.append(c)
# for i in range(len(q)):
#         print(p[0],q[i])
# for i in range(1,len(p)):
#         print(p[i],q[-1])


# def f1(a,b):
#     x=np.argsort(a)
#     y=np.argsort(b)
    #print(x)
    #print(y)
#     for i in range(len(y)):
#         print(x[0],y[i])
#     for j in range(1,len(x)):
#         print(x[j],y[-1])

# import numpy as np
# n,m=map(int,input().split());s=[];r=[]
# a=list(map(int,input().split()))
# b=list(map(int,input().split()))
# f1(a,b)

def printPairs(arr, arr_size, sum): 
      
    # Create an empty hash set 
    s = set() 
      
    for i in range(0,arr_size): 
        temp = sum-arr[i] 
        if (temp>=0 and temp in s): 
            print ("Pair with the given sum is", arr[i], "and", temp) 
        s.add(arr[i]) 
  
# driver program to check the above function 
A = [1,6,45,8,10] 
n = 16
printPairs(A, len(A), n) 


# n,m=map(int,input().split());
# a=list(map(int,input().split()))
# b=list(map(int,input().split()))
# A=sorted(a)
# B=sorted(b)
# dict1=[]
# dict2=[]
# for i in range(len(A)):
#     for j in range(len(a)):
#         if(A[i]==a[j]):
#             dict1.append(j)
# for i in range((len(B))):
#     for j in range((len(b))):
#         if(B[i]==b[j]):
#             dict2.append(j)
# for i in range(len(dict2)):
#     print(dict1[0],dict2[i])
# for i in range(1,len(dict1)):
#     print(dict1[i],dict2[-1])


# def xor(n):
#     if(n%4==0):
#         return n
#     elif(n%4==1):
#         return 1
#     elif(n%4==2):
#         return n+1
#     return 0
# for _ in range(int(input())):
#     l,r=map(int,input().split())
#     if(l==r):
#         if(l%2==0):
#             print("Even")
#         else:
#             print("Odd")
#     else:
#         a=xor(l-1);b=xor(r)
#         result=(a ^ b)%2
#         if(result==0):
#             print("Even")
#         else:
#             print("Odd")

# for _ in range(int(input())):
#     n,m=map(int,input().split())
#     a=list(map(int,input().split()))
#     b=list(map(int,input().split()))
#     a1=set(a)
#     b1=set(b)
#     s=list(a1&b1)
#     print(len(s))

# for _ in range(int(input())):
#     num=int(input())
#     l=list(map(str,str(num)))
#     one=l.count('1');zero=l.count('0')
#     if(one==1 or zero==1):
#         print("Yes")
#     else:
#         print("No")

    
# for _ in range(int(input())):
#     l=input()
#     one=0;zero=0
#     for i in l:
#         if(i=='0'):
#             zero=zero+1
#         else:
#             one=one+1
#     if(one==1 or zero==1):
#         print("Yes")
#     else:
#         print("No")

