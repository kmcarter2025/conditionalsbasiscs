var = input('enter an even or odd integer: ')
ivar = int(var)

if ivar % 2 == 0:                     # if the number is even
    print(ivar, 'is even')
    print('2 divides evenly into it')

else:  # otherwise if it is odd        # otherwise if it is odd
    print(ivar, 'is odd')
    print("you're pretty odd, too")

print('done')

print(type(var))
print(type(ivar))
