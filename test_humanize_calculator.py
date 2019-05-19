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
    'A', 'a', 'B', 'C', 'D', 'E', 'F'
]

valid_expressions_humanize: List[str] = [
    ("0", "zero"),
    ("1", "one"),
    ("2", "two"),
    ("3", "three"),
    ("4", "four"),
    ("5", "five"),
    ("6", "six"),
    ("7", "seven"),
    ("8", "eight"),
    ("9", "nine"),

]

def random_expression_and_tokens(amount: int = 100) -> Iterator[Tuple[str, List[str]]]:
    for _ in range(amount):
        tokens: List[str] = []
        tokens.append(str(random.randrange(100)))
        for _ in range(random.randrange(10)):
            tokens.append(random.choice(humanize_calculator.operators))
            tokens.append(str(random.randrange(100)))
        yield (''.join(tokens), tokens)

@pytest.mark.parametrize('expression,tokens', random_expression_and_tokens())
def test_is_valid_true(expression,tokens):
    assert humanize_calculator.is_valid(expression)
    
@pytest.mark.parametrize('expression', invalid_expressions)
def test_is_valid_false(expression):
    assert not humanize_calculator.is_valid(expression)

@pytest.mark.parametrize('expression,tokens', random_expression_and_tokens())
def test_random_tokenize(expression, tokens):
    assert humanize_calculator.tokenize(expression) == tokens

# @pytest.mark.parametrize('expression,human_string', valid_expression_humanize)
# def test_humanize():
#     assert humanize_calculator.humanize()