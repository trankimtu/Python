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

        # print('begin before while = ', begin)
        # print('begin before while = ', begin)
        # print('begin before while = ', begin)
        # print('begin before while = ', begin)
        # print('begin before while = ', begin)
        # print('begin before while = ', begin)
        # print('begin before while = ', begin)
        # print('begin before while = ', begin)
        # print('begin before while = ', begin)
        # print('begin before while = ', begin)


        print(f'begin = {begin}')

        isStatement, result, newBegin = Statement(lexemes, begin)

        print(f'isStatement = {isStatement}')
        print(f'result = {result}')
        print(f'newBegin = {newBegin}')
        # Statement(lexemes, begin)


        print('len(lexemes) = ', len(lexemes))



        
        while begin < len(lexemes) and begin >= 0:

            isCheck, result, newBegin = checkAllRules(lexemes, begin)


            # print('isCheck = ', isCheck)
            print('Result = ', result)
           
            begin = newBegin
            print('\n')


        print('after while')
     

# ==============================================
# End class here
# ==============================================

def Statement(arg, begin):
    print (f'begin in Statement = {begin}')
    IsAssign, AssignResult, AssignBegin = isAssign(arg, begin)
    IsDeclarative, DeclarativeResult, DeclarativeBegin = isDeclarative(arg, begin)
    # isIf(arg, begin)
    # isWhile(arg, begin)
    # isBegin(arg, begin)
    if IsAssign == True:
        IsStatement, stamentResult, statementBegin = IsAssign, result, newBegin
    elif IsDeclarative == True:
        IsStatement, stamentResult, statementBegin = IsDeclarative, DeclarativeResult, DeclarativeBegin
    else:
        print('Not a statement')


    return IsStatement, stamentResult, statementBegin

def isAssign(arg, begin):

    IsID, idKey, idValue = isID(arg[begin])
    if IsID == True:
        opreatorKey, operatorValue = getKeyValue(arg[begin + 1])
        if operatorValue == '=':
            isExpression[begin + 2] =========================================================]


def isDeclarative(arg, begin):
    IsType, typeKey, typeValue = isType(arg[begin])
    IsID, idKey, idValue = isID(arg[begin + 1])
    IsSemicolon = isSemicolon(arg[begin + 2])

    if IsType & IsID & IsSemicolon == True:

        result = {
            'Token': 'Declaration',
            # 'Lexeme': '',
            'BNF': '<Statement> -> <Declarative> \n <Declarative> -> <Type> <id> ;'
        }
        newBegin = begin + 3
        return True, result, newBegin
    else: 
        return False, -1, begin

    
def isIf(arg, begin):
    pass
def isWhile(arg, begin):
    pass
def isBegin(arg, begin):
    pass

def getKeyValue (mydict):
    # print('dict = ', mydict)
    for key, value in mydict.items():
        return key, value


def isType(typeDict):

    # typeKey = list(typeDic.keys())[0]
    # typeValue = list(typeDic.values())[0]

    # print(typeKey)
    # print(typeValue)

    typeKey, typeValue = getKeyValue (typeDict)

    typeList = ['int', 'float', 'bool']

    if typeValue in typeList:
        return True, typeKey, typeValue
    else:
        return False, 'Not Type Key', 'Not Type Value'


def isRelop (relopDict):
    relopKey, relopValue = getKeyValue(relopDict)

    relopList = ['<', '<=', '==', '<>', '>=', '>' ]

    if relopValue in relopList:
        return True, relopValue
    else:
        return False, 'Not a relop'

def isExpression(*arg, begin):
    pass

def isTerm(*arg, begin):
    pass


