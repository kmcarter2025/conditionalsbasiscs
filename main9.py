print('starting')

while True:                                # loop thru this block repeatedly
    print('top of loop *')
    x = input('enter "q" to quit: ')
    if x == 'q':
        print('quitting...')
        break
    print("continuing...")
    # return to top of loop

print('ending')
