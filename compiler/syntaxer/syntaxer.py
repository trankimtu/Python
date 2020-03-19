class Syntaxer (object):
    def __init__(self, *arg):
        self.lexemes = arg
        # print('arg = ', arg)

    # statemenize method - create statement list from lexemes
    def syntaxer(self):
        lexemes = list(self.lexemes[0])
        # lexemes = [subject 
        #            for lexeme in self.lexemes
        #            for subject in lexeme]
        # print('before while')
        # print ('len = ', len(lexemes))
        # print ('lexemes = ', lexemes)
        # print()
        # print ('lexemes[0] = ', lexemes[0])
        # print ('list(lexemes[0]) = ', list(lexemes[0]))

        # print ('lexemes[0].keys()', lexemes[0].keys())
        # print ('list(lexemes[0].keys())', list(lexemes[0].keys()))
        # print ('list(lexemes[0].values())', list(lexemes[0].values()))
        # print ('list(lexemes[0].keys())[0]', list(lexemes[0].keys())[0])
        # print ('list(lexemes[0].values())[0]', list(lexemes[0].values())[0])
       
        
        # types = ['int', ]   
        begin = 0
        i = 0

        print('begin before while = ', begin)
        print('begin before while = ', begin)
        print('begin before while = ', begin)
        print('begin before while = ', begin)
        print('begin before while = ', begin)
        print('begin before while = ', begin)
        print('begin before while = ', begin)
        print('begin before while = ', begin)
        print('begin before while = ', begin)
        print('begin before while = ', begin)



        print()


        
        while begin < len(lexemes) and begin >= 0:

            isCheck, result, newBegin = checkAllRules(lexemes, begin)


            print('isCheck = ', isCheck)
            print('isResult = ', result)
           
            begin = newBegin
            print('\n\n')


        print('after while')
        # print (semicolonIndex)
        # for i in statementList:
        #     print (f'{i}\n')

# ==============================================
# End class here
# ==============================================

def checkAllRules(arg, begin):
    # print('My arg = ', arg)
    print('begin in checkAllRules = ', begin)

    isDeclare, resultDeclare, newBegin = isDeclaration (arg, begin)
    isDefined1, resultDefine1, newBegin = isDefine1 (arg, begin)
    isDefined2, resultDefine2, newBegin = isDefine2 (arg, begin)

    print('isDeclare = ', isDeclare)
    print('isDefined1 = ', isDefined1)
    print('isDefined2 = ', isDefined2)

    # Check declaration : int a --------------
    if isDeclare:
        newBegin = begin + 3
        return isDeclare, resultDeclare, newBegin



    # Check define1 : a = 1 --------------
    # isDefined1 = False
    if isDefine1:
        newBegin = begin + 4
        return isDefined1, resultDefine1, newBegin



    # # Check define2 : a = b --------------
    # isDefined2 = False
    if isDefine2:
        newBegin = begin + 4


        return isDefined2, resultDefine2, newBegin





    else:
        print ('Something go wrong')
        print ('Something go wrong')
        print ('Something go wrong')
        print ('Something go wrong')
        print ('Something go wrong')
        print ('Something go wrong')
        print ('Something go wrong')
        begin = 99999999999999999
        return -1, -2, begin



def getKeyValue (mydict):
    print('dict = ', mydict)
    for key, value in mydict.items():
        return key, value


# <Declaration> -> <Type> <IDs>;        Example : int a
def isDeclaration (arg, begin):
    myType = ['int', 'float', 'bool']
    print('begin in isDeclaration = ', begin)
    print('arg in isDeclaration = ')
    for i in arg:
        print(f'{i}')
    print()


    print(f'arg[{begin}] = ', arg[begin])
    print(f'arg[{begin + 1}] = ', arg[begin + 1])
    print(f'arg[{begin + 2}] = ', arg[begin + 2])
    print()

    key0, value0 = getKeyValue(arg[begin])
    key1, value1 = getKeyValue(arg[begin + 1])
    key2, value2 = getKeyValue(arg[begin + 2])

    print()
    print('key0   = ', key0)
    print('value0 = ', value0)
    print()
    print('key1   = ', key1)
    print('value1 = ', value1)
    print()
    print('key2   = ', key2)
    print('value2 = ', value2)
    print()

    if (value0 in myType) and key1 == 'IDENTIFIER' and value2 == ';':
        result = {
            'Token': 'Declaration',
            'Lexeme': '',
            'BNF': '<Declaration> -> <Type> <IDs> ;'
        }
        # begin = begin + 3
        return True, result, begin
    else:
        return False, -1, 999999999999
  
