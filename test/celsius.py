import sys
def convert(cel):
    # calculate fahrenheit
    fahrenheit = (cel * 1.8) + 32
    print('%0.1f degree Celsius = %0.1f degree Fahrenheit' % (cel, fahrenheit))
    return fahrenheit

if __name__ == '__main__':
    arg = sys.argv
    n = float(arg[1])
    convert(n)
