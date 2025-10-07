import lexer



bodmas_expression = "3 + 5 / (2 * 3) - 1"
token = lexer.lex(bodmas_expression)
print(f"Tokens {token}")