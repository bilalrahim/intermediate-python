import random

def countDown(n):
    while n > 0:
        yield n
        n-=1

x=countDown(10)
print(list(x))
# print(next(x))
# print(next(x))

def rand_nums():
    while True:
        rands=(random.random(), random.random())
        yield rands

def gen_random():
    while True:
        yield next(rand_nums())
fun=gen_random()
print(next(fun))
print(next(gen_random()))
