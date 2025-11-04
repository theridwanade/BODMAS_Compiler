import sys
import os
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

import pytest
from core import evaluator, parser, lexer

# Test cases for BODMAS_Compiler

# - 2*2(3)
# - 2+2
# - 4+3*5 + (3 -1 + (4+5))
# - 2*2*(3)


# eval function defination for easy testing

def eval(expression: str) -> float:

    token = lexer.lex(expression)
    ast = parser.parse(None, token)
    result = evaluator.evaluate(ast)
    return result

@pytest.mark.parametrize("expression, expected", [
    ("2*2(3)", 12),             
    ("2+2", 4),
    ("4+3*5+(3-1+(4+5))", 4 + 3*5 + (3 - 1 + (4 + 5))),  # nested parentheses
    ("2*2*(3)", 12),
])
def test_bodmas_expressions(expression, expected):
    assert eval(expression) == pytest.approx(expected)