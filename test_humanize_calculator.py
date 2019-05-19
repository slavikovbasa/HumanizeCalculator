import humanize_calculator
import pytest
import random
from typing import Iterator, Tuple, List

invalid_expressions: List[str] = [
    '00', '000', '01', '002', '0123', '+', '-', '*', '/', '=',
    '2+', '2-', '2*', '2/', '2=', '+2', '-2', '*2', '/2', '=2',
    '2++2', '2--2', '2**2', '2//2', '2==2', '2+++2', '2---2',
    '2***2', '2///2', '2===2', '2+2==2', '2++2=2', '2--2=0',
    '2**2=4', '2//2=1', '2+2==2+2', '.', '(', ')', ',', '?', '!',
    '|', '&', '^', '%', '2.+2=4', '2+2.=4', '2+2=4.', '0.2+2=2',
    'A', 'a', 'B', 'C', 'D', 'E', 'F', '2 2'
]

valid_expressions_humanize: List[str] = [
    ('0', 'zero'),
    ('1', 'one'),
    ('2', 'two'),
    ('3', 'three'),
    ('4', 'four'),
    ('5', 'five'),
    ('6', 'six'),
    ('7', 'seven'),
    ('8', 'eight'),
    ('9', 'nine'),
    ('10', 'ten'),
    ('11', 'eleven'),
    ('12', 'twelve'),
    ('13', 'thirteen'),
    ('14', 'fourteen'),
    ('15', 'fifteen'),
    ('16', 'sixteen'),
    ('17', 'seventeen'),
    ('18', 'eighteen'),
    ('19', 'nineteen'),
    ('20', 'twenty'),
    ('30', 'thirty'),
    ('40', 'fourty'),
    ('50', 'fifty'),
    ('60', 'sixty'),
    ('70', 'seventy'),
    ('80', 'eighty'),
    ('90', 'ninety'),
    ('100','hundred'),
    ('1000', 'thousand'),
    ('1000000', 'million'),
    ('1000000000', 'billion'),
    ('123456789', 'one hundred twenty three million four hundred fifty six thousand seven hundred eighty nine'),
    ('2+2', 'two plus two'),
    ('2-2', 'two minus two'),
    ('2*2', 'two multiplied by two'),
    ('2/2', 'two divided by two'),
    ('2=2', 'two equals two'),
    ('2+2=2', 'two plus two equals two'),
    ('2=2+2', 'two equals two plus two'),
    ('2+2*2=7-7/7', 'two plus two multiplied by two equals seven minus seven divided by seven')
]

def random_expression_and_tokens(amount: int = 100, spaces: bool = False) -> Iterator[Tuple[str, List[str]]]:
    for _ in range(amount):
        tokens: List[str] = []
        tokens.append(str(random.randrange(100)))
        for _ in range(random.randrange(10)):
            tokens.append(random.choice(humanize_calculator.operators))
            tokens.append(str(random.randrange(100)))
        if spaces:
            expression = tokens[0]
            for el in tokens[1:]:
                expression += ' ' * random.randrange(5) + el
            yield (expression, tokens)
        else:
            yield (''.join(tokens), tokens)

@pytest.mark.parametrize('expression,tokens', random_expression_and_tokens(spaces=True))
def test_is_valid_true(expression,tokens):
    assert humanize_calculator.is_valid(expression)

@pytest.mark.parametrize('expression', invalid_expressions)
def test_is_valid_false(expression):
    assert not humanize_calculator.is_valid(expression)

@pytest.mark.parametrize('expression,tokens', random_expression_and_tokens())
def test_random_tokenize(expression, tokens):
    assert humanize_calculator.tokenize(expression) == tokens

@pytest.mark.parametrize('expression,human_string', valid_expressions_humanize)
def test_valid_humanize(expression, human_string):
    assert humanize_calculator.humanize(expression) == human_string

@pytest.mark.parametrize('expression', invalid_expressions)
def test_invalid_humanize(expression):
    assert humanize_calculator.humanize(expression) == 'invalid input'