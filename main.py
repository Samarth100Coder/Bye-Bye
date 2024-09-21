try:
    a=int(input('Enter a number: '))
    if a%2==0:
        raise ValueError
    print('Number is:',a)
except ValueError:
    print('Error is: Number is divisible by 2')
else:
    print('Successful')
finally:
    print('Program ended')