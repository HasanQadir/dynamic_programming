def recursive_fib(n):
    if n ==1 or n ==2:
        return 1
    else:
        return recursive_fib(n-1) + recursive_fib(n-2)

def dp_memoize_fib(n, arr):
    if arr[n] != None:
        result = arr[n]
    if n ==1 or n ==2:
        return 1
    else:
        result = dp_memoize_fib(n-1, arr) + dp_memoize_fib(n-2, arr)
    return result

def main():
    n = int(input("Enter fibonacci number: "))
    # result = recursive_fib(n)
    result = dp_memoize_fib(n, [None] * (n + 1))
    print("Result:", result)

if __name__ == "__main__":
    main()