def prime_number(number):
    if number<2: return False
    for i in range(2,int(number**0.5)+1):
        if number%i==0:
            return False
    return True

def primeX(x):
    n=1
    count=0
    while (count<x):
        n +=1
        if prime_number(n):
            count +=1
    return n



if __name__ == "__main__":
    print(primeX(1))  # 2
    print(primeX(5))  # 11
    print(primeX(8))  # 19
    print(primeX(9))  # 23
    print(primeX(10)) # 29