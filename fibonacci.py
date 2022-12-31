def recursive_fib(n):
    if n ==1 or n ==2:
        return 1
    else:
        return recursive_fib(n-1) + recursive_fib(n-2)

def dp_memoize_fib(n, arr):
    if arr[n] != None:
        result = arr[n]
    if n ==1 or n ==2:
        result = 1
    else:
        result = dp_memoize_fib(n-1, arr) + dp_memoize_fib(n-2, arr)
    return result

def dp_bottomup_fib(n):
    if n ==1 or n ==2:
        return 1
    bottom_up = [0] * (n)
    bottom_up[0] = 1
    bottom_up[1] = 1
    for i in range(2,n):
        bottom_up[i] = bottom_up[i-1] + bottom_up[i-2]
    return bottom_up[n-1]

def main():
    n = int(input("Enter fibonacci number: "))
    # result = recursive_fib(n)
    # result = dp_memoize_fib(n, [None] * (n + 1))
    result = dp_bottomup_fib(n)
    print("Result:", result)

if __name__ == "__main__":
    main()