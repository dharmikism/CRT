def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

def lcm(a, b):
    return (a * b) // gcd(a, b)

def minimum(a, b):
    return a if a < b else b

def maximum(a, b):
    return a if a > b else b

def check_perfect_number(n):
    if n < 2:
        return False
    sum_of_divisors = 1
    for i in range(2, n//2 + 1):
        if n % i == 0:
            sum_of_divisors += i
    return sum_of_divisors == n

a,b=map(int,input("Enter two numbers: ").split())
print("Traditional method:")
print("GCD of",a,"and",b,"is",gcd(a,b))
print("LCM of",a,"and",b,"is",lcm(a,b))
print("Minimum of",a,"and",b,"is",minimum(a,b))
print("Maximum of",a,"and",b,"is",maximum(a,b))
print("Perfect number check:")
print(a,"is a perfect number.",check_perfect_number(a))
print("\nBuilt-in functions:")
print("GCD of",a,"and",b,"is",gcd(a,b))
print("LCM of",a,"and",b,"is",lcm(a,b))
print("Minimum of",a,"and",b,"is",minimum(a,b))
print("Maximum of",a,"and",b,"is",maximum(a,b))

