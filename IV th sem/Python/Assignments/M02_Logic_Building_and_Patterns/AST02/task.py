def reverse_number(n: int) -> int:
    reversed_num = 0
    sign = -1 if n < 0 else 1
    n = abs(n)
    
    while n > 0:
        digit = n % 10
        reversed_num = reversed_num * 10 + digit
        n //= 10
    
    return sign * reversed_num

if __name__ == "__main__":
    n = int(input())
    print(reverse_number(n))
