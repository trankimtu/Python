# ===============================================
print("=" * 50)
print(f"break".upper())
print("=" * 50)
# ===============================================

for i in range(5):
    if i == 3:
        break
    else:
        print(f'i = {i}')
        
# ===============================================
print("=" * 50)
print(f"continue".upper())
print("=" * 50)
# ===============================================

for i in range(5):
    if i == 3:
        continue
    else:
        print(f'i = {i}')
# ===============================================
print("=" * 50)
print(f"pass".upper())
print("=" * 50)
# ===============================================

for i in range(5):
    if i == 3:
        pass # don't know what to do yet, use pass
    else:
        print(f'i = {i}')

print("Pass is used to keep function empty when don't know what to do yet")    
def myFunction():
    pass