class Piece:
    nombre: str
    rotation_id: []
    arr_coordinadas: []

    def __init__(self, nombre):
        self.nombre = nombre
        if (nombre == 'O'):
            self.arr_coordinadas = [
                [(0, 1), (0, 0), (1, 1), (1, 0)]
            ]
            self.n_rotations = [0]
            return
        if (nombre == 'I'):
            self.arr_coordinadas = [
                [(-1, 0), (0, 0), (1, 0), (2, 0)],
                [(1, 1), (1, 0), (1, -1), (1, -2)]
            ]
            self.n_rotations = [0, 1]
            return
        if (nombre == 'S'):
            self.arr_coordinadas = [
                [(-1, 0), (0, 0), (0, 1), (1, 1)],
                [(0, 1), (0, 0), (1, 0), (1, -1)]
            ]
            self.n_rotations = [0, 1]
            return
        if (nombre == 'Z'):
            self.arr_coordinadas = [
                [(-1, 1), (0, 1), (0, 0), (1, 0)],
                [(0, -1), (0, 0), (1, 0), (1, 1)]
            ]
            self.n_rotations = [0, 1]
            return
        if (nombre == 'L'):
            self.arr_coordinadas = [
                [(-1, 0), (0, 0), (1, 0), (1, 1)],
                [(-1, 0), (0, 0), (1, 0), (-1, -1)],
                [(0, -1), (0, 0), (0, 1), (1, -1)],
                [(0, 1), (0, 0), (0, -1), (-1, 1)],
            ]
            self.n_rotations = [0, 2, 1, 3]
            return
        if (nombre == 'J'):
            self.arr_coordinadas = [
                [(-1, 0), (0, 0), (1, 0), (-1, 1)],
                [(-1, 0), (0, 0), (1, 0), (1, -1)],
                [(0, -1), (0, 0), (0, 1), (1, 1)],
                [(0, 1), (0, 0), (0, -1), (-1, -1)],
            ]
            self.n_rotations = [0, 2, 1, 3]
            return
        if (nombre == 'T'):
            self.arr_coordinadas = [
                [(-1, 0), (0, 0), (1, 0), (0, 1)],
                [(0, 1), (0, 0), (0, -1), (1, 0)],
                [(-1, 0), (0, 0), (1, 0), (0, -1)],
                [(0, 1), (0, 0), (0, -1), (-1, 0)],
            ]
            self.n_rotations = [0, 2, 1, 3]
            return