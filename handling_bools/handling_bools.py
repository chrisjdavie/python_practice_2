import operator

class BoolMatrix(list):

    def __init__(self, axis=None):

        if axis == 'A':
            self.append([True, True])
            self.append([False, False])
        if axis == 'B':
            self.append([True, False])
            self.append([True, False])
        if not axis:
            self.append([False, False])
            self.append([False, False])


    def not_(self):
        
        not__self = BoolMatrix()
        for i, row in enumerate(self):
            for j, col in enumerate(row):
                not__self[i][j] = not col

        return not__self


    def __opp_(self, other, opp_):

        s_opp__o = BoolMatrix()
        for i, (s_row, o_row) in enumerate(zip(self, other)):
            for j, (s_col, o_col) in enumerate(zip(s_row, o_row)):
                s_opp__o[i][j] = opp_(s_col, o_col)
        
        return s_opp__o


    def and_(self, other):

        return self.__opp_(other, operator.and_)


    def or_(self, other):

        return self.__opp_(other, operator.or_)
