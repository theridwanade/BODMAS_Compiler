# Test cases for BODMAS_Compiler


# eval function defination for easy testing

def eval(expression: str) -> float:
    from core import evaluator, parser, lexer

    token = lexer.lex(expression)
    ast = parser.parse(None, token)
    result = evaluator.evaluate(ast)
    return result

