import sys, csv, re

def getCandFirstLast(n):
	strs = n.split()
	ns = len(strs)
	if(ns == 0):
		return ""
	lw = strs[0].strip('.').lower()  
	if(lw == "rep" or lw == "sen"):
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
			if(i != 0):
				firstLast += " "
			firstLast += strs[i]

	return firstLast
		
	


v = open(sys.argv[1], "r")
c = open(sys.argv[2], "r")

reader = csv.DictReader(v, delimiter=",", quotechar='"')

# print(nn, row['person'], CID, sep=",")
print("name,person,CID")

for row in reader:
	n = row['name']
	# print(row['person'], ",", row['state'], ",", row['district'], ",", getCandFirstLast(n), ",", row['party'], sep=",")
	# print("personID, name") 
	nn = getCandFirstLast(n)
	c.seek(0)
	r2 = csv.DictReader(c, delimiter=',')
	CID = -1
	for row2 in r2:
		if(row2['name'] == nn):
			# print("Matched", nn, "with", row2["name"])
			CID = row2['CID']
			print(nn, row['person'], CID, sep=",")
			break
