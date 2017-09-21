a = float(input('Input first number: '))
b = input('Choose the function: ')
c = float(input('Input second number: '))

def plus():
    print('Number is ' + ('%.2f' % (a + c)))
def minus():
    print('Number is ' + ('%.2f' % (a - c)))
def multiply():
    print('Number is ' + ('%.2f' % (a * c)))
def divide():
    print('Number is ' + ('%.2f' % (a / c)))
def zero():
    print('ZERO')

if b == '+':
    plus()
if b == '-':
    minus()
if b == '*':
    multiply()
if b == '/' and c != 0:
    divide()
elif b == '/' and c == 0:
    zero()

input('\n\nPress Enter to exit')