from Lexer import *
# import Lexer
def openSourceFile(fileName):
    # ===============================================
    # print("=" * 50)
    # print(f"Read Source code from file".upper())
    # print("=" * 50)
    # ===============================================

    with open(fileName, 'r') as file:
        content = file.read()

    # Another syntax open file
    # sourceFile = open('test.lang', 'r') 
    # content = sourceFile.read() 
    # print(content)

    return content



def main():
    # ===============================================
    # print("=" * 50)
    # print(f"Start main".upper())
    # print("=" * 50)
    # ===============================================


    content = openSourceFile('test.lang')
    # print('content = ', content)

    # Lexer
    # Call Lexer class, initialize with sour code
    lex = Lexer(content)
    lex.tokenize()


    
main()





# f = open('test.lang', 'r')  
# print('f.read() = ', f.read())    # After read, current cursor at the end of file, readline will get nothing
# f = open('25_myFile.txt', 'r')  


# print(f)
# print('='*10)

# # fetch data
# print('f.read() = ', f.read())    # After read, current cursor at the end of file, readline will get nothing

# print('f.readline() = ', f.readline())
# print('f.readline() = ', f.readline())
# print('f.readline() = ', f.readline(10))    # read 10 first char of line 3

# myFile = open('test.lang', 'r')
# print('myfile = ', myFile.read())