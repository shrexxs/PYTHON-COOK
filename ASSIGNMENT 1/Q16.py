import math

e_pow_pi = math.e**math.pi
pi_pow_e = math.pi ** math.e
print("e^π: ",e_pow_pi)
print("π^e: ",pi_pow_e)

if e_pow_pi > pi_pow_e:
    print("ok")
else:
    print("ok anyway")