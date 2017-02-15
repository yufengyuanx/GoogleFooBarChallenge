def answer(n):
    currentNumber = 1
    primeStr = ""
    while len(primeStr) < n + 5:
        currentNumber = currentNumber + 1
        while is_prime(currentNumber) == False:
            currentNumber = currentNumber + 1
        primeStr = primeStr + str(currentNumber)
    return primeStr[n:n+5]
    
    
def is_prime(num):
    for i in range(2,num):
        if (num % i) == 0:
            return False
    return True

