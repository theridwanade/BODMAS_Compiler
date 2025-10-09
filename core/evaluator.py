from core.parser import ASTNode


def evaluate(node: ASTNode):
    if node.node_type == 'NumberLiteral':
        return int(node.value)
    elif node.node_type == 'AdditiveExpression':
        left_value = evaluate(node.left)
        right_value = evaluate(node.right)
        if node.value == '+':
            return left_value + right_value
        elif node.value == '-':
            return left_value - right_value
    elif node.node_type == 'MultiplicativeExpression':
        left_value = evaluate(node.left)
        right_value = evaluate(node.right)
        if node.value == '*':
            return left_value * right_value
        elif node.value in ('/', '÷'):
            return left_value / right_value
    else:
        raise ValueError(f"Unknown node type: {node.node_type}")