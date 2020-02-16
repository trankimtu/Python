"""
Lexer = Lexical Analyser
     Break source code to token that identify by the language
     1. Read source code
     2. Break to word list
     3. Initial datatype to every word in the list - Make token
"""
def remove_comment(source_code):
     if '!' in source_code:
          # commentIdx store all index of '!' in source_code
          commentIdx = []
          for i in range(len(source_code)):
               if source_code[i] == '!':
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
                         source_code = source_code.replace(source_code[begin:end], (int(end) - int(begin))*' ')
                         i += 2
                         
                    # print('source_code = ', source_code)
                    return source_code, True
     else:
          return source_code, True
# print('This line in Lexer')

def identifier(word):
     if word[0] == '_' or word[0]:
          pass
# def brackets (source_code, seperator):
     # brackets = []
     # bracketsCheck = True
     # for i in source_code:
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
     def __init__(self, source_code):
          self.source_code = source_code

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
          
          source_code = self.source_code

          # Remove comment
          source_code, checkSingleQuotes = remove_comment(source_code)
          # print('checkSingleQuotes = ', checkSingleQuotes)

          # Check brackets match
          # print("separator['openParenthesis'] = ", separator['openParenthesis'])
          brackets = []
          # print('brackets[-1] = ', brackets[-1])
          checkBrackets = True
          for i in source_code:
               if i == '(' or i == '{' or i =='[':
                    brackets.append(i)
                    # print('brackets = ', brackets)
                    # print('brackets[-1] = ', brackets[-1])
                    continue
               if i == ')':
                    if len(brackets) > 0:
                         if brackets[-1] == separator['openParenthesis']:
                              # print('brackets = ', brackets)
                              brackets.pop()
                              # print('brackets = ', brackets)
                              # print('len(brackets) = ', len(brackets))
                              continue
                         else:
                              checkBrackets = False
                              print('closeParenthesis miss match')
                              break
                    else:
                         checkBrackets = False
                         print('There are too many Close Parenthesis')
                         break
               if i == '}':
                    if len(brackets) > 0:
                    
                         if brackets[-1] == separator['openBrace']:
                              # print('brackets = ', brackets)
                              brackets.pop()
                              # print('brackets = ', brackets)
                              continue
                         else:
                              checkBrackets = False
                              print('closeBrace miss match')
                              break
                    else:
                         checkBrackets = False
                         print('There are too many Close Brace')
                         break
               if i == ']':
                    if len(brackets) > 0:
                         if brackets[-1] == separator['openBracket']:
                              brackets.pop()
                              continue
                         else:
                              checkBrackets = False
                              print('closeBracket miss match')
                              break
                    else:
                         checkBrackets = False
                         print('There are too many Close Bracket')
                         break
          if len(brackets) != 0:
               checkBrackets = False
               print ('Separator miss match')




          print('checkBrackets = ', checkBrackets)
          print('checkSingleQuotes = ', checkSingleQuotes)
          if checkBrackets & checkSingleQuotes == True:

               separatorList = list(separator.values())
               print('separatorList = ', separatorList)
               allSpecialKeys = operator + separatorList

               # All tokens will stored in tokens list 
               tokens = []

               # Split source file to words and store in wordList
               wordList = source_code.split()
          
               # Check every single word in word list and append to tokens
               for word in wordList:

                    # Check whole word is key word
                    if (word in keywordLib) or (word in allSpecialKeys):
                         tokens.append(word)
                         continue

                    # Check word not contain any key = should be identifier
                    isExistKey = False
                    for key in allSpecialKeys:
                         if key in word:
                              isExistKey = True
                              break
                    if isExistKey == False:
                         tokens.append(word)
                         continue

                    # Word contain key
                    begin = end = 0
                    # print ('word[begin:] = ', word[begin:])
                    
                    i = 0
                    # print('len(word) = ', len(word))
                    while i < len(word):
                         # print('Start while loop i = ', i)
                         # print('Start while loop len(word) = ', len(word))
                         # print('len(word[begin:i]) = ', len(word[begin:i]))

                         # double key word
                         if i + 1 < len(word) and (word[i] + word[i+1]) in allSpecialKeys:
                              # print ('i in DOUBLE keyword BEFPORE process = ', i)
                              # print ('double key = ', word[i] + word[i+1])

                              # whatever before keyword is a token
                              if len(word[begin:i]) >= 1 :
                                   tokens.append(word[begin:i])

                              # Double keyword is a token
                              tokens.append(word[i]+word[i+1])

                              begin = i+2
                              i = begin
                              # print ('i in DOUBLE keyword AFTER process = ', i)
                              # print('word[i] = ', word[i])

                         # single keyword
                         elif word[i] in allSpecialKeys:
                              # print ('i in SINGLE keyword BEFPORE process = ', i)

                              # Whatever before i is a token
                              if len(word[begin:i]) >= 1:
                                   tokens.append(word[begin:i])

                              # Single keyword is a token
                              tokens.append(word[i])

                              begin = i+1
                              i = begin
                              # print ('i in SINGLE keyword AFTER process = ', i)
                              # print ('word[i] = ', word[i])
                         else:
                              # from the last keyword to end
                              if i == len(word) - 1:
                                    if len(word[begin:(i+1)]) >= 1:
                                        tokens.append(word[begin:(i+1)])
                                        i += 1

                              else:
                                   i += 1
                    
               print('tokens  = ', tokens)
     
               return tokens

          else:
               print('Separator miss match')

