# core/evaluator.py

# We import the ASTNode from the parser.
# Every node in the AST we built earlier will pass through this function,
# where each node will be evaluated to its actual numerical result.
from core.parser import ASTNode


# The evaluate function walks through the AST recursively,
# computing values based on the type of node it encounters.
def evaluate(node: ASTNode):
    # If the node is just a number, we simply return its integer value.
    if node.node_type == 'NumberLiteral':
        return int(node.value)

    # If the node represents addition or subtraction, we first evaluate its left and right sides.
    elif node.node_type == 'AdditiveExpression':
        left_value = evaluate(node.left)
        right_value = evaluate(node.right)

        # Then, we apply the corresponding operator.
        if node.value == '+':
            return left_value + right_value
        elif node.value == '-':
            return left_value - right_value

    # If the node represents multiplication or division, we do the same process again.
    elif node.node_type == 'MultiplicativeExpression':
        left_value = evaluate(node.left)
        right_value = evaluate(node.right)

        # Apply the operator to the two evaluated sides.
        if node.value == '*':
            return left_value * right_value
        elif node.value in ('/', '÷'):
            return left_value / right_value

    # If we somehow reach a node type we didn’t define, that’s an error in the structure.
    else:
        raise ValueError(f"Unknown node type: {node.node_type}")
