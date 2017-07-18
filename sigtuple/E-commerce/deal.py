input_file = 'input2.txt'

links = dict()
disc = dict()



def apply_discount(key,discount):
	if key not in links:
		if key in disc:
				disc[key] = discount
		else:
			disc[key] = discount
		return

	for k in links[key]:
		if k in links:
			apply_discount(k,discount)
		else:
			if k in disc:
				disc[k] = discount
			else:
				disc[k] = discount


with open(input_file,'r') as f:
	lines = f.readlines()
	n = int(lines[0])

	for line in lines[1:n]:
		u,v = map(int,line.strip().split())
		links.setdefault(u,[]).append(v)

	q = int(lines[n].strip())
	
	for query in lines[n+1:]:
		_query_ = query.strip().split()
		if _query_[0] == 'U':
			key = int(_query_[1])
			discount = int(_query_[2])
			
			apply_discount(key,discount)
	
		if _query_[0] == 'Q':
			key = int(_query_[1])
			if key in disc:
				print disc[key]
			else:
				print 0



