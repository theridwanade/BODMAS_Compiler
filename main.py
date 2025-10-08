import lexer
import parser
import evaluator

bodmas_expression = "-2 + 4"
token = lexer.lex(bodmas_expression)
# print(f"Tokens {token}")
ast = parser.parse(None, token)
# print(f"AST {ast}")
result = evaluator.evaluate(ast)
print(f"Result {result}")