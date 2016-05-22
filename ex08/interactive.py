print "Print formatting changes drastically in Python 3."
print "I've never spent too much time trying to learn it,"
print "but we will give it a cursory treatment here."

print '''
Pretend the following code block has been entered for you.

formatter = "%r %r %r %r"

print formatter % (22, 23, 24, 25)
print formatter % ("twenty-two", "twenty-three", "twenty-four", "twenty-five")
print formatter % (True, False, False, True)
print formatter % (formatter, formatter, formatter, formatter)
print formatter % (
    "Once upon a time,",
    "There was a princess.",
    "And something came and",
    "saved her from the dragon"
)

Press Enter to see the code run.
'''

raw_input()

formatter = "%r %r %r %r"

print formatter % (1, 2, 3, 4)
print formatter % ("one", "two", "three", "four")
print formatter % (True, False, False, True)
print formatter % (formatter, formatter, formatter, formatter)
print formatter % (
    "I had this thing.",
    "That you could type up right.",
    "But it didn't sing.",
    "So I said goodnight."
)

