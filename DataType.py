"""
Python Datatype:
    None
    Numeric
        int
        float
        complex
        bool
    Sequence
        List
        Tuple
        Set
        String
        Range
    Dictionary

"""
print("=" * 50)
print(f"numberic".upper())
print("=" * 50)

num = 5
print(f"type(5) \t = {type(num)} \t value num = {num}")

num = 5.0
print(f"type(5.0) \t = {type(num)} \t value num = {num}")

num = 5.0 + 2j
print(f"type(5.0 + 2j) \t = {type(num)} \t value num = {num}")

num = True
print(f"type(true) \t = {type(num)} \t value num = {num}")


print("*" * 20)
print(f"cast type".upper())
print("*" * 20)

a = 5.6
b = int(a)
print(f"type of int(5.6) \t = {type(b)} \t value of b = {b}")

k = float(b)
print(f"type of float(5) \t = {type(k)} \t value of k = {k}")

k = 6.0
c = complex (b, k)
print(f"type of complex(5, 6.0)  = {type(c)} \t value of k = {c}")

print("Swap 2 number")
a = 5.6
b = 10
print(f"a = {a}")
print(f"b = {b}")

a, b = b, a
print(f"a = {a}")
print(f"b = {b}")

# ===============================================
print("=" * 50)
print(f"sequence".upper())
print("=" * 50)
# ===============================================

myList = [1, 3, 5, 7]
print(f"type of myList \t = {type(myList)} \t value = {myList}")

myTuple = (1, 3, 5, 7)
print(f"type of myTuple  = {type(myTuple)} \t value = {myTuple}")

mySet = {1, 3, 5, 7}
print(f"type of mySet \t = {type(mySet)} \t value = {mySet}")

myRange = range(0, 10)
print(f"type of myRange  = {type(myRange)} \t value = {myRange}")
print(f"All value in range(0, 10) is {list(myRange)}")

myRange = range(1, 10, 2)
print(f"All value in range(1, 10, 2) is {list(myRange)}")


# ===============================================
print("=" * 50)
print(f"dictionary".upper())
print("=" * 50)
# ===============================================

d = {
        'brandName': 'samsung', 
        'model': 'galaxy s10',
        'year' : 2020,
    }
print(f"Dictionary d = {d}")
print(f"d.keys() = {d.keys()}")
print(f"d.values() = {d.values()}")
print(f"d['brandName'] = {d['brandName']}")
print(f"d.get('brandName') = {d.get('brandName')}")