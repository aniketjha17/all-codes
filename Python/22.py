# def intreverse(n):
#     a=[]
#     while(n>0):
#         b=n%10
#         n=n//10
#         a.append(b)
#     c=[str(i) for i in a]
#     return (''.join(c))

# def descending(b):
#     flag=1
#     for i in range(len(b)):
#         if(i<=len(b)-2):
#             if(a[i]-a[i+1]>=0):
#                 flag=1
#             else:
#                 flag=0
#                 break
#     if(flag==1):
#         return True
#     else:
#         return False
    
# def valley(l):
#     change=0
#     if(len(l)==1):
#         return False
#     for i in range(len(l)-1):
#         if(l[i]>l[i+1]):
#             if(change==0):
#                 change=0
#             else:
#                 change=1
#         elif(l[i]==l[i+1]):
#             change=1
#             break
#         elif(l[i]<l[i+1]):
#             if(change==0):
#                 change=0
#             else:
#                 change=1
#     if(change==1):
#         return False
#     else:
#         return True
# a=[10,9,8]
# print(valley(a))



# def transpose(m):
#   result = [[m[j][i] for j in range(len(m))] for i in range(len(m[0]))]
#   return(result)

# a=[[21,33,11],[42,64,16]]
# print(transpose(a))'''

# '''t, k = [int(k) for k in input().split()]
# for i in range(t):
#     n = int(input())
#     a = [int(k) for k in input().split()]
#     if(sum(a) >= k):
#         print("FAILURE")
#     else:
#         print("SUCCESS")


# def f1(l1, l2):
#     count = 0
#     k = len(l1)
#     for i in range(k):
#         if(l1[i] != l2[i]):
#             count = count+1
#     p = (count/k)*100
#     return(p)

# n, l = [int(i) for i in input().split()]
# l = input()
# pe = []
# list1 = []
# for i in range(n):
#     list1.append(input())
#     s = f1(l, list1[i])
#     pe.append(s)
# m = pe.index(min(pe))
# print(list1[m])


# for _ in range(int(input())):
#     n=int(input())
#     a=[int(k) for k in input().split()]
#     a.sort()
#     count=0
#     for i in range(len(a)):
#         if(a[i]!=i+1):
#             count=count+1
#             a[i]=i+1
#     print(a)
#     print(count)


# for _ in range(int(input())):
#     n, k = map(int, input().split())
#     r = []
#     m = list(map(int,input().split()))
#     for i in range(n):
#         if(m[i] <= k):
#             a = 1
#             r.append(a)
#             k = k-m[i]
#         elif(m[i] > k):
#             a = 0
#             r.append(a) 
#     print(''.join(map(str, r)))




# f=0;lead=0
# c1=0;c2=0
# for _ in range(int(input())):
#     p1,p2=map(int,input().split())
#     c1=c1+p1
#     c2=c2+p2
#     if(c1>c2):
#         s=c1-c2
#         if(s>lead):
#             lead=s
#             f=1
#     elif(c2>c1):
#         s=c2-c1
#         if(s>lead):
#             lead=s
#             f=2
# print(f,lead)


# for _ in range(int(input())):
#     p=int(input())
#     l=[]
#     while(p>=2048):
#         p=p-2048
#         l.append(2048)
#     l.append(p)
#     #print(l)
#     c=0
#     for i in l:
#         s=str(bin(i))
#         c=c+s.count('1')
#     print(c)    
            

# for _ in range(int(input())):
#     n=int(input())
#     c=0
#     for i in range(n):
#         s,j=map(int,input().split())
#         if((j-s)>5):
#             c=c+1
#     print(c)


# while(1):
#     n=int(input())
#     if(n==0):
#         break
#     else:
#         l=[0]*n
#         a=list(map(int,input().split()))
#         for i in range(n):
#             l[a[i]-1]=i+1
#         print(l)
#         print(a)
#         if(l==a):
#             print("ambiguous")
#         else:
#             print("not ambiguous")
    
    
# def gcd(m,n):
#     while(m%n!=0):
#         r=m%n
#         m=n
#         n=r
#     return n 
# for _ in range(int(input())):
#     n=list(map(int,input().split()))
#     k=n[1]
#     for i in range(2,len(n)):
#         k=gcd(k,n[i])
#     if(k==1):
#         for i in range(1,len(n)):
#             print(n[i],end=" ")
#     else:
#         for i in range(1,len(n)):
#             print(n[i]//k,end=" ")    
#     print()


