from random import choice

keyword_flashcards = {
	"and" 		: "Logical and.",
	"as"  		: "Part of the with-as statement.",
	"assert"	: "Assert (ensure) that something is true.",
	"break"		: "Stop this loop right now.",
	"class"		: "Define a class.",
	"continue"	: "Don't process more of the loop, do it again.",
	"def"		: "Define a function.",
	"del"		: "Delete from dictionary",
	"elif"		: "Else if condition.",
	"else"		: "Else condition.",
	"except"	: "If an exception happens, do this.",
	"exec"		: "Run a string as Python.",
	"finally"	: "Exceptions or not, finally do this no matter what.",
	"for"		: "Loop over a collection of things.",
	"from"		: "Importing specific parts of a module.",
	"global"	: "Declare that you want a global variable.",
	"if"		: "If condition.",
	"import"	: "Import a module into this one to use.",
	"in"		: "Part of for-loops. Also a test of X in Y.",
	"lambda"	: "Create a short anonymous function.",
	"not"		: "Logical not.",
	"or"		: "Logical or.",
	"pass"		: "This block is empty.",
	"print"		: "Print this string.",
	"raise"		: "Raise an exception when things go wrong.",
	"return"	: "Exit the function with a return value.",
	"try"		: "Try this block, and if exception, go to except.",
	"while"		: "While loop.",
	"with"		: "With an expression as a variable do.",
	"yield"		: "Pause here and return to caller."
}

data_type_flashcards = {
	"True" 		: "True boolean value.",
	"False"		: "False boolean value.",
	"None"		: "Represents 'nothing' or 'no value'.",
	"strings"	: "Stores textual information.",
	"numbers"	: "Stores integers.",
	"floats"	: "Stores decimals.",
	"lists"		: "Stores a list of things.",
	"dicts"		: "Stores a key=value mapping of things."
}

escape_flashcards = {
	r'\\'	: "Backslash",
	r'\''	: "Single-quote",
	r'\"'	: "Double-quote",
	r'\a'	: "Bell",
	r'\b'	: "Backspace",
	r'\f'	: "Formfeed",
	r'\n'	: "Newline",
	r'\r'	: "Carriage",
	r'\t'	: "Tab",
	r'\v'	: "Vertical tab"
}

string_format_flashcards = {
	r'%d'	: "Decimal integers (not floating point).",
	r'%i'	: r'Same as %d.',
	r'%o'	: "Octal number.",
	r'%u'	: "Unsigned decimal.",
	r'%x'	: "Hexadecimal lowercase.",
	r'%X'	: "Hexadecimal uppercase.",
	r'%e'	: "Exponential notation, lowercase 'e'.",
	r'%E'	: "Exponential notation, uppercase 'E'.",
	r'%f'	: "Floating point real number.",
	r'%F'	: r'Same as %f.',
	r'%g'	: r'Either %f or %e, whichever is shorter.',
	r'%G'	: r'Same as %g but uppercase.',
	r'%c'	: "Character format.",
	r'%r'	: "Repr format (debugging format).",
	r'%s'	: "String format.",
	r'%%'	: "A percent sign."
}

operators_flashcards = {
	"+"	: "Addition",
	"-"	: "Subtraction",
	"*"	: "Multiplication",
	"**": "Power of",
	"/"	: "Division",
	"//": "Floor division",
	"%"	: "String interpolate or modulus.",
	"<"	: "Less than",
	">" : "Greater than",
	"<=": "Less than equal",
	">=": "Greater than equal",
	"==": "Equal",
	"!=": "Not equal",
	"<>": "Not equal",
	"()": "Parenthesis",
	"[]": "List brackets",
	"{}": "Dict curly braces",
	"@" : "At (decorators)",
	","	: "Comma",
	":"	: "Colon",
	"."	: "Dot",
	"="	: "Assign equal",
	";" : "semi-colon",
	"+=": "Add and assign",
	"-=": "Subtract and assign",
	"*=": "Multiply and assign",
	"/=": "Divide and assign",
	"//=": "Floor divide and assign",
	"%=": "Modulus assign",
	"**=": "Power assign"
}

print "I have been kind enough to put all these terms" 
print "and definitions into flashards.  I have only seen" 
print "about half of these used in the wild."

print "Do them as long as you can stand it :-)"

def get_random_key_value(d):
	key = choice(d.keys())
	value = d[key]
	return (key, value)

def quiz(dict_tuple):
	print "==============================="
	print "TERM: %s" % dict_tuple[0]
	print "Press Enter to see definition."
	raw_input()
	print "DEFINITION: %s" % dict_tuple[1]
	print "==============================="

game_on = True

while game_on:
	print "Pick a category from the following."
	print "1 Keywords"
	print "2 Data Types"
	print "3 Escape Characters"
	print "4 String Formatters"
	print "5 Operators"
	print "6 Quit"

	prompt = int(raw_input("> "))

	if prompt == 1:
		flashcard = get_random_key_value(keyword_flashcards)
		quiz(flashcard)
	elif prompt == 2:
		flashcard = get_random_key_value(data_type_flashcards)
		quiz(flashcard)
	elif prompt == 3:
		flashcard = get_random_key_value(escape_flashcards)
		quiz(flashcard)
	elif prompt == 4:
		flashcard = get_random_key_value(string_format_flashcards)
		quiz(flashcard)
	elif prompt == 5:
		flashcard = get_random_key_value(operators_flashcards)
		quiz(flashcard)
	else:
		game_on = False

print "Game over."
