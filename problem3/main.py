def fibonacci(number):

    if number<0:return None
    elif number==0:return 0
    elif number<3: return 1
    else: 
        # recursive function: F(n) = F(n-1) + F(n-2)
        return fibonacci(number-1)+fibonacci(number-2)

if __name__ == "__main__":
    print(fibonacci(0))  # 0
    print(fibonacci(2))  # 1
    print(fibonacci(9))  # 34
    print(fibonacci(10)) # 55
    print(fibonacci(12)) # 144