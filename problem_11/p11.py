from decimal import Decimal
from typing import List
from statistics import mean
from operator import mul
from functools import reduce


class ProductMatrix(object):
    def __init__(self, width: int, height: int, grid_list: list) -> None:
        self.width = width
        self.height = height
        self.grid = grid_list

    def __repr__(self) -> str:
        out = [str(self.get_row(r)) for r in range(self.height)]
        return 'ProductMatrix {\n' + '\n'.join(['  ' + o for o in out]) + '\n}'

    @staticmethod
    def string_to_grid_list(s: str) -> list:
        return [int(s.strip()) for s in s.strip().replace('\n', ' ').split(' ')]

    def get_coord(self, x: int, y: int) -> int:
        return self.grid[(y * self.height) + x]

    def get_row(self, row: int, start=None, length=None) -> List[int]:
        start = (row * self.height) if not start else (row * self.height) + start
        end = start + self.width if not length else start + length
        return self.grid[start:end]

    def get_col(self, col: int) -> List[int]:
        return [self.get_coord(col, x) for x in range(self.height)]

    def get_row_average(self, row: int) -> Decimal:
        return mean([Decimal(d) for d in self.get_row(row)])

    @staticmethod
    def prod(l: List[int]) -> int:
        return reduce(mul, l, 1)

    def get_diag_product(self, reflect_y=False) -> int:
        offset = self.width - 1 if reflect_y else 0
        modifier = -1 if reflect_y else 1
        return self.prod([self.get_coord(offset + (modifier * x), x) for x in range(self.width)])

    def largest_diag_product(self) -> int:
        p1 = self.get_diag_product()
        p2 = self.get_diag_product(reflect_y=True)
        return max(p1, p2)

    def largest_row_product(self) -> int:
        return max([self.prod(self.get_row(r)) for r in range(self.height)])

    def largest_col_product(self):
        return max([self.prod(self.get_col(c)) for c in range(self.width)])

    def largest_product(self):
        return max(self.largest_col_product(), self.largest_row_product(), self.largest_diag_product())

    def submatrix_from_bounds(self, top_x, top_y, bottom_x, bottom_y) -> 'ProductMatrix':
        rows = [self.get_row(r, start=top_x, length=bottom_x - top_x + 1) for r in range(top_y, bottom_y + 1)]
        rows_flat = [row for sublist in rows for row in sublist]
        return ProductMatrix(bottom_x - top_x + 1, bottom_y - top_y + 1, rows_flat)

    def adjacent_product_search(self, length: int) -> int:
        """divide step is incomplete. just using brute force for now"""
        matrices = []
        for start_x in range(self.width - (length - 1)):
            for start_y in range(self.height - (length - 1)):
                matrices.append(self.submatrix_from_bounds(top_x=start_x,
                                                           top_y=start_y,
                                                           bottom_x=start_x + length - 1,
                                                           bottom_y=start_y + length - 1))

        return max([m.largest_product() for m in matrices])