def isFactor(*arg, begin):
    
    IsID, IdKey, IdValue = isID(arg[begin])
    if IsID == True:
        return True, IdKey, IdValue

    IsNum, numKey, numValue = isNum(arg[begin])
    if IsNum == True:
        return True, numKey, numValue

    
    # openParenthesisKey, openParenthesisValue = getKeyValue(arg[begin])
    # if openParenthesisValue = '(':
    #     IsExpression, expressionEnd = isExpression (arg, begin + 1)




    if len(arg) == 0:
        print("Error, Factor must be provided!")
        return False
    
    if len(arg) == 1:
        print(arg[0].keys())


def isID (idDict):
    # idKey = list(idDic.keys())[0]
    # idValue = list(idDic.values())[0]

    # print(idKey)
    # print(idValue)

    idKey, idValue = getKeyValue(idDict)

    if idKey == 'IDENTIFIER':
        return True, idKey, idValue
    else:
        return False, 'Not ID Key', 'Not ID Value'

def isNum(numDict):

    # numKey = list(numDic.keys())[0]
    # numValue = list(numDic.values())[0]

    # print(numKey)
    # print(numValue)

    numKey, numValue = getKeyValue(numDict)

    numType = ['FLOAT', 'INT']

    if numKey in numType:
        return True, numKey, numValue
    else:
        return False, 'NAN Key', 'NAN Value' 
    
def isSemicolon(semicolonDict):
    semicolonKey, semicolonValue = getKeyValue(semicolonDict)
    # semicolonValue = list(semicolonDic.values())[0]

    # print(numKey)
    # print(numValue)

    if semicolonValue == ';':
        return True
    else:
        return FalsesemicolonValue

















# ========================================================================================
# ignore those stuff bellow
# ========================================================================================


def checkAllRules(arg, begin):
    # print('My arg = ', arg)
    # print('begin in checkAllRules = ', begin)
    # print('len(arg) in checkAllRules = ', len(arg))

    availableLen = len(arg) - begin
    # print('availableLen = ', availableLen)

    # Check declaration : int a; len = 3 --------------
    if availableLen >= 3:

        isDeclare, resultDeclare, newBeginDeclare = isDeclaration (arg, begin)

        if isDeclare:
            newBeginDeclare = begin + 3
            return isDeclare, resultDeclare, newBeginDeclare


    if availableLen >= 4:
        isDefined1, resultDefine1, newBeginDefined1 = isDefine1 (arg, begin)
        isDefined2, resultDefine2, newBeginDefined2 = isDefine2 (arg, begin)
        # print('isDefined1 = ', isDefined1)
        # print('isDefined2 = ', isDefined2)


        # Check define1 : a = 1; len = 4--------------
        # isDefined1 = False
        if isDefined1:
            newBeginDefined1 = begin + 4
            return isDefined1, resultDefine1, newBeginDefined1


        # # Check define2 : a = b; len =4 --------------
        # isDefined2 = False
        elif isDefined2:
            newBeginDefined2 = begin + 4


            return isDefined2, resultDefine2, newBeginDefined2

        else:
            print ('Something go wrong')
            print ('Something go wrong')
            print ('Something go wrong')
            print ('Something go wrong')
            print ('Something go wrong')
            print ('Something go wrong')
            print ('Something go wrong')



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





# <Declaration> -> <Type> <IDs>;        Example : int a
def isDeclaration (arg, begin):
    myType = ['int', 'float', 'bool']
    # print('begin in isDeclaration = ', begin)
    # print('arg in isDeclaration = ')
    # for i in arg:
    #     print(f'{i}')
    # print()


    # print(f'arg[{begin}] = ', arg[begin])
    # print(f'arg[{begin + 1}] = ', arg[begin + 1])
    # print(f'arg[{begin + 2}] = ', arg[begin + 2])
    # print()

    key0, value0 = getKeyValue(arg[begin])
    key1, value1 = getKeyValue(arg[begin + 1])
    key2, value2 = getKeyValue(arg[begin + 2])

    # print()
    # print('key0   = ', key0)
    # print('value0 = ', value0)
    # print()
    # print('key1   = ', key1)
    # print('value1 = ', value1)
    # print()
    # print('key2   = ', key2)
    # print('value2 = ', value2)
    # print()

    if (value0 in myType) and key1 == 'IDENTIFIER' and value2 == ';':
        result = {
            'Token': 'Declaration',
            'Lexeme': '',
            'BNF': '<Declaration> -> <Type> <IDs> ;'
        }
        return True, result, begin
    else:
        return False, -1, 999999999999
  
