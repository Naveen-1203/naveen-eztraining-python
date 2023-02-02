n=int(input("Enter the size:"))

L=[]

for i in range(n):
    ele=int(input("Element:"))
    L.append(ele)

print(L)

for j in L:
    if(j%2==0):
        print(j)
        

n=int(input("Enter the size:"))
product=1
sumof=0
L=[]

for i in range(n):
    ele=int(input("Element:"))
    L.append(ele)
for j in L:
    product=product*j
for k in L:
    sumof=sumof+k
if(product<750):
    print("prod  ",product)
else:
    print("sum  ",sumof)


L=list(map(int,input("Numbers:").split()))
product=1
sumof=0
for i in L:
    product=product*i
for j in L:
    sumof=sumof+j
if(product<750):
    print("prod  ",product)
else:
    print("sum  ",sumof)


numbers=[elements for elements in "Great Afternoon"]
print(numbers)



L=["hyd","vijaywada","chennai","vizag"]
city=[]
for n in L:
    if "v" in n:
        city.append(n)
print(city)




L1=[2**x for x in range(2,10)]
print(L1)




L2=[a for a in range(100,201,20)]
print(L2)





L3=[1,2,3,4,5,6]
L4=[i for i in L3 if(i<6)]
print(L4)



L=[1,3,5,7,9,11,2.3,5.8,"Aki","Akki"]
print(L[0])
print(L[1])
print(L[2])
print(L[3])
print(L[4])
print(L[5])
print(L[6])
print(L[7])
print(L[8])
print(L[9])


L=[1.2,3.5,5.6,2.8,7.1]
count=0
for i in L:
    count=count+i
Average=((count)/5)
print(count)
print(Average)

