import unittest

from triangle_func import get_triangle_type


class TestTriangleType(unittest.TestCase):

    def test_equilateral(self):
        self.assertEqual(get_triangle_type(5, 5, 5), 'equilateral')

    def test_isosceles(self):
        self.assertEqual(get_triangle_type(5, 5, 3), 'isosceles')
        self.assertEqual(get_triangle_type(3, 5, 5), 'isosceles')
        self.assertEqual(get_triangle_type(5, 3, 5), 'isosceles')

    def test_nonequilateral(self):
        self.assertEqual(get_triangle_type(3, 4, 5), 'nonequilateral')

    def test_incorrect_sides(self):
        self.assertEqual(get_triangle_type(-1, 2, 3), 'IncorrectTriangleSides')
        self.assertEqual(get_triangle_type(0, 1, 2), 'IncorrectTriangleSides')
        self.assertEqual(get_triangle_type(2, 3, 6), 'IncorrectTriangleSides')

if __name__ == '__main__':
    unittest.main()
