"""
Lexer = Lexical Analyser
     Break source code to token that identify by the language
     1. Read source code
     2. Break to word list
     3. Initial datatype to every word in the list - Make token
"""
d = {'mykey1': 'myvalue1', 'mykey2': 'myvalue2'}
# print(d)
# k = d.keys()
# l = []
# for i in d.keys():
#      l.append(i)

# print('l = ', l)
# print('k = ', k)
# print(f'{list(d.keys())}\t = \t {list(d.values())}\n')
# print(f'd.items() = ', d.items())
# for key, value in d.iteritems() :
#     print (f'{key} , {value}')

# print(d.keys())
# print(d.values())
# a = int('2')
# print(a)
# print(int('2'))
# b = float('2.3')
# print(b)
# print(int("2.2",10))
# ===============================================
# print("=" * 50)
# print(f"Declare function".upper())
# print("=" * 50)
# ===============================================
def removeComment(sourceCode): pass
def isIdentifier(lexeme): pass
def numberHandler(numberString): pass
# def isInt(intString): pass
# def isFloat(floatString): pass
# def brackets (sourceCode, seperator):
     # brackets = []
     # bracketsCheck = True
     # for i in sourceCode:
     #      if i == '(' or i == '{' or i =='[':
     #           brackets.append(i)
     #      if i == ')':
     #           if brackets[-1] == separator['closeParenthesis']:
     #                brackets.pop()
     #           else:
     #                bracketsCheck = False
     #                print('closeParenthesis miss match')
     #                break
     #      if i == '}':
     #           if brackets[-1] == separator['closeBrace']:
     #                brackets.pop()
     #           else:
     #                bracketsCheck = False
     #                print('closeBrace miss match')
     #                break
     #      if i == ']':
     #           if brackets[-1] == separator['closeBracket']:
     #                brackets.pop()
     #           else:
     #                bracketsCheck = False
     #                print('closeBracket miss match')
     #                break
     # if len(brackets) != 0:
     #      bracketsCheck = False
     #      print ('Separator miss match')




