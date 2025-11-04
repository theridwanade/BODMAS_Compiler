# Test cases for BODMAS_Compiler

# - 2*2(3)
# - 2+2
# - 4+3*5 + (3 -1 + (4+5))
# - 2*2*(3)


# eval function defination for easy testing

def eval(expression: str) -> float:
    from core import evaluator, parser, lexer

    token = lexer.lex(expression)
    ast = parser.parse(None, token)
    result = evaluator.evaluate(ast)
    return result

