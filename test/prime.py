import sys
def prime_check(num):
    if num == 1:
        print("1 is neither prime nor composite")
        return num
    elif num > 1:
        # check for factors
        for i in range(2, num):
            if (num % i) == 0:
                print(num, "is not a prime number")
                print(i, "times", num // i, "is", num)
                return i
                break
        else:
            print(num, "is a prime number")
            return num
    else:
        print(num, "is not a postive nonzero number")
        return -1

if __name__ == '__main__':
    arg = sys.argv
    n = int(arg[1])
    a=prime_check(n)
