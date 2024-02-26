def prime_number(number):
    if number<2: return False
    for i in range(2,int(number**0.5)+1):
        if number%i==0:
            return False
    return True

def generate_primes_grid(width, height, start):
    result = ""
    list_prime=[]
    n=start
    count=0
    
    # generate semua prime number 
    while (count<width*height):
        n +=1
        if prime_number(n):
            list_prime.append(n)
            count +=1

    # generate primes grid
    inc=0
    for i in range(height):
        for j in range(width):
                # hapus spasi di ujung column
                if j==width-1 :
                    result +=str(list_prime[inc])

                # cek spasi jika bilangan prima pertama hanya 1 digit     
                elif list_prime[inc] < 10:
                    if j==0:
                        result +=str(list_prime[inc])+" "
                    else: result +=" "+str(list_prime[inc])+" "
                else:result +=str(list_prime[inc])+" "
                inc +=1
        result +="\n"
    return result

if __name__ == "__main__":
    print(generate_primes_grid(2, 3, 13))
    """
    17 19
    23 29
    31 37
    """
    print(generate_primes_grid(5, 2, 1))
    """
    2  3  5  7 11
    13 17 19 23 29
    """