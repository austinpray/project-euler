from problem_11.p11 import ProductMatrix
from decimal import Decimal as Dec

horizontal_test_1 = """
01 02 03 04
05 06 07 08
09 10 11 12
13 14 15 16
"""

ht1 = ProductMatrix(4, 4, ProductMatrix.string_to_grid_list(horizontal_test_1))

horizontal_false_pos_test_1 = """
01 01 01 01
01 01 01 01
50 01 01 01
10 10 10 10
"""

hfpt1 = ProductMatrix(4, 4, ProductMatrix.string_to_grid_list(horizontal_false_pos_test_1))


def test_get_row():
    row = ht1.get_row(0)
    assert row[0] == 1
    assert row[1] == 2
    assert row[2] == 3
    assert row[3] == 4


def test_get_row_average():
    assert ht1.get_row_average(0) == Dec('2.5')


def test_get_products():
    # diag
    assert ht1.get_diag_product() == 1056
    assert ht1.get_diag_product(reflect_y=True) == 3640
    assert ht1.largest_diag_product() == 3640

    # horiz
    assert hfpt1.largest_row_product() == 10000

    # vert
    assert hfpt1.largest_col_product() == 500


def test_submatrix():
    sub = ht1.submatrix_from_bounds(1, 1, 2, 2)
    print()
    print(sub)
    assert sub.get_coord(0, 0) == 6
    assert sub.get_coord(1, 0) == 7
    assert sub.get_coord(0, 1) == 10
    assert sub.get_coord(1, 1) == 11

    sub = ht1.submatrix_from_bounds(0, 0, 1, 1)
    assert sub.get_coord(0, 0) == 1
    assert sub.get_coord(1, 0) == 2
    assert sub.get_coord(0, 1) == 5
    assert sub.get_coord(1, 1) == 6

    sub = ht1.submatrix_from_bounds(2, 2, 3, 3)
    assert sub.get_coord(0, 0) == 11
    assert sub.get_coord(1, 0) == 12
    assert sub.get_coord(0, 1) == 15
    assert sub.get_coord(1, 1) == 16


vertical_test_1 = """
01 05 13 09
02 06 14 10
03 07 15 11
04 08 16 12
"""

vt1 = ProductMatrix(4, 4, ProductMatrix.string_to_grid_list(vertical_test_1))

semi_complicated_1 = """
00 00 00 00 00 00 00 00 00 00
00 00 00 00 00 00 00 00 00 00
00 00 00 10 00 00 00 00 00 00
00 00 00 10 00 00 00 00 00 00
00 00 00 10 00 00 00 00 00 00
00 00 00 10 00 00 00 00 00 00
00 00 00 00 00 00 00 00 00 00
00 00 00 00 00 00 00 00 00 00
00 00 00 00 00 00 00 00 00 00
00 00 00 00 00 00 00 00 00 00
"""

semi_complicated_2 = """
00 00 00 00 00 00 00 00 00 00
00 00 00 00 00 00 00 00 00 00
00 00 00 00 00 00 00 00 00 00
00 00 00 10 10 10 10 00 00 00
00 00 00 00 00 00 00 00 00 00
00 00 00 00 00 00 00 00 00 00
00 00 00 00 00 00 00 00 00 00
00 00 00 00 00 00 00 00 00 00
00 00 00 00 00 00 00 00 00 00
00 00 00 00 00 00 00 00 00 00
"""

semi_complicated_3 = """
00 00 00 00 00 00 00 00 00 00
00 00 00 00 00 00 00 00 00 00
00 00 00 00 00 00 00 00 00 00
00 00 00 00 00 00 10 00 00 00
00 00 00 00 00 10 00 00 00 00
00 00 00 00 10 00 00 00 00 00
00 00 00 10 00 00 00 00 00 00
00 00 00 00 00 00 00 00 00 00
00 00 00 00 00 00 00 00 00 00
00 00 00 00 00 00 00 00 00 00
"""

