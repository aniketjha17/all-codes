# def f1(l,n,c):
#     sum=0
#     if(c==n):
#         return 0
#     else:
#         for i in range(c,n):
#             sum=sum+l[i]-l[c]
#     return sum+f1(l,n,c+1)

# n=int(input())
# l=list(map(int,input().split()))
# l.sort()
# total=sum(l)
# s=[]
# for i in range(n):
#     s.append(total-l[i])
#     total=total-l[i]
# r=0
# for i in range(n):
#     r=abs((l[i]*(n-i-1))-s[i])
#     print(r)    

# for _ in range(int(input())):
#     k,n=map(int,input().split())
#     h=list(map(int,input().split()))
#     h.insert(0,0)
#     c=0;r=0
#     for i in range(k):
#         if(True):
#             diff=h[i+1]-h[i]
#             #print(diff,end=" ")
#             if(diff>n):
#                 r=r+diff//n
#                 #print(r,end=" ")
#                 if(h[i]+n*(diff//n)==h[i+1]):
#                     r=r-1
#     print(r)


# t = int(input())
# for _ in range(t):
#     n, k = map(int, input().split())
#     h = [int(i) for i in input().split()]
#     h.insert(0, 0)
#     min_stairs = 0
#     for i in range(n):
#         min_stairs += ((h[i+1] - h[i] - 1)//k)
#     print(min_stairs)

# import math
# for _ in range(int(input())):
#     a,d=map(int,input().split())
#     m,n,p=map(int,input().split())
#     if(((math.sqrt(m**2+n**2))*p+d)<=a):
#         print("Possible")
#     else:
#         print("Impossible")

# for _ in range(int(input())):
#     n,k=map(int,input().split())
#     p=list(map(str,input().split()))
#     m=[]
#     for i in range(k):
#         m1=list(map(str,input().split()))
#         m.extend(m1)
#     re=[]
#     for i in p:
#         if(i in m):
#             re.append("YES")
#         else:
#             re.append("NO")
#     print(*re)


# for _ in range(int(input())):
#     ls=int(input())
#     s=list(map(int,input().split()))
#     lf=int(input())
#     f=list(map(int,input().split()))
#     c=0
#     for i in range(lf):
#         for j in range(ls):
#             if(f[i]==s[j]):
#                 c=c+1
#                 break
#     if(c==lf):
#         print("YES")
#     else:
#         print("NO")

# for _ in range(int(input())):
#     tr=int(input())
#     r=list(map(int,input().split()))
#     tempr=list(set(r))

#     dr=int(input())
#     d=list(map(int,input().split()))
#     tempd=list(set(d))

#     dr=int(input())
#     ds=list(map(int,input().split()))
#     tempds=list(set(ds))

#     ad=int(input())
#     sd=list(map(int,input().split()))
#     tempsd=list(set(sd))
    
#     for i in ds:
#         if(i in r):
#             c=0
#         else:
#             c=1
#     for i in sd:
#         if(i in d):
#             c=0
#         else:
#             c=1
#     if(c==0):
#         print("yes")
#     else:
#         print("no")

# n,m=map(int,input().split());s=[]
# a=list(map(int,input().split()))
# b=list(map(int,input().split()))
# if(len(a)<len(b)):
        
# for i in range(max(n,m)):
#     for j in range(0,(min(n,m))):
#         s.append(a[i]+b[j])
# print(s)
