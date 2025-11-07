# core/parser.py

# We import the Token class from the lexer. Every token produced from our lexer
# will be used here to build a tree-like structure called an Abstract Syntax Tree (AST).
from core.lexer import Token


# This is the foundation of our parser — the AST Node.
# Each node represents a construct in the expression (like a number or an operator).
class ASTNode:
    def __init__(self, node_type, value=None):
        self.node_type = node_type  # Type of node (e.g. NumberLiteral, AdditiveExpression)
        self.value = value          # Actual value (e.g. '3', '+', '*')
        self.left = None            # Left child node
        self.right = None           # Right child node

    def __repr__(self):
        return f"{{node_type: {self.node_type}, value: '{self.value}', left: {self.left}, right: {self.right}}}"


# Now, here’s where the main logic lives — the parser.
# It takes tokens (from lexer) and organizes them into a meaningful hierarchy (the AST).
def parse(node, tokens: list[Token]):
    current = 0  # This will keep track of which token we’re currently reading.

    # The peek function looks at the current token without consuming it.
    def peek():
        return tokens[current] if current < len(tokens) else None

    # The consume function takes the current token and moves the pointer forward.
    # If we expect a certain type (like "NUMBER"), and we don’t get it, we raise an error.
    def consume(expected_type=None):
        nonlocal current
        token = peek()
        if expected_type and (token is None or token.type != expected_type):
            raise ValueError(f"Expected token type {expected_type}, got {token.type if token else 'EOF'}")
        current += 1
        return token

    # Now, let's define the first level of parsing — the factor.
    # A factor can be a number, a unary operator, or a grouped expression like (2+3).
    def parse_factor():
        token = peek()
        if token.type == 'NUMBER':
            consume("NUMBER")
            return ASTNode('NumberLiteral', token.value)
        elif token.type == 'UNARY_MINUS':
            consume('UNARY_MINUS')
            factor_unary_node = parse_factor()
            # Here we simulate the effect of unary minus by multiplying by -1
            new_node = ASTNode("MultiplicativeExpression", '*')
            new_node.left = ASTNode("NumberLiteral", "-1")
            new_node.right = factor_unary_node
            return new_node
        elif token.type == 'UNARY_PLUS':
            consume('UNARY_PLUS')
            return parse_factor()
        elif token.type == 'LPAREN':
            consume('LPAREN')
            factor_node = parse_expression()
            consume('RPAREN')
            return factor_node
        else:
            raise SyntaxError(f"Unexpected token {token.type}")

    # Next level — term.
    # A term handles multiplication and division. It builds nodes for those operations.
    def parse_term():
        term_node = parse_factor()
        while peek() and peek().type in ('MULTIPLY', 'DIVIDE'):
            operator_token = consume()
            right = parse_factor()
            new_node = ASTNode("MultiplicativeExpression", operator_token.value)
            new_node.left = term_node
            new_node.right = right
            term_node = new_node
        return term_node

    # Then comes the expression level.
    # This handles addition and subtraction, building on top of the term structure.
    def parse_expression():
        expression_node = parse_term()
        while peek() and peek().type in ('PLUS', 'MINUS'):
            operator_token = consume()
            right = parse_term()
            new_node = ASTNode("AdditiveExpression", operator_token.value)
            new_node.left = expression_node
            new_node.right = right
            expression_node = new_node
        return expression_node

    # We start parsing at the highest level: the full expression.
    ast_root = parse_expression()

    # After parsing, if there are still tokens left, that means the expression was invalid.
    if peek() is not None:
        raise SyntaxError(f"Unexpected token {peek()} at the end of expression")

    # Finally, we return the fully constructed AST.
    return ast_root
