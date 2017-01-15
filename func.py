def fib(num):
    if(num == 0 or num == 1):
        return num
    else:
        return fib(num-1) + fib(num-2)

def count_one(num):
    count = 0
    while (num != 0):
        num = num & (num - 1)
        count = count + 1

    return count


def left_shift(num):
    for i in range(1,num+1):
        print i<<1

print count_one(7)
print left_shift(10)


var = int(raw_input('Enter the nth number to calculate nth fibonacci'))
print fib(var)
