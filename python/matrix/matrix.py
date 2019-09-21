class Matrix(object):
    def __init__(self, matrix_string):
        self.matrix_string = matrix_string
        self.rows = matrix_string.split('\n')
        pass

    def row(self, index):
        return  [int(number) for number in self.rows[index-1].split()]

    def column(self, index):
        return [int(row.split()[index-1]) for row in self.rows]