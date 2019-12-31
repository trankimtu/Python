
print ("================================")
print ("List")
print ("================================")


fruitList = ["apple", "bannana", "cherry"]
print(fruitList.index('cherry'))
print("fruitList: {}".format(fruitList))
print("fruitList length: {}".format(len(fruitList)))
print("fruitList {} = {}".format(0, fruitList[0]))
print("fruitList {} = {}".format(1, fruitList[1]))
print("fruitList {} = {}".format(2, fruitList[2]))

print("\n\n")

print("fruitList {} = {}".format(-1, fruitList[-1]))
print("fruitList {} = {}".format(-2, fruitList[-2]))
print("fruitList {} = {}".format(-3, fruitList[-3]))

print (f"fruitList 0:2 = {fruitList[0:2]}")
print (f"fruitList 1:  = {fruitList[1:]}")
print (f"fruitList :1  = {fruitList[:2]}")

nums = [25, 12, 36, 95, 14]
names = ['navin', 'kiran', 'john']
values = [9.5, 'Navin', 25]
mil = [nums, names]
print(mil)

print("\n\n")
print(f"nums \t\t\t = {nums}")

# Append list - Add 1 element to the end
nums.append(45)
print(f"nums.append(45) \t = {nums}") # cannot put append inside {} of f string

# Extend
nums.extend([11, 22, 33])
print(f"nums.extend([11, 22, 33])= {nums}")

# Insert to list 
nums.insert(2, 77)
print(f"nums.insert(2, 77) \t = {nums}")

# Remove from list
nums.remove(14)
print(f"nums.remove(14) \t = {nums}")

print(f"nums.pop(1) \t\t = {nums.pop(1)}")
print(f"nums \t\t\t = {nums}")

print(f"nums.pop() \t\t = {nums.pop()}")
print(f"nums \t\t\t = {nums}")

# del
del nums[2:]
print(f"nums \t\t\t = {nums}")

# min
print(f"min(nums) \t\t = {min(nums)}")

# max
print(f"max(nums) \t\t = {max(nums)}")

# sum
print(f"sum(nums) \t\t = {sum(nums)}")

# sort
nums.extend([33, 11])
print(f"nums.extend([33, 11]) \t = {nums}")

nums.sort()
print(f"nums.sort() \t\t = {nums}")


print("\n\n")

print ("================================")
print ("Tuple")
print ("================================")

# Like a list, but cannot change value, run faster than list
tup = (21, 36, 14, 25)
print(f"tup = {tup}")
print(f"tup[1] = {tup[1]}")
# cannot: tup[1] = 2


print("\n\n")

print ("================================")
print ("Set")
print ("================================")

# no sequence, cannot access by index. Repeat won't be count
s = {11, 33, 22, 44, 33}
print(s)
print(s)
print(s)


print("\n\n")

print ("================================")
print ("Dictionary")
print ("================================")


# ===============================================
print("=" * 50)
print(f"array".upper())
print("=" * 50)
# ===============================================

# All members are the same data type
import array

myArray = array.array('i', (1, 2, 3, 4, 5))
print(f'myArray \t\t = {myArray}')

from array import *

intArray = array('i', (1, 2, 3, 4, 5))
print(f'intArray \t\t = {intArray}')

print(f'intArray[0] \t\t = {intArray[0]}')
print('All values of intArray   = ', end = '')
for e in intArray:
    print(f'{e}\t', end = '')
print()
print(f'intArray.buffer_info()   = {intArray.buffer_info()}') # return address and len()
print(f'intArray address \t = {intArray.buffer_info()[0]}')
print(f'intArray len \t\t = {intArray.buffer_info()[1]}')
print(f'len(intArray) \t\t = {len(intArray)}')
print(f'intArray.typecode = {intArray.typecode}')
intArray.append(2)
print(intArray)
intArray.pop()
print(intArray)

# Copy array
intReverse = array(intArray.typecode, (e for e in intArray))

# Reverse array
intReverse.reverse()
print(intReverse)


print("\n\n")


print ("================================")
print ("Empty Array")
print ("================================")

from array import *

myArray = array ('i', [])
x = -1000

while True:
    x = int(input('Enter the next int value (-1 to finish): '))
    if x == -1 :
        break
    else:
        myArray.append(x)
print(myArray)

print ("================================")
print ("Search in Array")
print ("================================")

x = int(input('Enter the value for search: '))
for i in myArray:
    if i == x:
        print('Found')
        print(f'Index = {myArray.index(x)}')
        break
else: 
    print('Not Found')