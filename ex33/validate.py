import unittest
import subprocess

proc = subprocess.Popen(
        ['python', 'practice.py'],
        stdout=subprocess.PIPE,
        stderr=subprocess.STDOUT)

print_text = proc.communicate()[0]

delim = print_text.split('\n')

class CanCreateWhileLoops(unittest.TestCase):

	def test_can_use_while_loop_to_print_to_5(self):
		self.assertEqual(delim[0], "1")
		self.assertEqual(delim[1], "2")
		self.assertEqual(delim[2], "3")
		self.assertEqual(delim[3], "4")
		self.assertEqual(delim[4], "5")

	def test_can_use_while_loop_to_print_items_of_list(self):
		self.assertEqual(delim[5], "protractor")
		self.assertEqual(delim[6], "compass")
		self.assertEqual(delim[7], "calculator")
		self.assertEqual(delim[8], "slide rule")
		self.assertEqual(delim[9], "pencil")

if __name__ == '__main__':
    unittest.main()   
