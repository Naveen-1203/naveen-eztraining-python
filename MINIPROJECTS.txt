#PROJECT-1-QUIZ GAME
q1="""Who is your fav. Crush?
a.Priya
b.Anushka
c.Rashmika
d.samantha"""

q2="""What is your fav. sport?
a.badminton
b.kabaddi
c.cricket
d.khokho
"""

q3="""Who is your fav. character?
a.IronMan
b.Thor
C.Spiderman
d.Aquaman
"""

q4="""What is your fav. Bike?
a.Duke 390
b.Benelli900i
c.Kawasaki z900
d.Hayabusa
"""

q5="""what is your fav. car?
a.Audi A3
b.RollsRoyce
c.FordMustang
d.impala
"""

questions={q1:"a",q2:"c",q3:"b",q4:"c",q5:"d",}

name=input("Hi whats your name: ")
print("Hello",name,"Welcome to the quiz")
score=0
for i in questions:
    print()
    print(i)
    flag1=input("Do you want to skip this ques(yes\no)")
    if flag1=="Yes":
        continue
    ans=input("enter your answer")
    if ans==questions[i]:
        print("Wow! You got one point")
        score=score+1
        print("Your current score is: ",score)
    else:
        print("Wrong answer, U lost 1 mark")
        score=score-1
        print("UR current score is: ",score)
        flag2=input("Do you want to Quit? type (yes/no)")
        if flag2=="yes":
            break
        print("Your total score is ",score)


#PROJECT-2-TIMER-CLOCK


import time
def countdown(t):
    while t:
        mins, secs = divmod(t, 60)
        timer='{:02d}:{:02d}'.format(mins,secs)
        print(timer)
        time.sleep(1)
        t-=1
    print("FINISHED")
t=input("Enter the time in seconds: ")
countdown(int(t))



#PRJOJECT-3-FLAMES

name1=input("Enter the name1: ").lower()
name2=input("Enter the name2: ").lower()

name1=name1.replace(" ","")
name2=name2.replace(" ","")
print(name1)
print(name2)

for i in name1:
    for j in name2:
        if i==j:
            name1=name1.replace(i,"",1)
            name2=name2.replace(j,"",1)
            break
count=len(name1+name2)

print(count)
if count>0:
    list1=["Friends","Lovers","Affectionate","Marriage","Enemies","Siblings"]
    while len(list1
              )>1:
        c=count%len(list1)
        s_index=c-1

#slicing

        if s_index>=0:
            left=list1[:s_index]
            right=list1[s_index+1:]
            list1=right+left
        else:
            list1=list1[:len(list1)-1]
    print("Relationship:",list1[0])

else:
    print("Enter different names")

