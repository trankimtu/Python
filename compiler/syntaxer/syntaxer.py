class Syntaxer (object):
    def __init__(self, *arg):
        self.lexemes = arg
        # print('arg = ', arg)

    # statemenize method - create statement list from lexemes
    def syntaxer(self):

        lexemes = list(self.lexemes[0])
       


        begin = 0
        length = len(lexemes)  #tes

        resultList = []
        
        # print('len(lexemes) = ', len(lexemes))
        while begin < length:

            isStatement, result, newBegin = Statement(lexemes, begin)

            begin = newBegin

            print(f'isStatement = {isStatement}')
            print(f'result = {result}')
            resultList.append(result)

            print()
            # Statement(lexemes, begin)
        return resultList
     

# ==============================================
# End class here
# ==============================================

# All test will be call in Statement
def Statement(arg, begin):
    print (f'begin in Statement = {begin}')
    print ('arg[begin] at begin Statement = ', arg[begin])

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
        IsStatement = False
        stamentResult = arg[begin]
        statementBegin = begin + 1


    return IsStatement, stamentResult, statementBegin

# End Statement =================================

def isDeclarative(arg, begin):
    print ('Begin at 1st lexeme in isDeclarative = ', begin)
    print ('length remain in isDeclarative = ', len(arg[begin:]))

    IsType, typeKey, typeValue = isType(arg[begin])
    print('IsType = ', IsType)
    print ('len(arg[begin:]) = ', len(arg[begin:]))
    if IsType == True and len(arg[begin:]) > 1:
        begin += 1

        print ('Begin at 2nd lexeme in isDeclarative = ', begin)
        IsID, idKey, idValue = isID(arg[begin])
        print ('IsID = ', IsID)

        if IsID == True and len(arg[begin:]) > 1:
            begin += 1
            print ('Begin at 3rd lexeme in isDeclarative = ', begin)
            IsSemicolon = isSemicolon(arg[begin])

            if IsSemicolon == True:
                result = {
                    'Token': 'Declaration',
                    # 'Lexeme': '',
                    'BNF': '<Statement> -> <Declarative> \n\t\t\t\t <Declarative> -> <Type> <ID> ;'
                }
                
                begin += 1
                return True, result, begin
            else:
                begin -=1
                return False, "3rd lexeme in isDeclarative is not ';'"
        else:
            begin -= 1
            return False, '2nd lexeme in isDeclarative is not ID'

    else: 
        return False, '1st lexeme in isDeclarative is not Type', begin

# End isDeclarative =============================


# isFactor =====================================
def isFactor(arg, begin):
    print('isFactor is called')
    if len(arg[begin:]) == 0:
        print("Error, Factor must be provided!")
        return False

    else:

        # factorKey, factorValue = getKeyValue(arg[begin])
        # if factorValue != '(' or 

        IsID, IdKey, IdValue = isID(arg[begin])
        IsNum, numKey, numValue = isNum(arg[begin])
        # IsBool, boolKey, boolValue = isBool(arg[begin])

        # print('IsBool = ', IsBool)
        
        if IsID == True or IsNum == True:
            return True, begin
        else:
            return False, begin
      
    
    # openParenthesisKey, openParenthesisValue = getKeyValue(arg[begin])
    # if openParenthesisValue = '(':
    #     IsExpression, expressionEnd = isExpression (arg, begin + 1)

# End isFactor =================================



  

def isTermPrime(arg, begin):
    IsPlusMinus = isPlusMinus(arg[begin])

    if IsPlusMinus == True:
        begin += 1
        print('arg[begin] in expressionprime = ', arg[begin])


        IsTerm, newBegin = isTerm(arg, begin)
        if IsTerm == True:
            return IsTerm, newBegin
        
        else:
            print('Error, after operator must be ID or num')
            return False, 1000000
        
    else:
        print('Error - Expression need operator right after ID')
    

def isTerm(arg, begin):
    print('isTerm is called')
    IsMulDev = isMulDev(arg[begin + 1])

    if IsMulDev == False:
        IsTerm, termEnd = isFactor(arg, begin)
        print('isterm = ', isTerm)

        return IsTerm, termEnd
    else:
        print('mul dev')
        temp = begin + 2
        IsFactor, factorEnd = isFactor(arg, temp)
        if IsFactor == True:
            return True, factorEnd
    
        return False, begin

    



