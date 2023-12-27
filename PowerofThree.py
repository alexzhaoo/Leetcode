def isPowerOfThree(n):
    if n==3:
        return True
    elif n<=3:
        return False
    return isPowerOfThree(n/3)


print(isPowerOfThree(28))