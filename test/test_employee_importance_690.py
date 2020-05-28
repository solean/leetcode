from employee_importance_690 import get_importance
from misc import Employee
import unittest

class TestEmployeeImportance(unittest.TestCase):

    def test_1(self):
        employees = [Employee(1, 5, [2, 3]), Employee(2, 3, []), Employee(3, 3, [])]
        self.assertEqual(get_importance(employees, 1), 11)

    def test_2(self):
        employees = [Employee(1, 5, [2, 3]), Employee(2, 3, [4]), Employee(4, 1, [])]
        self.assertEqual(get_importance(employees, 1), 13)

