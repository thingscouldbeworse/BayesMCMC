import random

def check_a(b, d):
    checker = random.uniform(0,1)
    if(b and d):
        return checker <= 0.8873239437
    if(not b and d):
        return checker <= 0.2727272727
    if(not b and not d):
        return checker <= 0.8571428571
    if(b and not d):
        return checker <= 0.9921259843

def check_b(a):
    checker = random.uniform(0,1)
    if(a):
        return checker <= 0.7
    if not a:
        return checker <= 0.1

def check_d(a, e):
    checker = random.uniform(0,1)
    if(a and e):
        return checker <= 0.02702
    if(not a and e):
        return checker <= 0.30769
    if(a and not e):
        return checker <= 0.6923
    if(not a and not e):
        return checker <= 0.973

def check_e(d):
    checker = random.uniform(0,1)
    if d:
        return checker <= 0.1
    if not d:
        return checker <= 0.9

counter = 0

a = random.randint(0,1)
b = random.randint(0,1)
d = random.randint(0,1)
e = random.randint(0,1)

iterations = 10000

print(a, b, d, e)

for i in range(0,iterations):

    if check_a(b, d):
        a = 1
    else:
        a = 0

    if check_b(a):
        b = 1
    else:
        b = 0

    if check_d(a, e):
        d = 1
    else:
        d = 0

    if check_e(d):
        e = 1
    else:
        e = 0
    if i % 100 == 0 and i > 1:
        print(counter/i)
    if b:
        counter += 1

print( str((counter)/iterations))
