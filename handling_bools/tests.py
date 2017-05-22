
import unittest

from .handling_bools import BoolMatrix

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


        

