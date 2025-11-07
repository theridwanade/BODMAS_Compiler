# core/lexer.py

# The lexer is the first gatekeeper of any interpreter.
# Its job is to take the raw input string and transform it into something more structured — tokens.
# Tokens are like words in a sentence, they make it possible for the parser to understand the expression.
#
# So here, we define the Token class. My goal here is simple:
# this class is not an object that performs tokenization,
# it is just a data structure, a definition of what a token is and what it holds.


class Token:
    def __init__(self, type, value):
        self.type = type      # The type of token, for example: NUMBER, PLUS, LPAREN, etc.
        self.value = value    # The actual character(s) that formed this token, e.g. "2" or "+"
    
    def __repr__(self):
        # This makes the token readable when printed,
        # showing both its type and value in a simple structure.
        return f"{{type: {self.type}, value: '{self.value}'}}"


# The lex function is where the real work begins.
# This is where we break down the expression into tokens.
# It reads each character in the string, decides what kind of token it is,
# and stores it inside a list which will later be passed to the parser.
def lex(expression: str):
    expression = expression.strip()       # Clean out any leading or trailing spaces.
    tokens: list[Token] = []              # The list that will contain all tokens.
    i = 0                                 # This will help us move through the string.
    length = len(expression)              # The total length of the expression.
    prev_token_type = None                # To remember the last token we processed.

    # We loop through every character in the expression.
    while i < length:
        char = expression[i]

        # Ignore spaces between characters.
        if char.isspace():
            i += 1
            continue

        # Handle the minus sign.
        # The minus sign can mean two things:
        #   1. Subtraction (binary) → e.g. 5 - 3
        #   2. Negation (unary) → e.g. -3 or (-5)
        # To know which one it is, we look at the previous token.
        if char == '-':
            if prev_token_type in ('NUMBER', 'RPAREN'):
                tokens.append(Token("MINUS", '-'))
            else:
                tokens.append(Token("UNARY_MINUS", '-'))
            i += 1
            prev_token_type = tokens[-1].type
            continue

        # Handle the plus sign.
        # Just like the minus, plus can also be unary or binary.
        # For example, +5 (unary) or 2 + 3 (binary).
        if char == '+':
            if prev_token_type in ('NUMBER', 'RPAREN'):
                tokens.append(Token("PLUS", '+'))
            else:
                tokens.append(Token("UNARY_PLUS", '+'))
            i += 1
            prev_token_type = tokens[-1].type
            continue

        # Handle numbers.
        # Here, we group consecutive digits together to form a complete number.
        if char.isdigit():
            num = ''
            while i < length and expression[i].isdigit():
                num += expression[i]
                i += 1
            tokens.append(Token("NUMBER", num))
            prev_token_type = "NUMBER"
            continue

        # Handle multiplication symbol.
        if char == '*':
            tokens.append(Token("MULTIPLY", '*'))
            i += 1
            prev_token_type = "MULTIPLY"
            continue

        # Handle division symbol using slash (/)
        if char == '/':
            tokens.append(Token("DIVIDE", '/'))
            i += 1
            prev_token_type = "DIVIDE"
            continue

        # Handle division symbol using ÷
        if char == '÷':
            tokens.append(Token("DIVIDE", '÷'))
            i += 1
            prev_token_type = "DIVIDE"
            continue

        # Handle open parenthesis.
        # Parentheses define operation grouping.
        if char == '(':
            if prev_token_type == "NUMBER":
                # Implicit multiplication: e.g. 2(3+4) → 2 * (3+4)
                tokens.append(Token("MULTIPLY", '*'))
            tokens.append(Token("LPAREN", '('))
            i += 1
            prev_token_type = "LPAREN"
            continue

        # Handle close parenthesis.
        if char == ')':
            tokens.append(Token("RPAREN", ')'))
            i += 1
            prev_token_type = "RPAREN"
            continue

        # If the character doesn't fit into any known category, raise an error.
        # This is a safety check — anything unknown should stop the interpreter.
        raise ValueError(f"Unexpected character: {char}")

    # When we reach the end, we return the list of tokens to the parser.
    return tokens
