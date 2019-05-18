import humanize_calculator
import pytest
import random
from typing import Iterator, Tuple, List

def random_expression_and_split(amount: int) -> Iterator[Tuple[str, List[str]]]:
    for _ in range(amount):
        elements: List[str] = []
        elements.append(str(random.randrange(100)))
        for _ in range(random.randrange(10)):
            elements.append(random.choice(humanize_calculator.operators))
            elements.append(str(random.randrange(100)))
        expression = elements[0]
        for el in elements[1:]:
            expression += ' ' * random.randrange(5) + el
        yield (expression, elements)

@pytest.mark.parametrize('expression,expression_split', random_expression_and_split(100))
def test_random_expression_split(expression, expression_split):
    assert humanize_calculator.split_expression(expression) == expression_split