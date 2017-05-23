
import unittest

from .binary_node import Node
from .handling_bools import BoolMatrix
from .resolve_expression_tree import resolve_tree


class TestBoolMatrix(unittest.TestCase):

    def test_init_A(self):

        A = BoolMatrix('A')
        
        test_A = [[True, True], [False, False]]

        self.assertEqual(test_A, A)


    def test_init_B(self):

        B = BoolMatrix('B')

        test_B = [[True, False], [True, False]]

        self.assertEqual(test_B, B)


    def test_init(self):

        F = BoolMatrix()

        test_F = [[False, False],[False, False]]

        self.assertEqual(test_F, F)


    def test_not_(self):

        A = BoolMatrix('A')
        
        test_not__A = [[False, False], [True, True]]

        not__A = A.not_()

        self.assertEqual(test_not__A, not__A)


    def test_and_(self):

        A = BoolMatrix('A')
        B = BoolMatrix('B')

        A_and__B = A.and_(B)
        B_and__A = B.and_(A)

        test_A_and__B = [[True, False], [False, False]]

        self.assertEqual(test_A_and__B, A_and__B)
        self.assertEqual(test_A_and__B, B_and__A)

    
    def test_or_(self):

        A = BoolMatrix('A')
        B = BoolMatrix('B')

        A_or__B = A.or_(B)
        B_or__A = B.or_(A)

        test_A_or__B = [[True, True], [True, False]]

        self.assertEqual(test_A_or__B, A_or__B)
        self.assertEqual(test_A_or__B, B_or__A)


class TestNode(unittest.TestCase):

    def test_init(self):

        data_str = 'A'
        a_node = Node(data_str)
        
        self.assertEqual(a_node.data, data_str)
        self.assertIsNone(a_node.left)
        self.assertIsNone(a_node.right)


class TestResolveTree(unittest.TestCase):


    def compare_result(self, tree, expected_result):

        result = resolve_tree(tree)
        self.assertEqual(result, expected_result)


    def test_single_node_A(self):
        test_A = BoolMatrix('A')
        A_tree = Node('A')
        self.compare_result(A_tree, test_A)


    def test_single_node_B(self):
        test_B = BoolMatrix('B')
        B_tree = Node('B')
        self.compare_result(B_tree, test_B)


    def test_and(self):
        and_tree = Node('and')
        and_tree.left = Node('A')
        and_tree.right = Node('B')

        expected = BoolMatrix('A').and_(BoolMatrix('B'))
        self.compare_result(and_tree, expected)


    def test_or(self):
        or_tree = Node('or')
        or_tree.left = Node('A')
        or_tree.right = Node('B')

        expected = BoolMatrix('A').or_(BoolMatrix('B'))
        self.compare_result(or_tree, expected)


    def test_not(self):
        not_tree = Node('not')
        not_tree.left = Node('A')

        expected = BoolMatrix('A').not_()
        self.compare_result(not_tree, expected)


    def test_more_than_two_levels(self):
        ml_tree = Node('and')
        ml_tree.left = Node('A')
        ml_tree.right = Node('not')
        ml_tree.right.left = Node('B')

        expected = BoolMatrix('A').and_(BoolMatrix('B').not_())
        self.compare_result(ml_tree, expected)



