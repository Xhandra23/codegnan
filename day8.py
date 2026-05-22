'''nested loops
---------------
'''
'''num=4
for t in range(1,11):
    print(f"{num}x{t}={t*num}")'''
'''
df=input("enter a word:")
gh=" "
for t in df:
    gh = t + df
    print(gh)
if'''
'''
num=int(input("enter a number :"))
amstro=0
length=len(str(num))
for i in str(num):
     amstro += int(i) ** length
if amstro == num:
    print(f" {num}is a amstro  ")
'''
'''num= int(input("enter a number:"))
perf=0
for i in range(1,num):
    if num%i ==0:
        perf += i
if perf == num:
    print(f"{num} is a perfect num")
else:
     print(f"{num} is  not a perfect num")'''
'''
num= int(input())
count = 0
for k in range(1,num+1):
    if num%k ==0:
        count+=1
if count == 2:
    print(f"{num} is a prime number")
else :
    print(f"{num} is not prime number")'''
'''
star=int(input())
for g in range(1,star+1):
    for d in range(1,g+1):
        print("*",end= " ")
        print()'''
'''star=5
for g in range(1,10,2):
    for d in range(1,8):
        print(d)'''
num = int(input("int:"))
for j in range(1,num+1):
    print(" "*(num-j),end="")
    for i in range(1,j+1):
        print("*",end=" ")
    print()
        
        