def isExpressionPrime (arg, begin):
    IsPlusMinus = isPlusMinus(arg[begin])

    if IsPlusMinus == True:
        begin += 1
        print('arg[begin] in expressionprime = ', arg[begin])


        IsTerm, newBegin = isTerm(arg, begin)
        if IsTerm == True:
            return IsTerm, newBegin
        
        else:
            print('Error, after operator must be ID or num')
            return False, 1000000
        
    else:
        print('Error - Expression need operator right after ID')

def isExpression(arg, begin):
    print('dict in isExpression = ', arg[begin])
    IsID, idKey, idValue = isID(arg[begin])
    IsNum, numKey, numValue = isNum(arg[begin])

    if IsID == True or IsNum == True:
        if len(arg[begin:]) > 1:


            print('arg[begin]', arg[begin])
            IsPlusMinus = isPlusMinus(arg[begin + 1])
            IsMulDev = isMulDev(arg[begin + 1])

            if IsPlusMinus == True:
                print('Plus Minus')
                begin += 1  # begin now is + -
                IsExpressionPrime, newBegin = isExpressionPrime(arg, begin)
                if IsExpressionPrime == True:
                    return True, newBegin

            else:
                # Expression = Term
                print('Go directly to Term')
                IsTerm, expressionEnd = isTerm(arg, begin)
                if IsTerm == True:
                    return IsTerm, expressionEnd
        else:
            return False, 'The length is not enough for the statement', 1000000
    else:
        return False, '1st lexeme in isExpression is Not an ID or a num', 1000000

# End isExpression ================================


# isAssign ========================================

def isAssign(arg, begin):
    IsID, idKey, idValue = isID(arg[begin])

    # 1st lexeme is ID
    if IsID == True:
        print('1st element in isAssign is ID')
        print('idKey = ', idKey)
        print('idValue = ', idValue)

        begin += 1
        print (arg[begin])
        IsEqual = isEqual(arg[begin])

        #2nd lexeme is '='
        if IsEqual == True:
            print("2nd element in isAssign is '='")
            begin += 1
            IsExpression, expressionEnd = isExpression(arg, begin)
            print('begin ====', begin)
            print('expressionEnd====', expressionEnd)
            # print('newBegin in isExpression = ', newBegin)
            print('expressionEnd = ', expressionEnd)
            print ('begin = ', begin)
            if IsExpression == True:
                begin = expressionEnd +1
                print('begin ++++', begin)
                print(arg[begin])
                IsSemicolon = isSemicolon(arg[begin])
                if IsSemicolon == True:
                    result = {
                        'Token': 'Assign',
                        'BNF': '<Assign> -> <ID> = <Expression> ;'
                    }
                    begin += 1 # 1 for new one
                    return True, result, begin
                else:
                    return False, "Not Assign, after Expression is not ';'", begin
            else:
                return False, '<ID> = NOT expression', begin
        else:    
            return False, "2nd lexem of define is not '='" , begin
    else:
        return False, '1st lexeme of Define is not ID', begin
 
    
def isIf(arg, begin):
    pass
def isWhile(arg, begin):
    pass
def isBegin(arg, begin):
    pass

# End isAssign ================================


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

def isBool(boolDict):

    boolKey, boolValue = getKeyValue(boolDict)

    boolType = ['true', 'false']

    if boolValue in boolType:
        return True, boolKey, boolValue
    else:
        return False, 'Not a bool Key', 'Not a bool Value' 
        

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

def isEqual(equalDict):
    equalKey, equalValue = getKeyValue(equalDict)

    if equalValue == '=':
        return True
    else:
        return False

def isPlusMinus(operatorDict):
    opKey, opValue = getKeyValue(operatorDict)
    if opValue == '+' or opValue == '-':
        return True
    else:
        return False

def isMulDev(operatorDict):
    opKey, opValue = getKeyValue(operatorDict)
    if opValue == '*' or opValue == '/':
        return True
    else:
        return False

