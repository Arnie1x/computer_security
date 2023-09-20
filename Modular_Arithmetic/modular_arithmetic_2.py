from math import gcd

a = 273246787654
p = 65537

if gcd(a,p) == 1:
    print("Coprime! Solution is 1")