def lines_code(filename):
	with open(filename, 'r') as f, open('my_new_code.py', 'w') as fw:
		comment=False
		for line in f:
			current= line.strip()
			if current.startswith('#'):
				continue

			if (current =='"""' or current.startswith('"""')) and not comment:
				comment = True
				continue
			if (current =='"""' or current.startswith('"""')) and comment:
				comment = False
				continue
			if comment:
				continue
			else:
				fw.write(line)


lines_code('comments.txt')

