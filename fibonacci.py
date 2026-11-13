
try:
    n = int(input("Enter number of terms: "))

    if n < 0:
        print("Please enter a non-negative number.")
    elif n == 0:
        print("No terms to display.")
    else:
        a, b = 0, 1

        print("Fibonacci series:")
        for _ in range(n):
            print(a, end=" ")
            a, b = b, a + b

except ValueError:
    print("Invalid input! Please enter an integer.")
