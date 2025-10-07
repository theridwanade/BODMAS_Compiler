# from lexer import Token


# class ASTNode:
#     def __init__(self, type=None, value=None):
#         self.type = type
#         self.value = value
#         self.left = None
#         self.right = None

# def parse(node: ASTNode, tokens: list[Token]):
#    i = 0
#    while i < len(tokens):
#        token = tokens[i]
#
#        if isinstance(token, int):
#            if node.left ==