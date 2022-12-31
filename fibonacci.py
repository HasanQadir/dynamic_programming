def fib(n):
    if n ==1 or n ==2:
        return 1
    else:
        return fib(n-1) + fib(n-2)

def main():
    result = fib(5)
    print(result)

if __name__ == "__main__":
    main()