# def f1(l):
#     if(l==[]):
#         print("bye")
#         return 0
#     else:
#         print(l)
#         return(l[0]+f1(l[1:]))
# l=list(range(1,5))
# print(l)
# print(f1(l))


# def selectionSort(l,s,n):
#     if(s==n):
#         return
#     for i in range(s+1,len(l)):
#         if(l[s]>l[i]):
#             (l[s],l[i])=(l[i],l[s])
#     selectionSort(l,s+1,n)
# l=list(range(20,1,-1))
# selectionSort(l,0,len(l))
# print(l)



# l=list(range(50,1,-1))
# for i in range(len(l)):
#     pos=i
#     while(pos>0 and l[pos]<l[pos-1]):
#         (l[pos-1],l[pos])=(l[pos],l[pos-1])
#         pos=pos-1
# print(l)


# def insertionSortRecursive(arr,n): 
#     if n<=1: 
#         return
#     insertionSortRecursive(arr,n-1) 
#     last = arr[n-1] 
#     j = n-2
#     while (j>=0 and arr[j]>last): 
#         arr[j+1] = arr[j] 
#         j = j-1
#     arr[j+1]=last 
# arr = [12,11,13,5,6] 
# n = len(arr) 
# insertionSortRecursive(arr, n) 
# print(arr) 


# def merge(a,b):
#     (c,m,n)=([],len(a),len(b))
#     (i,j)=(0,0)
#     while(i+j<m+n):
#         if(i==m):
#             c.append(b[j])
#             j=j+1
#         elif(j==n):
#             c.append(a[i])
#             i=i+1
#         elif(a[i]<=b[j]):
#             c.append(a[i])
#         elif(a[i]>b[j]):
#             c.append(b[j])
#             j=j+1
#     return c
# def mergeshort(a,left,right):
#     if(right-left<=1):
#         return(a[left:right])
#     if(right-left>1):
#         mid=(left+right)//2
#         l=mergeshort(a,left,mid)
#         r=mergeshort(a,mid,right)
#         return(merge(l,r))
# l=list(range(20,1,-1))
# print(mergeshort(l,0,len(l)))


# def quickShort(a,l,r):
#     if(r-l<=1):
#         return()
#     yellow=l+1
#     for green in range(l+1,r):
#         if(a[green]<=a[l]):
#             (a[yellow],a[green])=(a[green],a[yellow])
#             yellow=yellow+1
#     (a[l],a[yellow-1])=(a[yellow-1],a[l])
#     quickShort(a,l,yellow-1)
#     quickShort(a,yellow,r)
# l=list(range(10,0,-1))
# print(l)
# quickShort(l,0,len(l))
# print(l)        


# def square(x):
#     return x*x
# def iseven(x):
#     return(x%2==0)
# a=list(map(square(iseven,range(100))))
# print(a)


# def f1(n):
#     return (n*(n+1)*(2*n+1)/6)
# for i in range(int(input())):
#     n=int(input())
#     print(int(f1(n)))
        
        
        
# def f1(n): 
#    return n*(n+1)*(2*n+1)/6 
# for i in range(int(input())):    
#     n=int(input())
#     if(n==1):
#         print(1)
#     else:
#         print(int(n*(n+1)*(2*n+1)/6)-1)



# for i in range(int(input())):
#     n=int(input())
#     s=input()
#     for i in range(len(s)):
#         if(i<=len(s)-1):
#             s[i]=s[len(s)-1]
#             s[i+1]=s[i]


# for i in range(int(input())):
#     m=int(input())
#     n=input()
#     print(n.count("1"))




