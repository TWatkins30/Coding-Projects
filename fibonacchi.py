def fibonacchi(n):
    """Print the Fibonacci series up to n numbers.
    a[n] = a[n-1] + a[n-2]
    a[1] = 1
    a[0] = 0
    """
    c = 0
    a, b = 0, 1
    while c < n:
        c += 1
        print(b,end=' ')
        a, b = b, a + b
    print(b)

if __name__ == "__main__":
    fibonacchi(20)
    
