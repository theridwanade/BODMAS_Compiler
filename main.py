from core import evaluator, parser, lexer

bodmas_expression = "(2+4) - 1"
token = lexer.lex(bodmas_expression)
print(f"Tokens {token}")
ast = parser.parse(None, token)
print(f"AST {ast}")
result = evaluator.evaluate(ast)
print(f"Result {result}")