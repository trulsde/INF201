
from abc import ABC, abstractmethod
import meshio
import numpy as np

class Point:
    def __init__(self, index, value):
        self._index = index
        self._value = value

    def __int__(self):
        return self._index

    def get_index(self):
        return self._index

class Cell(ABC):
    def __init__(self, index, points):
        self._index = index
        self._points = points
        self._neighbours = []

        assert isinstance(points, list), "Entry 'points' must be a list"

    def points(self):
        return self._points

    def get_neighbours(self):
        return self._neighbours

    @abstractmethod
    def type(self):
        pass

    @abstractmethod
    def index(self):
        pass

    @abstractmethod
    def size(self):
        pass

    @abstractmethod
    def store_neighbours(self, list_of_cells):
        pass


class Line(Cell):
    def __init__(self, index, points):
        super().__init__(index, points)
        self._type = 'Line'

    def __str__(self):
        return f'Line cell {self._index}'

    def size(self):
        return abs(self._points[1] - self._points[0])

    def type(self):
        return self._type

    def index(self):
        return self._index

    def store_neighbours(self, list_of_cells):
        for cell in list_of_cells:
            common_points = set(self._points) & set(cell.points())
            if cell.type() == 'Line' and len(common_points) == 1:
                self._neighbours.append(cell)
            elif cell.type() == 'Triangle' and len(common_points) == 2:
                self._neighbours.append(cell)

class Triangle_cell(Cell):
    def __init__(self, index, points):
        super().__init__(index, points)
        self._type = 'Triangle'

    def __str__(self):
        return f'Triangle cell {self._index}'

    def type(self):
        return self._type

    def index(self):
        return self._index

    def size(self):
        u = self._points[1] - self._points[0]
        v = self._points[2] - self._points[0]

        cross_product = abs(np.cross(u, v))

        return 0.5 * np.linalg.norm(cross_product)

    def id(self):
        return 'Triangle', self._index

    def store_neighbours(self, list_of_cells):
        for cell in list_of_cells:
            matching_points = 0
            for point in cell.points():
                if point in self._points:
                    matching_points += 1
            if matching_points == 2:
                self._neighbours.append(cell)

class Point_cell(Cell):
    def __init__(self, index, points):
        super().__init__(index, points)
    def size(self):
        return 0

    def type(self):
        return 'Point'

    def index(self):
        return self._index

class Mesh:
    def __init__(self, msh_name):
        self._file = msh_name
        self._points = []
        self._cells = []

    def make_cells(self):

        msh = meshio.read(self._file)
        points = msh.points
        cells = msh.cells

        for index, value in enumerate(points):
            self._points.append(Point(index, value))

        lines_dict = {}
        triangles_dict = {}

        cell_index = 0
        while cell_index <= 1:
            if cell_index == 0:
                for j in range(len(cells[cell_index].data)):
                    lines_dict[j] = cells[cell_index].data[j]

                cell_index += 1
            else:
                for j in range(len(cells[cell_index].data)):
                    triangles_dict[j] = cells[cell_index].data[j]
                cell_index += 1

        for index in lines_dict:
            pointlist = []
            for point in self._points:
                if point.get_index() in lines_dict[index]:
                    pointlist.append(point)
            self._cells.append(Line(index, pointlist))

        for index in triangles_dict:
            pointlist = []
            for point in self._points:
                if point.get_index() in triangles_dict[index]:
                    pointlist.append(point)
            self._cells.append(Triangle_cell(index, pointlist))

        for cell in self._cells:
            cell.store_neighbours(self._cells)

    def find_neighbours(self, cell_number):

        for cell in self._cells:
            if cell.index() == cell_number:
                print(f'Neighbours of {cell}:')
                for neighbour in cell.get_neighbours():
                    print(neighbour)

mesh = Mesh('simple.msh')
mesh.make_cells()
mesh.find_neighbours(4)
mesh.find_neighbours(189)
mesh.find_neighbours(222)