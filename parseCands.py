import sys, csv, re

def getFirstLast(nc1):
	strs = nc1.split()

	# ns is numstrs
	ns = len(strs)

	# Remove party affiliation	

	match = re.search(r'\(.\)', strs[ns-1])
	if(len(strs[ns-1]) > 3 and match):
		strs[ns-1] = strs[ns-1][:-3]
		print(strs[ns-1])
	elif(ns > 1 and match):
		strs.pop()

	ns = len(strs)

	#lw is last word in string nc1
	lw = strs[ns-1].strip('.').lower() 

	if(lw == "sr" or lw == "jr" or lw == "i" or lw == "ii" or lw == "iii" or lw == "iv" or lw == "v" or lw == "vi" or lw == "vii"):
		# print("Stripping last word", nc1, lw)
		strs.pop()

	ns = len(strs)

	print("Starting on ", strs)
	for i in range(0, ns):
		if(i > ns-1):
			break
		print("\t", i, ":", strs)

		#lw is last word in string nc1
		lw = strs[i].strip('.').lower() 

		if(len(lw) == 1):
			del strs[i]
			ns = len(strs)
			i = i-1
		if(lw == "sr" or lw == "jr" or lw == "i" or lw == "ii" or lw == "iii" or lw == "iv" or lw == "v" or lw == "vi" or lw == "vii"):
			print("Deleting", lw)
			del strs[i]
			ns = len(strs)
			i = i-1
		else:
			match = re.search(r'\(.\)', lw)
			if(len(strs[i]) > 3 and match):
				strs[i] = strs[i][:-3]
				print(strs[i])
			elif(ns > 1 and match):
				del strs[i]
				ns = len(strs)
				i = i-1
			else:
				match = re.search(r'\(.*\)', lw)
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
'''
	elif(ns == 3):
		firstLast = strs[0] + " " + strs[2]
	elif(ns == 4):
		firstLast = strs[0] + " " + strs[3]
'''
	
		
		
	

print("Merging", sys.argv[1], "and", sys.argv[3])

c1 = open(sys.argv[1], "r")
c2 = open(sys.argv[2], "r")
out = open(sys.argv[3], "w")

reader = csv.DictReader(c1, delimiter=';')
# getFirstLastTwo("foo bar is cool")
for row in reader:
	nc1 = row['name'] 
	print(getFirstLast(nc1))
