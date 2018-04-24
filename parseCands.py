import sys, csv, re

def getFirstLast(nc1):
	strs = nc1.split()

	# ns is numstrs
	ns = len(strs)

	# Remove party affiliation	

	match = re.search(r'(.)', strs[ns-1])
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
	if(ns == 3):
		firstLast = strs[0] + " " + strs[2]
	elif(ns == 2):
		firstLast = strs[0] + " " + strs[1]
	elif(ns == 4):
		firstLast = strs[0] + " " + strs[3]
	else:
		firstLast = "Unknown"
		print("\tError:", nc1, strs)
		
	return firstLast
		
	

print("Merging", sys.argv[1], "and", sys.argv[3])

c1 = open(sys.argv[1], "r")
c2 = open(sys.argv[2], "r")
out = open(sys.argv[3], "w")

reader = csv.DictReader(c1, delimiter=';')
for row in reader:
	nc1 = row['name'] 
	print(getFirstLast(nc1))
