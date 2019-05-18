from typing import List, Tuple
import re

class InvalidCharError(ValueError): pass

operators: str = '+-*/='

def extract_numeric(string: str) -> Tuple[str, str]:
    ''' Extract longest numeric string from the beginning of the input string
        
    '''
    if string == '' or not string[0].isdigit():
        return ('', string)
    else:
        rest: Tuple[str, str] = extract_numeric(string[1:])
        return (string[0] + rest[0], rest[1])

def extract_token(string: str) -> Tuple[str, str]:
    if string == '':
        return ('', string)
    elif string[0].isdigit():
        return extract_numeric(string)
    elif string[0] in operators:
        return (string[0], string[1:])
    else:
        raise InvalidCharError("Invalid char {}".format(string[0]))

def split_expression(expression: str) -> List[str]:
    expression = expression.replace(' ', '')
    elements: List[str] = []
    while expression != '':
        token, expression = extract_token(expression)
        elements.append(token)
    return elements