semi_complicated_4 = """
00 00 00 00 00 00 00 00 00 00
00 00 00 00 00 00 00 00 00 00
00 00 00 00 00 00 00 00 00 00
00 00 00 00 00 00 00 00 00 00
00 10 00 00 00 00 00 00 00 00
00 00 10 00 00 00 00 00 00 00
00 00 00 10 00 00 00 00 00 00
00 00 00 00 10 00 00 00 00 00
00 00 00 00 00 00 00 00 00 00
00 00 00 00 00 00 00 00 00 00
"""

sc1 = ProductMatrix(10, 10, ProductMatrix.string_to_grid_list(semi_complicated_1))
sc2 = ProductMatrix(10, 10, ProductMatrix.string_to_grid_list(semi_complicated_2))
sc3 = ProductMatrix(10, 10, ProductMatrix.string_to_grid_list(semi_complicated_3))
sc4 = ProductMatrix(10, 10, ProductMatrix.string_to_grid_list(semi_complicated_4))


def test_find_adjacent_product():
    assert sc1.adjacent_product_search(4) == 10000
    assert sc2.adjacent_product_search(4) == 10000
    assert sc3.adjacent_product_search(4) == 10000
    assert sc4.adjacent_product_search(4) == 10000


input_string = """
08 02 22 97 38 15 00 40 00 75 04 05 07 78 52 12 50 77 91 08
49 49 99 40 17 81 18 57 60 87 17 40 98 43 69 48 04 56 62 00
81 49 31 73 55 79 14 29 93 71 40 67 53 88 30 03 49 13 36 65
52 70 95 23 04 60 11 42 69 24 68 56 01 32 56 71 37 02 36 91
22 31 16 71 51 67 63 89 41 92 36 54 22 40 40 28 66 33 13 80
24 47 32 60 99 03 45 02 44 75 33 53 78 36 84 20 35 17 12 50
32 98 81 28 64 23 67 10 26 38 40 67 59 54 70 66 18 38 64 70
67 26 20 68 02 62 12 20 95 63 94 39 63 08 40 91 66 49 94 21
24 55 58 05 66 73 99 26 97 17 78 78 96 83 14 88 34 89 63 72
21 36 23 09 75 00 76 44 20 45 35 14 00 61 33 97 34 31 33 95
78 17 53 28 22 75 31 67 15 94 03 80 04 62 16 14 09 53 56 92
16 39 05 42 96 35 31 47 55 58 88 24 00 17 54 24 36 29 85 57
86 56 00 48 35 71 89 07 05 44 44 37 44 60 21 58 51 54 17 58
19 80 81 68 05 94 47 69 28 73 92 13 86 52 17 77 04 89 55 40
04 52 08 83 97 35 99 16 07 97 57 32 16 26 26 79 33 27 98 66
88 36 68 87 57 62 20 72 03 46 33 67 46 55 12 32 63 93 53 69
04 42 16 73 38 25 39 11 24 94 72 18 08 46 29 32 40 62 76 36
20 69 36 41 72 30 23 88 34 62 99 69 82 67 59 85 74 04 36 16
20 73 35 29 78 31 90 01 74 31 49 71 48 86 81 16 23 57 05 54
01 70 54 71 83 51 54 69 16 92 33 48 61 43 52 01 89 19 67 48
"""

final_gpf = ProductMatrix(width=20, height=20, grid_list=ProductMatrix.string_to_grid_list(input_string))


def test_string_to_grid():
    assert final_gpf.grid[0] == 8
    assert final_gpf.grid[-1] == 48
    assert final_gpf.grid[16] == 50


def test_get_coord():
    assert final_gpf.get_coord(0, 0) == 8
    assert final_gpf.get_coord(19, 19) == 48
    assert final_gpf.get_coord(16, 0) == 50
    assert final_gpf.get_coord(0, 16) == 4


if __name__ == "__main__":
    print(final_gpf.adjacent_product_search(length=4))
