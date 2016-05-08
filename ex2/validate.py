import unittest
import subprocess

proc = subprocess.Popen(
        ['python', 'practice.py'],
        stdout=subprocess.PIPE,
        stderr=subprocess.STDOUT)

print_text = proc.communicate()[0]

delim = print_text.split(' ')

stripped = []

for string in delim:
    n = string.strip()
    stripped.append(n)

print stripped

class TestCanUseComments(unittest.TestCase):

    def test_correct_text_output(self):
        self.assertEqual(stripped, ['Monty', 'Python', 'and', 'the', 'Flying', 'Circus'])


if __name__ == '__main__':
    unittest.main()                   
