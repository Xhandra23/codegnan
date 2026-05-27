'''
fibnaaci series
num=0
num_2=1
def finaaci(num,num_2):
    limit=int(input("enter the limit:"))
    print(num,num_2,end="")
    for i in range (1,limit):
        num_3 = num+ num_2
        num = num_2
        num_2 = num_3
        print(num_3,end=" ")
finaaci(num,num_2)
'''
'''
remove duplicates from list
any=[2,5,7,9,2,7]
new_=[]
def dup(any,new_):
    for j in any:
        if j not in new_:
            new_.append(j)
    print(new_)
dup(any,new_)
'''
'''
count the word in paragarah
jii=0
any="chandra sekhar kkkldjfkldf ljdjsl dfljsljtr nfnd;k;l nndkllk; ".split()
def count(any,jii): 
    for j in any:
        jii += 1
    print(jii)
count(any,jii)
'''
