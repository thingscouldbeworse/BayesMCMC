import random

#        abde
probabilities = {
        'x11x': 0.8873239437,
        'x01x': 0.2727272727,
        'x00x': 0.8571428571,
        'x10x': 0.9921259843,
        '1xxx': 0.7,
        '0xxx': 0.1,
        'xx1x': 0.1,
        'xx0x': 0.9,
        '1xx1': 0.02702,
        '0xx1': 0.30769,
        '1xx0': 0.6923,
        '0xx0': 0.973
        }

counter = 0
iterations = 10000

a = random.randint(0,1)
b = random.randint(0,1)
d = random.randint(0,1)
e = random.randint(0,1)
print(a, b, d, e)

for i in range(0,iterations):
    
    checker = random.uniform(0,1)
    a = (1 if checker <= probabilities['x'+str(b)+str(d)+'x'] else 0) 
    checker = random.uniform(0,1)
    b = (1 if checker <= probabilities[str(a)+'xxx'] else 0) 
    checker = random.uniform(0,1)
    d = (1 if checker <= probabilities[str(a)+'xx'+str(e)]else 0)
    checker = random.uniform(0,1)
    e = (1 if checker <= probabilities['xx'+str(d)+'x'] else 0)

    if i % 100 == 0 and i > 1:
        print(counter/i)
    if b:
        counter += 1

print( str((counter)/iterations))