# n=int(input())
# a=list(map(int,input().split()))
# for _ in range(int(input())):
#     flag=0
#     l,r,x=map(int,input().split())
#     if(r<=len(a)-1):
#         for i in range(l,r+1):
#             if(a[i]==x):
#                 flag=1
#                 break    
#         if(flag==1):
#             print("YES")
#         else:
#             print("NO")
#     else:
#         for i in range(l,len(a)):
#             if(a[i]==x):
#                 flag=1
#                 break
#         if(flag==1):
#             print("YES")
#         else:
#             print("NO")



# n=int(input())
# a=list(map(int,input().split()))
# a.sort(reverse=True)
# sum=0
# for i in range(n):
#     sum=sum+(2**i)*a[i]
# print(sum)




# def search(l1,r1,list):
#     l=0
#     r=len(list)-1
#     while l <= r: 
#         mid = l + (r - l)//2; 
#         if list[mid]>=l1 and list[mid]<=r1:
#             return 1 
#         elif list[mid] < l1: 
#             l = mid + 1
#         elif list[mid] > l1:
#             r = mid - 1
#     return 0
# n=int(input())
# s=input()
# q=int(input())
# l=list(map(int,s.split()))
# dict={}
# for i in range(0,len(l)):
#     if dict.get(l[i])==None:
#         dict[l[i]]=[]
#         dict[l[i]].append(i)
#     else:
#         dict[l[i]].append(i)
# for i in range(0,q):
#     s=input()
#     s=s.split()
#     p=0
#     l=int(s[0])
#     r=int(s[1])
#     x=int(s[2])
#     if dict.get(x)==None:
#         print("no")
#         continue
#     if search(l,r,dict[x]):
#         print("yes")
#     else:
#         print("no")

        

# for _ in range(int(input())):
#     p1,p2,k=map(int,input().split())
#     s=p1+p2
#     temp=s%k
#     if(temp!=0):
#         r=p1+p2-temp
#     else:
#         r=p1+p2
#     if((r/k)%2==0):
#         print("COOk")
#     else:
#         print("CHEF")

    

# def semi_prime(n):
#     c = 0
#     for i in range(2, n // 2 + 1):
#         if n % i == 0:
#             c = c + 1
#     if c == 2:
#         return 'NO'
#     else:
#         return 'YES'

# t = int(input())
# for i in range(t):
#     n = int(input())
#     print(semi_prime(n))


# def prime(q,i):
#     c1=0;c2=0
#     for k in range(1,q+1):
#         if(q%k==0):
#             c1=c1+1
#     for k in range(1,i+1):
#         if(i%k==0):
#             c2=c2+1
#     if(c1==c2==2):
#         return True
#     else:
#         return False

# def no_square(base, sqaure=2):
# 	square_base = int((base / sqaure) - 1)
# 	return int((square_base * (square_base+1))/2)

# for i in range(int(input())):
# 	no = int(input())
# 	print(no_square(no))

# import math
# for _ in range(int(input())):
#     a,b=map(int,input().split())
#     if(a>b):
#         num1=a
#         num2=b
#     else:
#         num1=b
#         num2=a
#     l=0;r=0
#     while(num1):
#         c1=num1%10
#         num1=num1//10
#         c2=num2%10
#         num2=num2//10
#         add=c1+c2
#         ans=add%10
#         r=ans*float(math.pow(10,l))+r
#         add=0
#         l=l+1
#         if(num2==0):
#             break
#     num1=num1*10**l
#     print(int(num1+r))



# for i in range(int(input())):
#     n,m,k=map(int,input().split())
#     s=min(n,m)
#     a=max(n,m)
#     for i in range(k):
#         if(s==a):
#             break
#         s=s+1        
#     print(a-s)

# for i in range(int(input())):
#     s1=input()
#     s2=input()
#     flag=0
#     for i in range(len(s1)):
#         if(s1[i]==s2[i] or (s1[i]!=s2[i] and (s1[i]=='?'or s2[i]=='?'))):
#             flag=flag+1
#         else:
#             flag=0
#     if(flag==len(s1)):
#         print("Yes")
#     else:
#         print("No")




