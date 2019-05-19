from typing import List, Tuple, Dict
import re

class InvalidCharError(ValueError): pass

operators: str = '+-*/='

number_orders: int = [100, 1000, 1000000, 1000000000]

human_numerics: Dict[str, str] = {
    '0': 'zero',
    '1': 'one',
    '2': 'two',
    '3': 'three',
    '4': 'four',
    '5': 'five',
    '6': 'six',
    '7': 'seven',
    '8': 'eight',
    '9': 'nine',
    '10': 'ten',
    '11': 'eleven',
    '12': 'twelve',
    '13': 'thirteen',
    '14': 'fourteen',
    '15': 'fifteen',
    '16': 'sixteen',
    '17': 'seventeen',
    '18': 'eighteen',
    '19': 'nineteen',
    '20': 'twenty',
    '30': 'thirty',
    '40': 'fourty',
    '50': 'fifty',
    '60': 'sixty',
    '70': 'seventy',
    '80': 'eighty',
    '90': 'ninety',
    '100':'hundred',
    '1000': 'thousand',
    '1000000': 'million',
    '1000000000': 'billion'
}

human_operators: Dict[str, str] = {
    '+': 'plus',
    '-': 'minus',
    '*': 'multiplied by',
    '/': 'divided by',
    '=': 'equals'
}

expression_pattern = re.compile(
    r'''^\s*(0|[1-9]\d*)    # the first token is always number;
                            # number is either single '0' character
                            # or any other numeric string,
                            # that doesn't start with 0
        (   \s*            
            [\+\-\*\/\=]    # any operator
            \s*
            (0|[1-9]\d*)    # any number
            \s*
        )*$                 # pattern <operator><number> is repeated
                            # arbitrary amount of times
    ''', re.VERBOSE
)

def is_valid(expression: str) -> bool:
    '''Test if expression is valid'''
    return expression_pattern.match(expression) != None

def extract_token(expression: str) -> Tuple[str, str]:
    '''Extract token from the beginning of the expression

    Returns a tuple(<extracted token>, <expression remainder>).
    Handles numeric tokens and tokens from the operators string.
    If unknown char is found, InvalidCharError is raised.
    '''
    if expression == '':
        return ('', expression)
    elif expression[0].isdecimal():
        match = re.match(r'(\d+)(.*)', expression)
        return match.groups()
    elif expression[0] in operators:
        return (expression[0], expression[1:])
    else:
        raise InvalidCharError('Invalid char {}'.format(expression[0]))

def tokenize(expression: str) -> List[str]:
    '''Tokenize expression

    Returns a list of all tokens in expression.
    If unknown char is found, InvalidCharError is raised.
    '''
    elements: List[str] = []
    while expression != '':
        token, expression = extract_token(expression)
        elements.append(token)
    return elements

def humanize_number(number: int) -> str:
    '''Return humanized number representation'''
    if str(number) in human_numerics:
        return human_numerics[str(number)]
    else:
        known_numbers: List[int] = sorted(
            [int(key) for key in human_numerics.keys()],
            reverse=True
        )[:-1]
        number_parts: List[str] = []
        for known in known_numbers:
            if number == 0:
                break
            elif number >= known:
                if known in number_orders:
                    number_parts.append(humanize_number(number // known))

                number_parts.append(human_numerics[str(known)])
                number = number % known
        return ' '.join(number_parts)

def humanize_token(token: str) -> str:
    '''Return humanized token'''
    if token in human_operators:
        return human_operators[token]
    elif token.isdecimal():
        return humanize_number(int(token))
    else:
        raise InvalidCharError('Invalid token {}'.format(token))

def humanize(expression: str) -> str:
    '''Humanize expression
    
    Expression is considered valid if it contains only integer numbers and
    operators [+-*/=], all of this operators have to be binary;
    numbers, except for '0' itself cannot start with '0';
    multiple zeroes (e.g. '000') are also forbidden;
    spaces are allowed, except for when they are between numbers (e.g. '2 2=2')
    '''
    if not is_valid(expression):
        return 'invalid input'
    expression = expression.replace(' ', '')
    try:
        tokens: List[str] = tokenize(expression)
        return ' '.join(humanize_token(token) for token in tokens)
    except InvalidCharError:
        return 'invalid input'