class Lexer(object):
     def __init__(self, sourceCode):
          self.sourceCode = sourceCode

     # tokenize method - create token from file input
     def tokenize(self):
          # print('This line in tokenize')
          

          # Define keyword
          keywordLib =   [
          'int', 
          'float', 
          'bool', 
          'true', 
          'false', 
          'if', 
          'else', 
          'then', 
          'endif', 
          'while', 
          'whileend', 
          'do', 
          'doend', 
          'for', 
          'forend', 
          'input', 
          'output', 
          'and', 
          'or', 
          'not',
          ]

          # Define Operator
          operator = [
               '+',
               '-',
               '*',
               '/',
               '=',
               '>',
               '<',
               '%',
               '==',
               '>=',
               '<=',
          ]
         
          # Define Separator
          separator = {

                    # '(){}[],.:;
               'singleQuote'        : "'",
               'openParenthesis'    : '(',
               'closeParenthesis'   : ')',
               'openBrace'          : '{',
               'closeBrace'         : '}',
               'openBracket'        : '[',
               'closeBracket'       : ']',
               'comma'              : ',',
               'semicolon'          : ';',
          }
          
          sourceCode = self.sourceCode

          # ===============================================
          # print("=" * 50)
          # print(f"Step2: Remove all comment".upper())
          # print("=" * 50)
          # ===============================================
          sourceCode, checkSingleQuotes = removeComment(sourceCode)
          # print('checkSingleQuotes = ', checkSingleQuotes)

          # Check brackets match =================================================================
          # print("separator['openParenthesis'] = ", separator['openParenthesis'])
          # brackets = []
          # # print('brackets[-1] = ', brackets[-1])
          # checkBrackets = True
          # for i in sourceCode:
          #      if i == '(' or i == '{' or i =='[':
          #           brackets.append(i)
          #           # print('brackets = ', brackets)
          #           # print('brackets[-1] = ', brackets[-1])
          #           continue
          #      if i == ')':
          #           if len(brackets) > 0:
          #                if brackets[-1] == separator['openParenthesis']:
          #                     # print('brackets = ', brackets)
          #                     brackets.pop()
          #                     # print('brackets = ', brackets)
          #                     # print('len(brackets) = ', len(brackets))
          #                     continue
          #                else:
          #                     checkBrackets = False
          #                     print('closeParenthesis miss match')
          #                     break
          #           else:
          #                checkBrackets = False
          #                print('There are too many Close Parenthesis')
          #                break
          #      if i == '}':
          #           if len(brackets) > 0:
                    
          #                if brackets[-1] == separator['openBrace']:
          #                     # print('brackets = ', brackets)
          #                     brackets.pop()
          #                     # print('brackets = ', brackets)
          #                     continue
          #                else:
          #                     checkBrackets = False
          #                     print('closeBrace miss match')
          #                     break
          #           else:
          #                checkBrackets = False
          #                print('There are too many Close Brace')
          #                break
          #      if i == ']':
          #           if len(brackets) > 0:
          #                if brackets[-1] == separator['openBracket']:
          #                     brackets.pop()
          #                     continue
          #                else:
          #                     checkBrackets = False
          #                     print('closeBracket miss match')
          #                     break
          #           else:
          #                checkBrackets = False
          #                print('There are too many Close Bracket')
          #                break
          # if len(brackets) != 0:
          #      checkBrackets = False
          #      print ('Separator miss match')
          # End brackets check =================================================================



          # print('checkBrackets = ', checkBrackets)
          # print('checkSingleQuotes = ', checkSingleQuotes)
          # if checkBrackets & checkSingleQuotes == True:

          # create separatorList from separator dictionary
          separatorList = list(separator.values())
          # print('separatorList = ', separatorList)

          allSpecialKeys = operator + separatorList

          # All lexeme will stored in lexeme list 
          lexeme = []

          # Split source file to words and store in wordList
          wordList = sourceCode.split()
     
          # Check every single word in word list and append to lexeme
          for word in wordList:

               # Check whole word is key word, word not contain key =============
               if word in keywordLib:
                    lexeme.append({'KEYWORD': f'{word}'})
                    continue

               # Check whole word is operator
               if word in operator:
                    lexeme.append({'OPERATOR': f'{word}'})
                    continue

               # Check whole word is separator
               if word in separatorList:
                    lexeme.append({'SEPARATOR': f'{word}'})
                    continue

               # Check whole word is number
               isNumber, value, dataType = numberHandler(word)
               if isNumber == True:
                    lexeme.append({f'{dataType}': f'{value}'})
                    continue

               # Check word not contain any key = should be identifier
               isExistKey = False
               for key in allSpecialKeys:
                    if key in word:
                         isExistKey = True
                         break
               if isExistKey == False:
                    if isIdentifier(word) == True:
                         lexeme.append({'IDENTIFIER': f'{word}'})
                    else:
                         print('whole keyword identifier error')
                    continue

               # Word contain key ==============================================
               begin = 0
               i = 0

               # print('len(word) = ', len(word))
               while i < len(word):
                    # print('Start while loop i = ', i)
                    # print('Start while loop len(word) = ', len(word))
                    # print('len(word[begin:i]) = ', len(word[begin:i]))

                    # double key word Operator
                    if i + 1 < len(word) and (word[i] + word[i+1]) in operator:

                         # whatever before keyword is a token
                         if len(word[begin:i]) >= 1 :
                              isNumber, value, dataType = numberHandler(word[begin:i])
                              if isNumber == True:
                                   lexeme.append({f'{dataType}': f'{value}'})

                              elif isIdentifier(word[begin:i]) == True:
                                   lexeme.append({'IDENTIFIER': f'{word[begin:i]}'})
                              else:
                                   print('Identifer before double keyword is not qualify')

                         # Double keyword is a token
                         lexeme.append({'OPERATOR': f'{word[i]+word[i+1]}'})

                         begin = i+2
                         i = begin

                    # single keyword Operator
                    elif word[i] in operator: 
                         # print ('i in SINGLE keyword BEFPORE process = ', i)

                         # Whatever before i is a Lexeme
                         if len(word[begin:i]) >= 1:

                              isNumber, value, dataType = numberHandler(word[begin:i])
                              if isNumber == True:
                                   lexeme.append({f'{dataType}': f'{value}'})

                              elif isIdentifier(word[begin:i]) == True:
                                   lexeme.append({'IDENTIFIER': f'{word[begin:i]}'})
                              else:
                                   print('Identifer before Single Operator is not qualify')

                              

                         # Single keyword is a Operator
                         lexeme.append({'OPERATOR': f'{word[i]}'})

                         begin = i+1
                         i = begin
                    
                    # Separator
                    elif word[i] in separatorList: 

                         # Whatever before i is a Identifier
                         if len(word[begin:i]) >= 1:
                              isNumber, value, dataType = numberHandler(word[begin:i])
                              if isNumber == True:
                                   lexeme.append({f'{dataType}': f'{value}'})
                              elif isIdentifier(word[begin:i]) == True:
                                   lexeme.append({'IDENTIFIER': f'{word[begin:i]}'})
                              else:
                                   print('Identifer before Single Separator is not qualify')

                         # Single keyword is a Separator
                         lexeme.append({'SEPARATOR': f'{word[i]}'})

                         begin = i+1
                         i = begin

                    else:
                         # no key word found, from the last keyword to end
                         if i == len(word) - 1:
                                   if len(word[begin:(i+1)]) >= 1:
                                        # print('word = ', word)
                                        # print('begin = ', begin)
                                        # print('i + 1 = ', i + 1)
                                        # print('len(word) - 1 = ', len(word) - 1)
                                        isNumber, value, dataType = numberHandler(word[begin:(i+1)])
                                        if isNumber == True:
                                             lexeme.append({f'{dataType}': f'{value}'})
                                        elif isIdentifier(word[begin:i+1]) == True:
                                             lexeme.append({'IDENTIFIER': f'{word[begin:(i+1)]}'})
                                        else:
                                             print('Identifer after last key word is not qualify aaa')

                                        i += 1

                         else:
                              i += 1
               
          

          return lexeme

          # else:
          #      print('Separator miss match')

