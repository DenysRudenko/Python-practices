from exp_root import exponentiation as exp, root
from factorial import factorial as fact
from logarithm import logarithm as log

def work_exp():
    n = int(input('Power value (2 or 3): '))
    x = float(input('Input x: '))
    sf = ''
    if n == 2:
        value = exp.exp2(x)
        sf = 'nd'
    elif n == 3:
        value = exp.exp3(x)
        sf = 'rd'
    else:
        print('Wrong power value')
        return
    print(f'{n}{sf} power of {x} is {value}')


def work_root():
    n = int(input('Root value (2 or 3): '))
    x = float(input('Input x: '))
    sf = ''
    if n == 2:
        if x < 0:
            print('Value of x must be not negative')
            return
        value = root.root2(x)
        sf = 'nd'
    elif n == 3:
        value = root.root3(x)
        sf = 'rd'
    else:
        print('Wrong root value')
        return
    print(f'{n}{sf} root of {x} is {value}')


def work_fact():
    n = int(input('Input n: '))
    if n < 0:
        print('Value of n must be not negative')
        return
    value = fact.fact(n)
    print(f'{n}! is {value}')


def work_log():
    fname = ''
    m = int(input('Select logarithm base (1: e, 2: 10, 3: your base): '))
    if m == 1:
        x = float(input('Input x: '))
        if x < 0:
            print('Value of x must be not negative')
            return
        value = log.ln(x)
        fname = 'ln'
    elif m == 2:
        x = float(input('Input x: '))
        if x < 0:
            print('Value of x must be not negative')
            return
        value = log.lg(x)
        fname = 'lg'
    elif m == 3:
        base = float(input('Input logarithm base: '))
        if base < 0:
            print('Value of logarithm base must be not negative')
            return
        if base == 1:
            print('Value of logarithm base must be equal to 1')
            return
        x = float(input('Input x: '))
        if x < 0:
            print('Value of x must be not negative')
            return
        value = log.log(base, x)
        fname = f'log_{base}'
    else:
        print('Wrong input')
        return

    print(f'{fname}({x}) is {value}')


def menu():

    while True:
        print('\nSelect function:')
        print('\t1 - exponential')
        print('\t2 - root')
        print('\t3 - factorial')
        print('\t4 - logarithm')
        print('\t5 - exit')
        m = int(input('Make your choice: '))
        if m == 1:
            work_exp()
        elif m == 2:
            work_root()
        elif m == 3:
            work_fact()
        elif m == 4:
            work_log()
        elif m == 5:
            break
        else:
            print('Wrong input')


if __name__ == '__main__':
    menu()

