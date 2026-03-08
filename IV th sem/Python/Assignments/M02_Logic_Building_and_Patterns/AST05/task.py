def number_triangle(n: int) -> str:
    result = ""
    for i in range(1, n + 1):
        for j in range(1, i + 1):
            result += str(j)
        result += "\n"
    return result.strip()

if __name__ == "__main__":
    n = int(input())
    print(number_triangle(n))
