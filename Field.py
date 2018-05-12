

class Field:
    def __init__(self, width=10, height=10):
        self.cells = []
        self.width, self.height = width, height
        for i in range(self.height):
            self.cells.append[]
            for j in range(self.width):
                self.cells[i].append(Cell.Cell())

    def make_matrix(self):
        matrix = Matrix.Matrix()
        for i in range(self.height):
            matrix.add
            for j in range(self.width):
                matrix[i].append(bool(self.cells[i]))
        return matrix

    def update(self):
        pass
