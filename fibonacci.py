def fib(n):
    if n ==1 or n ==2:
        return 1
    else:
        return fib(n-1) + fib(n-2)

def main():
    n = int(input("Enter fibonacci number: "))
    result = fib(n)
    print("Result:", result)

if __name__ == "__main__":
    main()