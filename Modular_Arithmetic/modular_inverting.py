# The problem given is 3 * d ≡ 1 mod 13
# To calculate d we can divide both sides by 3 which gives us
# d = (1/3) * 1 mod 13
# which is equivalent to
# d = 3^-1 mod 13, where ^ symbol is raised to the power of
# We can easily convert this into python equation using the pow function


print(pow(3, -1, 13))