# for _ in range(int(input())):
#     m,x,y=map(int,input().split())
#     a=list(map(int,input().split()))
#     s=x*y;c=[0]*100000
#     for i in range(len(a)):
#         temp=a[i]-s
#         l2=temp+(2*s)
#         if(temp<0):
#             temp=1
#         for j in range(temp,l2+1):
#             c[j]=0
#     count=0
#     for i in range(1,101):
#         if(c[i]!=0):
#             count=count+1
#     print(count)

# for i in range(int(input())):
#     n=int(input())
#     a=list(map(int,input().split()))
#     s=min(a)
#     print(s*(len(a)-1))


# for _ in range(int(input())):
#     s=input()
#     a=list(set(s))
#     c=[]
#     for i in range(len(a)):
#         c.append(s.count(a[i]))
#     if(2*max(c)==len(s)):
#         print("YES")
#     else:
#         print("NO")

# for _ in range(int(input())):
#     n=int(input())
#     l=[]
#     for i in range(n):
#         a=int(input())
#         l.append(a)
#     l.sort()
#     c=list(set(l))
#     for i in range(len(l)):
#         s=l.count(c[i])
#         if(s%2!=0):
#             print(c[i])
#             break


# for _ in range(int(input())):
#     n=int(input())
#     c=1;s=n
#     for i in range(1,n+1):
#         s=s-c
#         if(s>c):
#             c=c+1
#         else:
#             break
#     print(c)

# import math
# for _ in range(int(input())):
#     n,m=map(int,input().split())
#     g=math.gcd(m,n)
#     print((m*n)//(g))


# for _ in range(int(input())):
#     n,m,k=map(int,input().split())
#     a=set(map(int,input().split()))
#     b=set(map(int,input().split()))
#     print(len(list(a&b)),n-len(list(a|b)))
    
# for _ in range(int(input())):
#     x1,y1,x2,y2=map(int,input().split())
#     x=x2-x1
#     y=y2-y1
#     if(x!=0 and y!=0):
#         print("sad")
#     else:
#         if(x>0):
#             print("right")
#         elif(x<0):
#             print("left")
#         elif(y>0):
#             print("up")
#         elif(y<0):
#             print("down") 

# for _ in range(int(input())):
#     n=int(input())
#     count=0
#     a=list(map(int,input().split()))
#     b=list(map(int,input().split()))
#     if(a[0]>=b[0]):
#         count=count+1
#     for i in range(1,len(a)):
#         if(a[i]-a[i-1]>=b[i]):
#             count=count+1
#     print(count)

# for _ in range(int(input())):
#     n=int(input())
#     print(n*(n**2+1)//2)    


# def prime(n):
#     count=0
#     for i in range(1,n//2):
#         if(n%i==0):
#             count=count+1
#     if(count==1):
#         return True
#     else:
#         return False
# for _ in range(int(input())):
#     l,r=map(int,input().split())
#     sum=0
#     for j in range(l,r+1):
#         for k in range(1,j+1):
#             if(j%k==0):
#                 if(prime(k)):
#                     sum=sum+k
#     print(sum)
# for i in range(5):
#     n=int(input())
#     print(prime(n))

# def prime(n):
#     s=True
#     count=0
#     for i in range(2,n//2+1):
#         if(n%i==0):
#             s=False
#             break
#     if(s):
#         return True
#     else:
#         return False
# for _ in range(int(input())):
#     l,r=map(int,input().split())
#     sum=0
#     for j in range(l,r+1):
#         for k in range(2,j+1):
#             if(j%k==0):
#                 if(prime(k)):
#                     sum=sum+k
#     print(sum)

# l=[]
# for _ in range(int(input())):
#     n=int(input())
#     l.append(n)
# l.sort()
# c=len(l)
# s=[]
# for i in range(len(l)):
#    s.append(l[i]*c)
#    c=c-1
# print(max(s)) 


# n=int(input())
# a=list(map(int,input().split()))
# sum=0
# for i in range(len(a)):
#     for j in range(i,len(a)):
#         sum=sum+abs(a[i]-a[j])
# print(sum)



      
for i in range(int(input())):
        a=list(map(str,input().split()))
        if("not" not in a):
                print("regularly fancy")
        else:
                print("Real Fancy")

