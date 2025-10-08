from lib2to3.pgen2.token import NUMBER


class Token:
    def __init__(self, type, value):
        self.type = type
        self.value = value

    def __repr__(self):
        return f"{{type: {self.type}, value: '{self.value}'}}"

def lex(expression: str):
    expression.strip()
    expression_length = len(expression)
    tokens: list[Token] = []

    if expression_length == 0:
        raise ValueError("Empty expression")


    def walk():
        count = 0
        while True:
            if expression[count].isdigit():
                num = ''
                while count < expression_length and expression[count].isdigit():
                    if expression[count - 1] == '-' and (count - 1 == 0 or expression[count - 2] in '+-*/( '):
                        num += '-'
                    num += expression[count]
                    count += 1
                token = Token("NUMBER", num)
                tokens.append(token)
            elif expression[count] == '+':
                tokens.append(Token("PLUS", '+'))
                count += 1
            elif expression[count] == '-':
                if (count == 0 and expression[count] == '-') or expression[count - 1] in '(':
                    count += 1
                    continue
                tokens.append(Token("MINUS", '-'))
                count += 1
            elif expression[count] == '*':
                tokens.append(Token("MULTIPLY", '*'))
                count += 1
            elif expression[count] == '/':
                tokens.append(Token("DIVIDE", '/'))
                count += 1
            elif expression[count] == '÷':
                tokens.append(Token("DIVIDE", '÷'))
                count += 1
            elif expression[count] == '(':
                tokens.append(Token("LPAREN", '('))
                count += 1
            elif expression[count] == ')':
                tokens.append(Token("RPAREN", ')'))
                count += 1
            elif expression[count].isspace():
                count += 1
            else:
                raise ValueError(f"Unexpected character: {expression[count]}")
            if count >= expression_length:
                break
    walk()
    return  tokens

