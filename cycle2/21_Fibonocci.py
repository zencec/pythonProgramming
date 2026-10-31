n = int(input("Enter the number of terms: "))

if n <= 0:
    print("Fibonacci series for", n, "terms is not defined")
else:
    first = 0
    second = 1

    print("The first", n, "numbers in the Fibonacci series are:")

    print(first, end="")

    if n > 1:
        print(",", second, end="")

    for i in range(2, n):
        fib = first + second
        first = second
        second = fib
        print(",", fib, end="")

    print()
