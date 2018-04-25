import sys, csv, re

def getCandFirstLast(n):
	strs = n.split()
	ns = len(strs)
	if(ns == 0):
		return ""
	if(strs[0].strip('.').lower() == "rep"):
		del strs[0]


	'''
	match = re.search(r'.*]', strs[ns-1])
	if(match):
		strs.pop()
		ns = len(strs)
	match = re.search(r'[.*', strs[ns-1])
	if(match):
		strs.pop()
		ns = len(strs)
	'''
	strs.pop()
	strs.pop()
	
	ns = len(strs)

	#lw is last word in string nc1
	lw = strs[ns-1].strip('.').lower() 

	if(lw == "sr" or lw == "jr" or lw == "i" or lw == "ii" or lw == "iii" or lw == "iv" or lw == "v" or lw == "vi" or lw == "vii"):
		# print("Stripping last word", nc1, lw)
		strs.pop()
		ns = len(strs)
	
	# print(strs)

	for i in range(0, ns):
		if(i > ns-1):
			break

		#lw is last word in string nc1
		lw = strs[i].strip('.').lower() 

		if(len(lw) == 1):
			del strs[i]
			ns = len(strs)
			i = i-1
		elif(lw == "sr" or lw == "jr" or lw == "i" or lw == "ii" or lw == "iii" or lw == "iv" or lw == "v" or lw == "vi" or lw == "vii"):
			# print("Deleting", lw)
			del strs[i]
			ns = len(strs)
			i = i-1
		else:
			match = re.search(r'\“(.+?)\”', lw)
			if(match):
				del strs[i]
				ns = len(strs)
				i = i-1

	ns = len(strs)
	if(ns == 1):
		firstLast = strs[0]
	elif(ns == 2):
		firstLast = strs[0] + " " + strs[1]
	else:
		firstLast = ""
		for i in range(0, ns):
			firstLast += strs[i]

	return firstLast
		
	


v = open(sys.argv[1], "r")

reader = csv.DictReader(v, delimiter=",", quotechar='"')

for row in reader:
	n = row['name']
	# print(row['person'], ",", row['state'], ",", row['district'], ",", getCandFirstLast(n), ",", row['party'], sep=",")
	print(row['person'], row['state'], row['district'], getCandFirstLast(n), row['party'], sep=",")
