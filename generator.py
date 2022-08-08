import random

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
