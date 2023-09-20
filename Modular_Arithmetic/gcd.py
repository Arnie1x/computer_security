def hcf(a, b):
    if (b == 0):
        return abs(a)
    else:
        return hcf(b, a % b)


a = 66528
b = 52920

# prints 12
print("The gcd of " + str(a) + " and " + str(b) + " is : ", end="")
print(hcf(a, b))
