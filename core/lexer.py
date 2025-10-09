# core/lexer.py

class Token:
    def __init__(self, type, value):
        self.type = type
        self.value = value

    def __repr__(self):
        return f"{{type: {self.type}, value: '{self.value}'}}"

def lex(expression: str):
    expression = expression.strip()
    tokens: list[Token] = []
    i = 0
    length = len(expression)
    prev_token_type = None

    while i < length:
        char = expression[i]
        if char.isspace():
            i += 1
            continue

        if char == '-':
            # Decide unary or binary minus
            if prev_token_type in ('NUMBER', 'RPAREN'):
                tokens.append(Token("MINUS", '-'))
            else:
                tokens.append(Token("UNARY_MINUS", '-'))
            i += 1
            prev_token_type = tokens[-1].type
            continue
        if char == '+':
            if prev_token_type in ('NUMBER', 'RPAREN'):
                tokens.append(Token("PLUS", '+'))
            else:
                tokens.append(Token("UNARY_PLUS", '+'))
            i += 1
            prev_token_type = tokens[-1].type
            continue
        if char.isdigit():
            num = ''
            while i < length and expression[i].isdigit():
                num += expression[i]
                i += 1
            tokens.append(Token("NUMBER", num))
            prev_token_type = "NUMBER"
            continue
        if char == '*':
            tokens.append(Token("MULTIPLY", '*'))
            i += 1
            prev_token_type = "MULTIPLY"
            continue
        if char == '/':
            tokens.append(Token("DIVIDE", '/'))
            i += 1
            prev_token_type = "DIVIDE"
            continue
        if char == '÷':
            tokens.append(Token("DIVIDE", '÷'))
            i += 1
            prev_token_type = "DIVIDE"
            continue
        if char == '(':
            tokens.append(Token("LPAREN", '('))
            i += 1
            prev_token_type = "LPAREN"
            continue
        if char == ')':
            tokens.append(Token("RPAREN", ')'))
            i += 1
            prev_token_type = "RPAREN"
            continue
        raise ValueError(f"Unexpected character: {char}")
    return tokens