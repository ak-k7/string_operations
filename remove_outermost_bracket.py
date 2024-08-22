# Removes the outermost brackets from the given string
# Example:
#  input : ()(())((()())())
#  output: ()(()())()
def remove_outermost_bracket(str):
	output = ""
	cnt = 0
	for ch in str:
		if ch == '(':
			if cnt > 0: output += ch
			cnt += 1
		else:
			cnt -= 1
			if cnt > 0: output += ch
	return output

if __name__ == '__main__':
  input = '()(())((()())())'
  output = remove_outermost_bracket(input)
  print(output)
