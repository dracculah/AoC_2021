# static dictionaries
corrMap = {}
corrMap["["] = "]"
corrMap["("] = ")"
corrMap["{"] = "}"
corrMap["<"] = ">"
corrMap[">"] = "<"
corrMap["}"] = "{"
corrMap[")"] = "("
corrMap["]"] = "["

errorMap = {}
errorMap[" "] = 0
errorMap[")"] = 3
errorMap["]"] = 57
errorMap["}"] = 1197
errorMap[">"] = 25137

def correspondingBracket(c):
	# consistency check
	assert(c in "[({<>})]")
	return corrMap[c]

def checkLine(l): # return bad char and expected char
	stack=[]
	for c in l:
		# consistency check
		assert(c in "[({<>})]")
		if c in "[({<": # opening
			stack.append(c)
		else:
			if len(stack)==0:
				raise Exception("the stack is empty and getting a closing bracket")
				return c, " " # errornous, the stack is empty and getting a closing bracket
			expected_char = correspondingBracket(stack[-1])
			if c == expected_char: # ok
				stack.pop()
			else:
				return c, expected_char # error, got a wrong closing bracket
	return " "," "

def day10_task(linez):
	sum_errorz = 0
	for l in linez:
		c, expected = checkLine(l)
		if c != " ":
			print("DEBUG: line: '{}', expected: '{}' bad char: '{}'".format(l,expected,c))
		sum_errorz += errorMap[c]
	return sum_errorz

example="""[({(<(())[]>[[{[]{<()<>>
[(()[<>])]({[<{<<[]>>(
{([(<{}[<>[]}>{[]{[(<()>
(((({<>}<{<{<>}{[]{[]{}
[[<[([]))<([[{}[[()]]]
[{[{({}]{}}([{[{{{}}([]
{<[[]]>}<{[{[{[]{()[[[]
[<(<(<(<{}))><([]([]()
<{([([[(<>()){}]>(<<{{
<{([{{}}[<[[[<>{}]]]>[]]"""

errorz = day10_task(example.split("\n"))
print("errorz -> {}".format(errorz))
