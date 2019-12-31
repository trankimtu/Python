x = int(input('Enter a number: '))
r = x % 2

if r == 0:
    print(f'{x} is even')
else:
    print(f'{x} is odd')
    
if x == 0:
    print ('Your input is 0')
elif x > 0:
    print ('Your input is possitive integer')
else:
    print ('Your input is negative integer')