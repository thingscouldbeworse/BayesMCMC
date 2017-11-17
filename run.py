import random

def check_a(b, d):
    if(b and d):
        # 0.8873239437
        return True
    if(not b and d):
        # 0.2727272727
        return False
    if(not b and not d):
        # 0.8571428571
        return True
    if(b and not d):
        # 0.9921259843
        return True

def check_b(a):
    if(a):
        # 0.1
        return False
    if not a:
        # 0.7
        return True

def check_d(a, e):
    if(a and e):
        # 0.02702
        return False
    if(not a and e):
        # 0.30769
        return False
    if(a and not e):
        # 0.6923
        return True
    if(not a and not e):
        # 0.973
        return True

def check_e(d):
    if d:
        # 0.1
        return False
    if not d:
        # 0.9
        return True

a_counter = 0
b_counter = 0
d_counter = 0
e_counter = 0

for i in range(0,10000):
    a = random.randint(0,1)
    b = random.randint(0,1)
    d = random.randint(0,1)
    e = random.randint(0,1)

    if not check_a(b, d):
        a_counter += 1
    if not check_b(a):
        b_counter += 1
    if not check_d(a, e):
        d_counter += 1
    if not check_e(d):
        e_counter += 1


print("a: " + str(a_counter))
print("b: " + str(b_counter))
print("d: " + str(d_counter))
print("e: " + str(e_counter))
print( str((a_counter + b_counter + d_counter + e_counter)/40000))
