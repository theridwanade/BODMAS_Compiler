import lexer
import parser

bodmas_expression = "3 + 5 - 2 * (8 ÷ 4)"
token = lexer.lex(bodmas_expression)
print(f"Tokens {token}")
print()
ast = parser.parse(None, token)
print(f"AST {ast}")