def rcolcheck(arr):
	global columns
	rcol=""
	for i in range(len(arr[0])):
		count=0
		for j in range(columns):
			count+=int(arr[j][i])
		rcol+=str(count%2)
	return rcol
def swapa(a):
	if(a=="1"):
		return "0"
	if(a=="0"):
		return "1"
errorcode="0110110010101101011000011011100100110111001101001101101110011001110010000010110001001100101011000010011101010111010001101001101100110011010010110010100111001100100000011010010011011100010000001101000101100001011100000111000010110100101101110011001011011100110111001100101100100100000011000010110111010110010000100000011000110011011110110110101100110101101111011100100111010000111001100100000011010010011011100010000001110101101101110011010000110000110111000001110000011010010011011100110010101110011001110011001011100010000000011110101110100001001010"
array1 = [errorcode[i:i+25] for i in range(0, len(errorcode), 25)]
columns=len(errorcode)//25
sumRow=""
for i in range(columns):
	count=0
	for n in array1[i]:
		count+=int(n)
	sumRow+=str(count%2)
print("SumRow: " + sumRow)

print("RCol: " + rcolcheck(array1))
for i in range(columns):
	tprint=""
	for j in range(25):
		tprint+=array1[i][j]+" | "
	print(tprint+sumRow[i])
print(" * ".join([char for char in rcolcheck(array1)]))

rcol=rcolcheck(array1)

for i in range(columns):
	if(sumRow[i]=="1"):
		for j in range(25):
			if(rcol[j]=="1"):
				array1[i]=array1[i][:j]+swapa(array1[i][j])+array1[i][j+1:]
sumRow=""
for i in range(columns):
	count=0
	for n in array1[i]:
		count+=int(n)
	sumRow+=str(count%2)
print()
print()
for i in range(columns):
	tprint=""
	for j in range(25):
		tprint+=array1[i][j]+" | "
	print(tprint+sumRow[i])
print(" * ".join([char for char in rcolcheck(array1)]))