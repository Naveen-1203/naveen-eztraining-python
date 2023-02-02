d={n:n*n for n in range(1,5)}
print(d)

#CALCULATING PRODUCT PRICE for 5 units
old={'rice':60,'dhaal':120,'oil':150}
new={product:price*5 for (product,price)in
     old.items()}
print(new)

#with checks
real={'sam':24,'angel':18,'kumar':35}
now={name:age for (name,age) in real.items()
     if age>20}
print(now)

import random
cust=["sam","smith","nila"]
cust_dict={names:random.randint(1,100) for names in cust}
print(cust_dict)

L1=['a','b','c']
L2=[1,2,3]
d={a:b for (a,b) in zip(L1,L2)}
print(d)

import random
student_names=list(map(str,input("Enter names : ")))
marks=[]
for i in range(len(student_names)):
    a=(random.randint(300,500)/500)*100
    marks.append(a)
my_dict={x:y for (x,y) in zip(student_names,marks)}
print(my_dict)


def isPalin'drome(s):
	return s == s[::-1]

s = "malayalam"
ans = isPalindrome(s)

if ans:
	print("Yes")
else:
	print("No")

s=input("sring:")
ch=input("chrt:")
if ch in s:
    print("present")
else:
    print("not present")

s=input("enter:")
char=input()
for i in s:
     if i==char:
         flag=1
         break
else:
        flag=0
if flag==1:
    print("present")
else:
    print("not present")

st=input("enter the string:")
char=input("enter req char:")
a="yes" if char in st else no

s=input("enter a string:")
count=0
for i in range(len(s)):
    if s[i]==" ":
        count+=1
        break
print(count)


#Math module
import math
print( "CEIL 12.5:",math.ceil(12.5))
print("FLOOR 12.5:",math.floor(12.5))
print("SQRT 345:",math.sqrt(345))
print("Factoral 3:",math.factoral(3))
print("power" 2,3:",math.pow(2,3))
print("Remainder 10,3:",math.fmod(10,3))
a,b=divmod(10,3)
print(a,b)

 
    



    

