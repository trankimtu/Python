class Syntaxer (object):
    def __init__(self, *arg):
        self.lexemes = arg
        # print('arg = ', arg)

    # statemenize method - create statement list from lexemes
    def syntaxer(self):

        lexemes = list(self.lexemes[0])

        begin = 0
        length = len(lexemes)
        
        # print('len(lexemes) = ', len(lexemes))
        while begin < length:


            isStatement, result, newBegin = Statement(lexemes, begin)

            begin = newBegin

            print(f'isStatement = {isStatement}')
            print(f'result = {result}')
            print(f'newBegin = {newBegin}')
            # Statement(lexemes, begin)




     

# ==============================================
# End class here
# ==============================================

# All test will be call in Statement
def Statement(arg, begin):
    print (f'begin in Statement = {begin}')

    IsDeclarative, DeclarativeResult, DeclarativeBegin = isDeclarative(arg, begin)
    IsAssign, AssignResult, AssignBegin = isAssign(arg, begin)
    # isIf(arg, begin)
    # isWhile(arg, begin)
    # isBegin(arg, begin)
    
    if IsDeclarative == True:
        IsStatement, stamentResult, statementBegin = IsDeclarative, DeclarativeResult, DeclarativeBegin
    elif IsAssign == True:
        IsStatement, stamentResult, statementBegin = IsAssign, AssignResult, AssignBegin

    else:
        print('Not a statement')


    return IsStatement, stamentResult, statementBegin

# End Statement =================================

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

# End isDeclarative ================================ 

def isTerm(termDict):
    termKey, termValue = getKeyValue(termDict)

    if termKey == 'IDENTIFER':
        return True
    else:
        return False

def isExpressionPrime (arg, begin):
    if arg[begin + 1] == '+' or arg[begin + 1] == '-':
        IsTerm = isTerm(arg[begin + 2])
        IsSemicolon = isSemicolon(arg[begin + 3])
        if IsTerm & IsSemicolon == True:
            return True


def isExpression(arg, begin):
    IsTerm = isTerm(arg[begin])

    if IsTerm == True:
        IsExpressionPrime = isExpressionPrime(arg, begin)

        if IsExpressionPrime == True:
            return True
        else:
            print(f'IsExpressionPrime = {IsExpressionPrime}')

    else:
        print ('Expression Error')


# End isExpression ================================

def isAssign(arg, begin):
    # pass
    IsID, idKey, idValue = isID(arg[begin])
    if IsID == True:
        opreatorKey, operatorValue = getKeyValue(arg[begin + 1])
        if operatorValue == '=':
            IsExpression = isExpression(arg, begin + 2)
            if IsExpression == True:
                result = {
                'Token': 'Declaration',
                'BNF': '<Assign> -> <ID> = <Expression> ;'
            }
            newBegin = begin + 4
        return True, result, newBegin
    
def isIf(arg, begin):
    pass
def isWhile(arg, begin):
    pass
def isBegin(arg, begin):
    pass



def isType(typeDict):

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





def isFactor(arg, begin):
    
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

    numKey, numValue = getKeyValue(numDict)

    numType = ['FLOAT', 'INT']

    if numKey in numType:
        return True, numKey, numValue
    else:
        return False, 'NAN Key', 'NAN Value' 
    


# Support Method =======================================================

def getKeyValue (mydict):
    # print('dict = ', mydict)
    for key, value in mydict.items():
        return key, value

def isSemicolon(semicolonDict):
    semicolonKey, semicolonValue = getKeyValue(semicolonDict)
    # semicolonValue = list(semicolonDic.values())[0]

    # print(numKey)
    # print(numValue)

    if semicolonValue == ';':
        return True
    else:
        return False