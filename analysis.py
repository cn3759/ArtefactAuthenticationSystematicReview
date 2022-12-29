import string

f = open("input.txt", "r")

counter = 0
lines = 0
results = []
duplicates = 0

expected = []
for i in range(1,1258):
	expected.append(str(i))

for line in f:
	lines = lines + 1
	if line[0:4] == "ID: ":
		counter = counter + 1
		value = line.split()[1]
		if value[-1] == "\\":
			value = value[:-1]
		if value in results:
			print "Duplicate value: " + value
			duplicates = duplicates + 1
		else:
			expected.remove(value)
			results.append(value)

print "Counter final value: " + str(counter)
print "Number of duplicates found: " + str(duplicates)
print "Length of results: " + str(len(results))
print "Length of expected ID values NOT used (should be 0): " + str(len(expected))
if len(expected) != 0:
	print expected
f.close()
