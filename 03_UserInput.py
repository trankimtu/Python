"""
# ===============================================
print("=" * 50)
print(f"Read input from console".upper())
print("=" * 50)
# ===============================================
name = input("Name: ")
print('name')
print(f"type of name = {type(name)}")

age = int(input("Age: "))
print(f"type of age = {type(age)}")

# ===============================================
print("=" * 50)
print(f"Get 1st character of string input".upper())
print("=" * 50)
# ===============================================
ch = input('enter a char: ')
print(ch[0])
ch = input('enter a char: ')[0]
print(ch)


# ===============================================
print("=" * 50)
print(f"Evaluate an expression".upper())
print("=" * 50)
# ===============================================

result = eval(input('Enter an expr: '))
print(f'Result = {result}')

# ===============================================
print("=" * 50)
print(f"Call file and pass arg from command line cmd".upper())
print("=" * 50)
# ===============================================
"""
import sys
x = int(sys.argv[1])
y = int(sys.argv[2])
z = x + y
print(f"z = {z}")
# call from command line: python UserInput.py 6 2
#                                 argv[0]   [1][2]