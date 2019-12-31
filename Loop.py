# ===============================================
print('\t' + '=' * 50)
print('\t'*3 + 'For loop'.upper())
print('\t' + '=' * 50)
# ===============================================

nums = [1, 2, 3, 4, 5]
for num in nums:
    if num % 5 == 0:
        print(num)
        break
else: print('Not found')

isPrime = int(input('Enter check Prime number: '))
for i in range(2, isPrime):
    if isPrime % i == 0:
        print(f'{isPrime} is not a prime number!')
else: print(f'{isPrime} is a prime number')
# ===============================================
print('\t' + '=' * 50)
print('\t'*3 + 'While loop'.upper())
print('\t' + '=' * 50)
# ===============================================

i = 1

while i <= 5:
    print(i)
    i += 1
else:
    print('End loop \n\n')

print('4 x 4 Square *')
for i in range(4):
    print('# ' * 4)
print('\n\n')    

print('4 x 4 Triangle *')
for i in range(5):
    print('*' * i)
print('\n\n')    

print('4 x 4 Square Num')

i = 1
j = 1
k = 1
while i < 5:

    for j in range(5):
        if k < 10:
            print(f'{k}  ' , end = '')
        else:    
            print(f'{k} ' , end = '')
        k += 1
    print()
    i += 1
print('\n\n')    

print('4 x 4 Triangle Num')

i = 1
j = 1
k = 1
while i < 5:
    j = k
    while j < 5:
        print(f'{j} ' , end = '')
        j += 1
    print()
    i += 1
    k += 1

print('\n\n')    

# ===================
j = 1
for i in range(1, 6):
    while j < 5:
        print(f'{j} ', end = '')
        j += 1
    print()
    j = i

# ===================
for i in range(1, 6):
    while j < 5:
        print(f'{j} ', end = '')
        j += 1
    print()
    j = i


print('\n\n')    



for i in range(4):
    print('# ' * (4-i))
print('\n\n')    
for i in range(4):
    print('# ' * (4-i))
print('\n\n')    
    

# ===============================================
print('\t' + '=' * 50)
print('\t'*3 + 'calendar'.upper())
print('\t'*3 + 'January 2020 \n')
print('\t' + '=' * 50)
# ===============================================

day = ('M', 'T', 'W', 'R', 'F', 'S', 'U')

for i in day:
    print(f'\t{i}', end = '')

print('\n\n')

date = 1
cycle = 2
print('\t\t', end = '')
while date <= 31:
    while cycle < 7:
        if date > 31:
            break
        print(f'\t{date}', end = '')
        date += 1
        cycle += 1
        
    else:
        print('\n')
        cycle = 0

print('\n\n')

# clip 25 break continue pass