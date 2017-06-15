
from .handling_bools import BoolMatrix

def resolve_tree(node):

    if node.data == 'A' or node.data == 'B':
        return BoolMatrix(node.data)
    

    mat_left = resolve_tree(node.left)
    if node.data == 'not':
        return mat_left.not_()

    mat_right = resolve_tree(node.right)

    if node.data == 'or':
        return mat_left.or_(mat_right)
    if node.data == 'and':
        return mat_left.and_(mat_right)

