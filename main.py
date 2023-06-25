var = input('please enter a number greater than 100: ')
number = int(var)

if number <= 100:
    exit('error: number must be greater than 100')

else:
    print('your number doubled is ', number * 2)
    print('thanks!')
