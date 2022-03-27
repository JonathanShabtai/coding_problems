def print_digits(n):
    while n:
        n, remainder = divmod(n, 10)
        print(remainder)
        print(n)

print_digits(321312890)