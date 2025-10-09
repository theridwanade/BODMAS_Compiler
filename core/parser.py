from core.lexer import Token


class ASTNode:
    def __init__(self, node_type, value=None):
        self.node_type = node_type
        self.value = value
        self.left = None
        self.right = None

    def __repr__(self):
        return f"{{node_type: {self.node_type}, value: '{self.value}', left: {self.left}, right: {self.right}}}"

def parse(node, tokens: list[Token]):
    current = 0

    def peek():
        return tokens[current] if current < len(tokens) else None

    def consume(expected_type=None):
        nonlocal current
        token = peek()
        if expected_type and (token is None or token.type != expected_type):
            raise ValueError(f"Expected token type {expected_type}, got {token.type if token else 'EOF'}")
        current += 1
        return token

    def parse_factor():
        token = peek()
        if token.type == 'NUMBER':
            consume("NUMBER")
            return ASTNode('NumberLiteral', token.value)
        elif token.type == 'UNARY_MINUS':
            consume('UNARY_MINUS')
            factor_unary_node = parse_factor()
            new_node = ASTNode("MultiplicativeExpression", '*')
            new_node.left = ASTNode("NumberLiteral", "-1")
            new_node.right = factor_unary_node
            return new_node
        elif token.type == 'LPAREN':
            consume('LPAREN')
            factor_node = parse_expression()
            consume('RPAREN')
            return factor_node
        else:
            raise SyntaxError(f"Unexpected token {token.type}")

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

    ast_root = parse_expression()

    if peek() is not None:
        raise SyntaxError(f"Unexpected token {peek()} at the end of expression")

    return ast_root