# <A1> -> <ID> = <NUM> ;      a = 1
# <Define> -> <IDs> = <NUM> ;       Example: a = 1
def isDefine1 (arg, begin):
    # print()
    # print('begin in isDefine1 = ', begin)
    # print('arg in isDefine1 = ')
    # for i in arg:
    #     print(f'{i}')
    # print()
    myNum = ['INT', 'FLOAT']
    myBool = ['true', 'false']


    # print(f'arg[{ begin }] = { arg[begin] }')
    # print(f'arg[{ begin + 1 }] = { arg[begin + 1] }')
    # print(f'arg[{ begin + 2 }] = { arg[begin + 2] }')
    # print(f'arg[{ begin + 3 }] = { arg[begin + 3] }')
    # print()

    key0, value0 = getKeyValue(arg[begin])
    key1, value1 = getKeyValue(arg[begin + 1])
    key2, value2 = getKeyValue(arg[begin + 2])
    key3, value3 = getKeyValue(arg[begin + 3])

    # print()
    # print('key0   = ', key0)
    # print('value0 = ', value0)
    # print()
    # print('key1   = ', key1)
    # print('value1 = ', value1)
    # print()
    # print('key2   = ', key2)
    # print('value2 = ', value2)
    # print()
    # print('key3   = ', key3)
    # print('value3 = ', value3)
    # print()


    if key0 == 'IDENTIFIER' and value1 == '=' and value2 in myBool and value3 == ';':
        result = {
            'Token': 'Define',
            'Lexeme': '',
            'BNF': '<Define> -> <Identifier>  = true/false ;'
        }
        return True, result, begin
    elif key0 == 'IDENTIFIER' and value1 == '=' and key2 in myNum and value3 == ';':
        result = {
            'Token': 'Define',
            'Lexeme': '',
            'BNF': '<Define> -> <Identifier>  = number ;'
        }
        return True, result, begin
    else:
        return False, -1, 9999999999



# <A2> -> <ID> = <ID> ;       a = b
def isDefine2 (arg, begin):
# B
# 1
# n
# h
# Tr 4 n 


    # print()
    # print('arg in isDefine2 = ')
    # for i in arg:
    #     print(f'{i}')
    # print()

    # print('begin in isDefine2 = ', begin)

    # print(f'arg[{ begin }] = { arg[begin] }')
    # print(f'arg[{ begin + 1 }] = { arg[begin + 1] }')
    # print(f'arg[{ begin + 2 }] = { arg[begin + 2] }')
    # print(f'arg[{ begin + 3 }] = { arg[begin + 3] }')
    # print()

    key0, value0 = getKeyValue(arg[begin])
    key1, value1 = getKeyValue(arg[begin + 1])
    key2, value2 = getKeyValue(arg[begin + 2])
    key3, value3 = getKeyValue(arg[begin + 3])

    # print()
    # print('key0   = ', key0)
    # print('value0 = ', value0)
    # print()
    # print('key1   = ', key1)
    # print('value1 = ', value1)
    # print()
    # print('key2   = ', key2)
    # print('value2 = ', value2)
    # print()
    # print('key3   = ', key3)
    # print('value3 = ', value3)
    # print()


    if key0 == 'IDENTIFIER' and value1 == '=' and key2 == 'IDENTIFIER' and value3 == ';':
        result = {
            'Token': 'Define2',
            'Lexeme': '',
            'BNF': '<Define2> -> <Identifier>  = <Identifier> ;'
        }
        return True, result, begin
    
    else:
        return False, -1, 9999999999







