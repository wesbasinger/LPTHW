import unittest
import subprocess

from practice import *

proc = subprocess.Popen(
        ['python', 'practice.py'],
        stdout=subprocess.PIPE,
        stderr=subprocess.STDOUT)

print_text = proc.communicate()[0]

delim = print_text.split('\n')

class TestCanUseStringFormatting(unittest.TestCase):

    def test_can_print_name_string(self):
		self.assertEqual(
			str(delim[0].rstrip()), 
			"Let's talk about %s." % my_name
		)

    def test_can_print_height_string(self):
		self.assertEqual(
			str(delim[1].rstrip()),
			"He's %s inches tall." % my_height
		)

    def test_can_print_weight_string(self):
		self.assertEqual(
			str(delim[2].rstrip()),
			"He's %s pounds heavy." % my_weight
		)

    def test_can_print_eyes_and_hair(self):
		self.assertEqual(
			str(delim[3].rstrip()), 
			"He's got %s eyes and %s hair." % (my_eyes, my_hair)
		)

    def test_can_print_teeth_string(self):
		self.assertEqual(
			str(delim[4].rstrip()), 
			"His teeth are usually %s depending on the coffee." % (my_teeth)
		)


if __name__ == '__main__':
    unittest.main()   

