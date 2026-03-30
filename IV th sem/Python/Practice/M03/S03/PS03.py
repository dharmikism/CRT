"""Practice file: examples of Python built-in functions."""


def largest_number_without_max(values):
    largest = values[0]
    for value in values:
        if value > largest:
            largest = value
    return largest


def palindrome_check(word):
    return word == "".join(reversed(word))


def read_int_list(prompt):
    return list(map(int, input(prompt).split()))


def read_name_list(prompt):
    return list(map(str.strip, input(prompt).split(",")))


def main():
    numbers = read_int_list("Enter numbers separated by space: ")
    if not numbers:
        print("Please enter at least one number.")
        return

    word = input("Enter a word to check palindrome: ").strip()
    names = read_name_list("Enter student names separated by comma: ")
    marks = read_int_list("Enter marks separated by space: ")

    if len(names) != len(marks):
        print("Names and marks count should be equal.")
        return

    abs_input = int(input("Enter an integer for abs(): "))
    round_number = float(input("Enter a decimal number for round(): "))
    round_digits = int(input("Enter digits for round(): "))
    base = int(input("Enter base for pow(): "))
    exponent = int(input("Enter exponent for pow(): "))
    dividend = int(input("Enter dividend for divmod(): "))
    divisor = int(input("Enter divisor for divmod(): "))

    if divisor == 0:
        print("Divisor cannot be zero for divmod().")
        return

    print("Original numbers:", numbers)

    # max, min, sum, len
    print("Largest (manual):", largest_number_without_max(numbers))
    print("Largest (max):", max(numbers))
    print("Smallest (min):", min(numbers))
    print("Total (sum):", sum(numbers))
    print("Count (len):", len(numbers))

    # sorted and set
    print("Sorted ascending:", sorted(numbers))
    print("Sorted descending:", sorted(numbers, reverse=True))
    print("Unique values (set):", set(numbers))

    # map and filter
    squares = list(map(lambda x: x * x, numbers))
    evens = list(filter(lambda x: x % 2 == 0, numbers))
    print("Squares (map):", squares)
    print("Even numbers (filter):", evens)

    # reversed
    print(f"Is '{word}' palindrome?", palindrome_check(word))

    # any and all
    print("Any even number?", any(n % 2 == 0 for n in numbers))
    print("All positive?", all(n > 0 for n in numbers))

    # enumerate and zip
    print("\nStudent list using enumerate:")
    for index, name in enumerate(names, start=1):
        print(index, name)

    print("\nName with marks using zip:")
    for name, mark in zip(names, marks):
        print(name, "->", mark)

    # abs, round, pow, divmod
    print(f"\nabs({abs_input}):", abs(abs_input))
    print(f"round({round_number}, {round_digits}):", round(round_number, round_digits))
    print(f"pow({base}, {exponent}):", pow(base, exponent))
    print(f"divmod({dividend}, {divisor}):", divmod(dividend, divisor))

    # type and isinstance
    print("\nType of numbers:", type(numbers))
    print("Is marks a list?", isinstance(marks, list))


if __name__ == "__main__":
    main()