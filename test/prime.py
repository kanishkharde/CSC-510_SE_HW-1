import sys
def prime_check(num):
    if num == 1:
        print("1 is neither prime nor composite")
    elif num > 1:
        # check for factors
        for i in range(2, num):
            if (num % i) == 0:
                print(num, "is not a prime number")
                print(i, "times", num // i, "is", num)
                break
        else:
            print(num, "is a prime number")
    else:
        print(num, "is not a postive nonzero number")

if __name__ == '__main__':
    arg = sys.argv
    n = int(arg[1])
    prime_check(n)
