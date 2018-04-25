import sys, csv, re

def getCandFirstLast(n):
	strs = nc1.split()

	ns = len(strs)
v = open(sys.argv[1], "r")
o = open(sys.argv[2], "w")

reader = csv.DictReader(v, delimiter=",", quotechar='"')

for row in reader:
	n = row['name']
	print(n)
