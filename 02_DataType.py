print("""
Python Datatype:
    None
    Text    :   str
    Numeric :   int     float       complex
    Sequence:   List    Tuple       Range
    Set     :   set     frozenset
    Binary  :	bytes   bytearray    memoryview
    Mapping :   Dict
    Bool
""")
# ===============================================
print("=" * 50)
print("None".upper())
print("=" * 50)
# ===============================================

myNone = None
print(f'myNone value = {myNone}')
print(f'type(myNone) = {type(myNone)}')
print(f'isinstance   = {isinstance(myNone, int)}') # Check datatype - return bool
print(f'address = id(myNone) = {id(myNone)}')
print('\n\n')

# ===============================================
print("=" * 50)
print("text".upper())
print("=" * 50)
# ===============================================

# Character is a string with length = 1
myStr = 'a'

# ----- One line str -----
myStr = "I'm Python"
print(f'myStr = {myStr}\n')

myStr = 'He said: "Hello!"'
print(f'myStr = {myStr}\n')

# ----- Multiple lines str -----

myStr = """Lorem ipsum dolor sit myStret,
consectetur adipiscing elit,
sed do eiusmod tempor incididunt
ut labore et dolore magna aliqua."""
print(f'myStr = {myStr}\n')

myStr = '''Lorem ipsum dolor sit amet,
consectetur adipiscing elit,
sed do eiusmod tempor incididunt
ut labore et dolore magna aliqua.'''
print(f'myStr = {myStr}\n')

# ----- Str function -----

print('#' * 10)

a = 'Hello World!'


print("------ sub str ------")
print(a)
print(a[:])
print(a[2:5]) # get a string from index 2 to index 5 (not include value at index 5)
print(a[5:]) # get a string from index 5 to the end
print(a[:5]) # get a string from beginning to index 5

print(a[-5:-2])

print("------ length ------")
print(len(a))

print("------ remove white space before and after string ------")
a = "   Hello World!        "


print(a)

print(f'a.strip() = {a.strip()}')   #remove white space before and after string

print(f'a.lower() = {a.lower()}')   # lower all case

print(f'a.upper() = {a.upper()}')   # upper all case

print(f'a.title = {a.title()}')

print(f'a.find("e") = {a.find("e")}') # return index
print(f'a.find("ee") = {a.find("ee")}') # not found, return -1


print("------ replace ------")
print(r"Python does not allow change directly in string index like str[0] = 'r'")
a = "aa bb cc dd aaa bbb ccc ddd"
print (a.replace("a", "o"))     # replace all "a" to "o"
print (a.replace("bb", "**"))   # replace all "bb" to "**"

print("------ split ------")
a = "aa bb cc dd aaa bbb ccc ddd"
print (a.split(" "))     # replace all "a" to "o"
b = a.split(" ")
print(b[0])
# print (a.replace("bb", "**"))   # replace all "bb" to "**"

print("------ check value in/not in string ------")
a = "aa bb cc dd aaa bbb ccc ddd"
x = "a" in a
print(x)        # true
y = "cc" not in a
print(y)        # false

print("------ str concatenation ------")
a = "aa bb cc dd"
b = "aaa bbb ccc ddd"
c = a + " " + b
print(c)


print("------ str escapse character ------")

    # \'	Single Quote	
    # \\	Backslash	
    # \n	New Line	
    # \r	Carriage Return	
    # \t	Tab	
    # \b	Backspace	
    # \f	Form Feed	
    # \ooo	Octal value	
    # \xhh	Hex value

print("The \\ is the escapse character for \"string \" output")

print('\n\n')


# ===============================================
print("=" * 50)
print("numberic".upper())
print("=" * 50)
# ===============================================

# ----- int -----

num = 5 # variable is case sensitive
print(f"type(5) \t = {type(num)} \t value num = {num} \t\t address = {id(num)}")

# ----- float -----

num = 5.0
print(f"type(5.0) \t = {type(num)} \t value num = {num} \t address = {id(num)}")

# ----- complex -----

num = 5.0 + 2j
print(f"type(5.0 + 2j) \t = {type(num)} \t value num = {num} \t address = {id(num)}")

# ----- Sciencetific notation e -----

x = 35e3
y = 12E4
z = -87.7e100

print(type(x))
print(type(y))
print(type(z))

print()

# ----- Random Number -----
import random
print(random.randrange(1, 10))

# ********************
print("*" * 20)
print("cast type".upper())
print("*" * 20)
# ********************

a = 5.6
b = int(a)
print(f"type of int(5.6) \t = {type(b)} \t value of b = {b}")