# ===============================================
# print("=" * 50)
# print(f"Define function".upper())
# print("=" * 50)
# ===============================================

def removeComment(sourceCode):
     if '!' in sourceCode:
          # commentIdx store all index of '!' in sourceCode
          commentIdx = []
          for i in range(len(sourceCode)):
               if sourceCode[i] == '!':
                    commentIdx.append(i)

          # Check for miss match '!' pair
          if len(commentIdx) % 2 != 0:
               # print("'!' pair miss match")
               return -1, False
          else:
               if len(commentIdx) >= 2:
                    # print('commentIdx = ', commentIdx)
                    i = 0
                    while i < len(commentIdx):
                         # print('i = ', i)
                         begin = commentIdx[i]
                         end = commentIdx[i+1]
                         # print('begin = ', begin)
                         # print('end = ', end)
                         sourceCode = sourceCode.replace(sourceCode[begin:end], (int(end) - int(begin))*' ')
                         i += 2
                         
                    # print('sourceCode = ', sourceCode)
                    return sourceCode, True
     else:
          return sourceCode, True
# print('This line in Lexer')

# def isExistKey(word, *key):


def isIdentifier(lexeme):
     if lexeme[0].isalpha() or lexeme[0] == '_':
          # print('first caracter is qualify')
          i = 1
          for i in range(len(lexeme)):
               # print('this line in for loop of lexeme')
               if lexeme[i].isalnum() or lexeme[i] == '_':
                    i += 1
                    continue
               else:
                    # print (lexeme, ' is not idetifier')
                    return False
          # print(lexeme, ' is an identifier')
          return True

def numberHandler(numString):
     try:
        numInt = int(numString)
        return True, numInt, "INT"
     except ValueError:
          try:
               numFloat = float(numString)
               return True, numFloat, "FLOAT"
          except ValueError:
               return False, -1, "Not Number"
