import unittest
import subprocess

proc = subprocess.Popen(
        ['python', 'practice.py'],
        stdout=subprocess.PIPE,
        stderr=subprocess.STDOUT)

print_text = proc.communicate()[0]

delim = print_text.split('\n')

class TestCanUseMathOperators(unittest.TestCase):

    def test_can_print_6(self):
        self.assertEqual(int(delim[0]), 6)

    def test_can_print_neg_3(self):
        self.assertEqual(int(delim[1]), -3)

    def test_can_print_100_with_multiplication(self):
        self.assertEqual(int(delim[2]), 100)

    def test_can_print_boolean_true(self):
        self.assertEqual(delim[3].rstrip(), "True")

    def test_can_print_4_with_3_operations(self):
        self.assertEqual(int(delim[4]), 4)

    def test_can_print_1_with_modular_division(self):
        self.assertEqual(int(delim[5]), 1)

    def test_can_print_a_float(self):
        self.assertEqual(float(delim[6]), 1.23)

    def test_can_print_boolean_false_with_diff_ops(self):
        self.assertEqual(delim[7].rstrip(), "False")


if __name__ == '__main__':
    unittest.main()                   
