import unittest
import subprocess

proc = subprocess.Popen(
		['python', 'practice.py'], 
		stdout=subprocess.PIPE, 
		stderr=subprocess.STDOUT)

print_text = proc.communicate()[0]

delim = print_text.split('\n')

class TestPrintStatements(unittest.TestCase):

  def test_maternal_and_paternal_insults(self):
      self.assertEqual(delim[0], 'Your mother was a hamster and your father smelt of elderberries!')

  def test_what_have_the_Romans_done_for_us(self):
      self.assertEqual(delim[1].rstrip(), 'All right... all right... but apart from better sanitation, the medicine, education, wine, public order, irrigation, roads, a fresh water system, and public health ... what have the Romans ever done for us?')

  def test_happy_occasion_of_killing(self):
      self.assertEqual(delim[2].rstrip(), 'Please, this is supposed to be a happy occasion. Let us not bicker and argue over who killed who.')

  def test_strange_women_lying_in_ponds(self):
	  self.assertEqual(delim[3].rstrip(), 'Listen, strange women lying in ponds distributing swords is no basis for a system of government. Supreme executive power derives from a mandate from the masses, not from some farcical aquatic ceremony.')

  def test_silly_walks(self):
	  self.assertEqual(delim[4].rstrip(), "I'm sorry to have kept you waiting, but I'm afraid my walk has become rather sillier recently.")

  def test_flesh_wound(self):
	  self.assertEqual(delim[5].rstrip(), "It's just a flesh wound.")	


if __name__ == '__main__':
    unittest.main()
