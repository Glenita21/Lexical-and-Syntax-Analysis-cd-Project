def isDelimiter(ch):
    if (ch == ' ' or ch == '+' or ch == '-' or ch == '*' or ch == '/' or ch == ',' or ch == ';' or ch == '>' or ch == '<' or ch == '=' or ch == '(' or ch == ')' or ch == '[' or ch == ']' or ch == '{' or ch == '}'):
        return True
    return False

def isOperator(ch):
    if (ch == '+' or ch == '-' or ch == '*' or ch == '/' or ch == '>' or ch == '<' or ch == '='):
        return True
    return False

def validIdentifier(stre):
    if (stre[0] == '0' or stre[0] == '1' or stre[0] == '2' or 
        stre[0] == '3' or stre[0] == '4' or stre[0] == '5' or 
        stre[0] == '6' or stre[0] == '7' or stre[0] == '8' or 
        stre[0] == '9' or isDelimiter(stre[0]) == True): 
        return False 
    return True;  

def isKeyword(stre):
    list1 = ["if","while","int"]
    
    if(stre in list1):
        return True 
    return False 

def isInteger( stre):
    len1 = len(stre); 
    if (len1 == 0):
        return False 
    for i in range(len1):
        if (stre != '0' and stre!= '1' and stre != '2'
         and stre != '3' and stre != '4' and stre != '5'
            and stre != '6' and stre != '7' and stre != '8'
            and stre != '9' or (stre == '-' and i > 0)): 
            return False 
    return True 

def isRealNumber(stre):
    hasDecimal = False 

    if (len(stre) == 0): 
        return False
    for i in range(len(stre)):
        if (stre[i] != '0' and stre[i] != '1' and stre[i] != '2'
            and stre[i] != '3' and stre[i] != '4' and stre[i] != '5'
            and stre[i] != '6' and stre[i] != '7' and stre[i] != '8'
            and stre[i] != '9' and stre[i] != '.' or 
            (stre[i] == '-' and i > 0)):
            return False
        if (stre[i] == '.'):
            hasDecimal = True 
    return (hasDecimal)
          
def parse(stre):
    
    len1 = len(stre)
    right =0
    left = 0
    while (right < len1 and left <= right):
        if (isDelimiter(stre[right]) == False): 
            right=right+1
        if (isDelimiter(stre[right]) == True and left == right):
            if (isOperator(stre[right]) == True): 
                print stre[right], "IS AN OPERATOR"
            right=right +1 
            left = right 
        elif (isDelimiter(stre[right]) == True and left != right 
                or (right == len and left != right)):
            substr = stre[left:right]
            if (isKeyword(substr) == True): 
                print substr, "IS A KEYWORD"; 
            elif (isInteger(substr) == True): 
                print substr, "IS AN INTEGER"; 
            elif (isRealNumber(substr) == True): 
                print substr, "IS A REAL NUMBER"; 
            elif (validIdentifier(substr) == True
                    and isDelimiter(stre[right - 1]) == False):
                print substr, "IS A VALID IDENTIFIER"
            elif (validIdentifier(substr) == False
                    and isDelimiter(stre[right - 1]) == False): 
                print substr, "IS NOT A VALID IDENTIFIER"; 
            left = right; 
    return; 


def main():
    with open('/home/ubuntu/cdq', 'r') as myfile:
        stre = myfile.read().replace('\n', ' ')
    parse(stre)
    
if __name__ == '__main__':
    main()


