"""
def sq_numbers(n):
    for i in range(1,n+1):
        yield i*i

a = sq_numbers(3)

print("The squre of numbers 1,2,3 are :")
print(next(a))
print(next(a))
print(next(a))
print(type(a))

#list is early loading causes memory error
l = []
for i in range(100000000):
    l.append(i)
print(l[0])


#generator lazy loading:memory utilization,performance improved,its not data structure,large
g = (x*x for x in range(100000000))
print(type(g))

print(next(g))
print(next(g))


def gen():
    yield "A"
    yield "B"
    yield "C"
    yield "D"
    yield "E"
    yield "F"
    yield "G"
    yield "H"

g = gen()
print(next(g))
print(next(g))
print(next(g))

def value_gen(a, b):
    yield a
    yield b

x,y = value_gen(10, 20)
print(x)
print(y)

result = value_gen(10, 20)

print(type(result))
print(next(result))
print(next(result))

#We can iterate on generator object
def first_nval(num):
    n = 1
    while n<= num:
        yield n
        n = n+1
values = first_nval(10000000000000)
print(type(values))
for x in values:
    print(x,end=" ")
"""






    
