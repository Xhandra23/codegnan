#list comprehension
#------------------
#---> this list comprehension offers a shortest syntax when we want to create a new from existing list
#--> syntax---> vari_name = [experssion  loop condition]
'''old=[1,2,3,4,5]
new=[so for so in old]
print(new)'''
'''
old=[1,2,3,4,5]
new=[so if so%2!=0 else "even" for so in old   ]
print(new)
'''

# generators
#-----------
#-->generator in python are special type of itterable,allowing users to iterate over data efficiently without storing everything in memory...
#---->they generate values lazily using yield keyword
#--> why to use generators
#-->genertors does not store the entire dataset in memroy ,they generate values on the fly
#-->avoid unnecessary storage of data speed up execution.
# how it works
#-------------
#--> it looks like nrml function but uses the yield key word instead of return
#--> when the function is called , it does not execute immediately .instead, it return a generator object which can be iterated using loop or the next() function 
'''
def simple_gen():
    print("start")
    yield 1
    yield 2
    yield 3
    print("end")
gen=simple_gen()
print(next(gen))
print(next(gen))
print(next(gen))
'''
'''
def any(num):
     for i in range (num):
         yield i*i
a= any(5)
print(next(a))
print(next(a))
print(next(a))
print(next(a))
'''
'''
def sqr(num):
    result = []
    for i in range(1,num+1):
        result.append(i*i)
    return result
print(sqr(23))
'''



