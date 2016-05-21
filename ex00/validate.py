import os
import sys
import unittest

file_practice = os.path.join('dir_practice', 'file_practice.txt')


try:
	f = open(file_practice, 'r')
	print "File opened successfully --- \n Dir and file created."
except IOError:
	print "File not opened sucessfully -- \n Check the directions."
	sys.exit(1)
	

should_string = '''1.  Get a suitable text editor.
2.  Make sure you can get to your text editor quickly.
3.  Run PowerShell or Terminal.
4.  In that terminal window, type "python".
5.  Type "quit()" or "exit".
6.  Learn how to make a directory.
7.  Learn how to change into a directory.
8.  Learn how to save files in your text editor.
9.  Get comfortable with the command line.'''

class TestFileAndDirectoryCreation(unittest.TestCase):

  def test_file_matches(self):
      self.assertEqual(f.read(), should_string,
		msg="The text from the files does not match exactly...")

if __name__ == '__main__':
    unittest.main()
