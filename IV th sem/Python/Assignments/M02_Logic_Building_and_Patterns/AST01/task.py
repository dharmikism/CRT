def count_digits(n: int) -> int:
    return len(str(abs(n)))

if __name__ == "__main__":
    n = int(input())
    print(count_digits(n))
