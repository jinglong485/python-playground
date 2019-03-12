def list_to_file(lst, file, loc = './'):
	location = loc + file
	with open(location,"w") as f:
		for l in lst:
			f.write(l+"\n")
			
def file_to_list(file,loc = './'):
	location = loc + file
	lst = list()
	with open(location, 'rt') as f:
		for line in f:
			lst.append(line.replace('\n', ''))
	return lst
	
def append_to_file(data, file, loc = './'):
	location = loc + file
	with open(location, 'a') as file:
		file.write(data + '\n')