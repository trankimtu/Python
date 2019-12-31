# ===============================================
print("=" * 50)
print(f"Output to console".upper())
print("=" * 50)
# ===============================================


msg1 = "Hello"
msg2 = "World!"
print(msg1 + ' ' + msg2)

# print without taking new line
print(msg1, end = '')
print(msg2)

# Raw text - ignore all special keyword meaning 
print(r"(}a\t\n\s{msg1}")

#  Format text - print string with parameter value
print('My string is {} {} '.format(msg1, msg2))
print(f'Mystring is {msg1} {msg2}') 