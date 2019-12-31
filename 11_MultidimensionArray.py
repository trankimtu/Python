# need to install 3rd party Numpy
# pip3 install numpy

from numpy import *

# myArray = np.array([[1, 2, 3], [4, 5, 6]], np.int32)
# myArray = np.array([[1, 2, 3], [4, 5, 6]])


myArray = array([[1, 2, 3], [4, 5, 6]])
print(myArray)
print(f'Type of myArray = {myArray.dtype}')

# cast datatype
myArray = array([[1, 2, 3], [4, 5, 6]], float)
print(myArray)
print(f'Type of myArray = {myArray.dtype}')

myArray = array([[1, 2, 3], [4, 5, 6.0]])   # all values will be converted to float
print(myArray)

print(f'Type of myArray = {myArray.dtype}')

#linspace