k = float(b)
print(f"type of float(5) \t = {type(k)} \t value of k = {k}")

k = 6.0
c = complex (b, k)
print(f"type of complex(5, 6.0)  = {type(c)} \t value of k = {c}")
print()

print("Swap value 2 variable")
a = 5.6
b = 10
print(f"a = {a}")
print(f"b = {b}")

a, b = b, a
print(f"a = {a}")
print(f"b = {b}")
print()

# same value -> same address
x     = 'string variable'
y = z = "string variable"

print(f"address = id(x) = {id(x)}")
print(f"address = id(y) = {id(y)}")
print(f"address = id(z) = {id(z)}")

print('\n\n')

# ===============================================
print("=" * 50)
print(f"sequence".upper())
print("=" * 50)
# ===============================================

# ----- list -----

myList = [1, 3, 5, 7]
print(f"type of myList      = {type(myList)}    value = {myList}    \t address = {id(myList)}")
myList = list((1, 3, 5, 7))
print(f"type of myList      = {type(myList)}    value = {myList}    \t address = {id(myList)}")

# ----- tuple -----

myTuple = (1, 3, 5, 7)
print(f"type of myTuple     = {type(myTuple)}   value = {myTuple}  \t\t address = {id(myTuple)}")
myTuple = tuple((1, 3, 5, 7))
print(f"type of myTuple     = {type(myTuple)}   value = {myTuple}  \t\t address = {id(myTuple)}")

# ----- range -----

myRange = range(0, 10)
print(f"type of myRange     = {type(myRange)}   value = {myRange}  \t\t address = {id(myRange)}")

# ----- access element by list method -----

print()
print(f"All value in range(0, 10) is {list(myRange)}")

myRange = range(1, 10, 2)
print(f"All value in range(1, 10, 2) is {list(myRange)}")
print('\n\n')




# ===============================================
print("=" * 50)
print(f"set".upper())
print("=" * 50)
# ===============================================

mySet = {1, 3, 5, 7}
print(f"type of mySet       = {type(mySet)}     value = {mySet}     \t address = {id(mySet)}")

mySet = set((1, 3, 5, 7))
print(f"type of mySet       = {type(mySet)}     value = {mySet}     \t address = {id(mySet)}")

mySet = frozenset ((1, 3, 5, 7))
print(f"type of mySet       = {type(mySet)}     value = {mySet}     \t address = {id(mySet)}")

print('\n\n')
# ===============================================
print("=" * 50)
print(f"binary".upper())
print("=" * 50)
# ===============================================

# ----- bytes -----
x = bytes(5)
print ("Type of x is : ")
print(type(x))
print("\n")

# ----- bytearray -----

x = bytearray(5)
print ("Type of x is : ")
print(type(x))
print("\n")

# ----- memoryview -----

x = memoryview(bytes(5))
print ("Type of x is : ")
print(type(x))
print("\n")

print('\n\n')
# ===============================================
print("=" * 50)
print(f"mapping".upper())
print("=" * 50)
# ===============================================

d = {
        'brandName': 'samsung', 
        'model': 'galaxy s10',
        'year' : 2020,
    }
print(f"Dictionary d        = {d}")
print(f'type(d)             = {type(d)}')
print(f'address = id(d)     = {id(d)}')
print(f"d.keys()            = {d.keys()}")
print(f"d.values()          = {d.values()}")
print(f"d['brandName']      = {d['brandName']}")
print(f"d.get('brandName')  = {d.get('brandName')}")

print('\n\n')

d = dict(
            brandName =  'samsung', 
            model     =  'galaxy s10',
            year      =   2020,
        )
print(f"Dictionary d        = {d}")
print(f'type(d)             = {type(d)}')
print(f'address = id(d)     = {id(d)}')
print(f"d.keys()            = {d.keys()}")
print(f"d.values()          = {d.values()}")
print(f"d['brandName']      = {d['brandName']}")
print(f"d.get('brandName')  = {d.get('brandName')}")

print('\n\n')

# ===============================================
print("=" * 50)
print(f"bool".upper())
print("=" * 50)
# ===============================================

myBool = True
print(f"type(true) \t = {type(myBool)} \t value myBool = {myBool} \t address = {id(myBool)}")
print("bool of all value is true except empty and {}".upper().format(0))  # upper cannot cast number 0
print(f"bool('Hello') = {bool('Hello')}")
print(f"bool(15) = {bool(15)}")
print(f"bool([]) = {bool([])}")
print(f"bool(0) = {bool(0)}")