# <A1> -> <ID> = <NUM> ;      a = 1
# <Define> -> <IDs> = <NUM> ;       Example: a = 1
def isDefine1 (arg, begin):
    print()
    print('begin in isDefine1 = ', begin)
    print('arg in isDefine1 = ')
    for i in arg:
        print(f'{i}')
    print()
    myNum = ['INT', 'FLOAT']
    myBool = ['true', 'false']


    print(f'arg[{ begin }] = { arg[begin] }')
    print(f'arg[{ begin + 1 }] = { arg[begin + 1] }')
    print(f'arg[{ begin + 2 }] = { arg[begin + 2] }')
    print(f'arg[{ begin + 3 }] = { arg[begin + 3] }')
    print()

    key0, value0 = getKeyValue(arg[begin])
    key1, value1 = getKeyValue(arg[begin + 1])
    key2, value2 = getKeyValue(arg[begin + 2])
    key3, value3 = getKeyValue(arg[begin + 3])

    print()
    print('key0   = ', key0)
    print('value0 = ', value0)
    print()
    print('key1   = ', key1)
    print('value1 = ', value1)
    print()
    print('key2   = ', key2)
    print('value2 = ', value2)
    print()
    print('key3   = ', key3)
    print('value3 = ', value3)
    print()


    if key0 == 'IDENTIFIER' and value1 == '=' and value2 in myBool and value3 == ';':
        result = {
            'Token': 'Define',
            'Lexeme': '',
            'BNF': '<Define> -> <Identifier>  = true/false ;'
        }
        begin = begin + 4
        return True, result, begin
    elif key0 == 'IDENTIFIER' and value1 == '=' and key2 in myNum and value3 == ';':
        result = {
            'Token': 'Define',
            'Lexeme': '',
            'BNF': '<Define> -> <Identifier>  = number ;'
        }
        # begin = begin + 4
        return True, result, begin
    else:
        return False, -1, 9999999999



# <A2> -> <ID> = <ID> ;       a = b
def isDefine2 (arg, begin):



    print()
    print('arg in isDefine2 = ')
    for i in arg:
        print(f'{i}')
    print()

    print('begin in isDefine2 = ', begin)

    print(f'arg[{ begin }] = { arg[begin] }')
    print(f'arg[{ begin + 1 }] = { arg[begin + 1] }')
    print(f'arg[{ begin + 2 }] = { arg[begin + 2] }')
    print(f'arg[{ begin + 3 }] = { arg[begin + 3] }')
    print()

    key0, value0 = getKeyValue(arg[begin])
    key1, value1 = getKeyValue(arg[begin + 1])
    key2, value2 = getKeyValue(arg[begin + 2])
    key3, value3 = getKeyValue(arg[begin + 3])

    print()
    print('key0   = ', key0)
    print('value0 = ', value0)
    print()
    print('key1   = ', key1)
    print('value1 = ', value1)
    print()
    print('key2   = ', key2)
    print('value2 = ', value2)
    print()
    print('key3   = ', key3)
    print('value3 = ', value3)
    print()


    if key0 == 'IDENTIFIER' and value1 == '=' and key2 == 'IDENTIFIER' and value3 == ';':
        result = {
            'Token': 'Define2',
            'Lexeme': '',
            'BNF': '<Define2> -> <Identifier>  = <Identifier> ;'
        }
        # begin = begin + 4
        return True, result, begin
    
    else:
        return False, -1, 9999999999












    # print()
    # print('arg in isDefine2 = ')
    # for i in arg:
    #     print(f'{i}')
    # print()
    # print('begin in isDefine2 = ', begin)
    # print('arg length = ', len(arg))

    # print(f'arg[{ begin }] = { arg[begin] }')
    # print(f'arg[{ begin + 1 }] = { arg[begin + 1] }')
    # print(f'arg[{ begin + 2 }] = { arg[begin + 2] }')
    # print(f'arg[{ begin + 3 }] = { arg[begin + 3] }')
    # print()

    # key0, value0 = getKeyValue(arg[begin])
    # key1, value1 = getKeyValue(arg[begin + 1])
    # key2, value2 = getKeyValue(arg[begin + 2])
    # key3, value3 = getKeyValue(arg[begin + 3])

    # print()
    # print('key0 = ', key0)
    # print('key1 = ', key1)
    # print('key2 = ', key2)
    # print('key3 = ', key3)
    # print()

    # print('value0 = ', value0)
    # print('value1 = ', value1)
    # print('value2 = ', value2)
    # print('value3 = ', value3)
    # if key0 == 'IDENTIFIER' and value1 == '=' and key2 == 'IDENTIFIER' and value3 == ';':
    #     result = {
    #         'Token': 'Define',
    #         'Lexeme': '',
    #         'BNF': '<Define> -> <Identifier>  = <Identifier> ;'
    #     }
    #     begin = begin + 4
    #     return True, result, begin
    
    # else:
    #     return False, -1, 9999999999
