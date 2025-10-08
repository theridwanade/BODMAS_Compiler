import lexer
import parser
import evaluator

bodmas_expression = ""
token = lexer.lex(bodmas_expression)
ast = parser.parse(None, token)
result = evaluator.evaluate(ast)
print(f"Result {result}")