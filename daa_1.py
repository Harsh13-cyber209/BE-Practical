def fibonacci_recursive(n):
    if n <= 1:
        return n
    return fibonacci_recursive(n-1) + fibonacci_recursive(n-2)

def fibonacci_iterative(n):
    a, b = 0, 1

    for i in range(n):
        print(a, end=" ")
        a, b = b, a + b



n = int(input("Enter number of terms: "))

if n < 0:
    print("Enter a non-negative number")
else:
    print("Recursive Fibonacci:")
    for i in range(n):
        print(fibonacci_recursive(i), end=" ")

    print("\nNon-Recursive Fibonacci:")
    fibonacci_iterative(n)
