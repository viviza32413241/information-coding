def printarray(arr):
	global rows
	for i in range(rows):
		tprint=""
		for j in range(len(arr[i])):
			tprint+=str(arr[i][j])+" | "
		print(tprint)

def arrInAscii(arr):
	global rows
	newarr=[[' ' for _ in range(3)] for _ in range(rows)]
	for i in range(rows):
		for j in range(3):
			newarr[i][j]=ord(arr[i][j])
	return newarr

def arrInBin(arr):
	global rows
	newarr=[[' ' for _ in range(3)] for _ in range(rows)]
	for i in range(rows):
		for j in range(3):
			newarr[i][j]=bin(arr[i][j])[2:].zfill(8)
	return newarr

def messagewithconrol(lst, step):
	s=0
	for i in range(step-1, len(lst), step*2):
		for j in range(min(step, len(lst) - i)):
			s+=int(lst[i+j])
	if(s%2==0):
		return 0
	else:
		return 1
def errorwithconrol(lst, step):
	s=0
	can=False
	for i in range(step-1, len(lst), step*2):
		for j in range(min(step, len(lst) - i)):
			if(can):
				s+=int(lst[i+j])
			can=True
	if(s%2==0):
		return 0
	else:
		return 1
def swapcode(code, pos, error):
	new_code=code[:pos]+error+code[pos+len(error):]
	return new_code

def swapa(a):
	if(a=="1"):
		return "0"
	if(a=="0"):
		return "1"

text="learning beautifies in happiness, and comforts in unhappiness."
rows=0
while(True):
	if(len(text)%3==0):
		rows=len(text)//3
		break
	else:
		text+=" "
array1 = [text[i:i+3] for i in range(0, len(text), 3)]
printarray(array1)
array2=arrInAscii(array1)
printarray(array2)
array3=arrInBin(array2)
printarray(array3)


array4=["" for i in range(rows)]
for i in range(rows):
	for j in range(3):
		array4[i]+=array3[i][j]
printarray(array4)


for i in range(rows):
	for j in range(5):
		k=2**j-1
		array4[i]=array4[i][:k]+"2"+array4[i][k:]
print("\n\n\n")
printarray(array4)

for i in range(rows):
	for j in range(5):
		k=2**j
		r=messagewithconrol(array4[i], k)
		array4[i]=array4[i][:k-1]+str(r)+array4[i][k:]
print("\n\n\n")
printarray(array4)

array4[0]=swapcode(array4[0], 5, "0")
array4[3]=swapcode(array4[3], 8, "1")
array4[4]=swapcode(array4[4], 12, "1")
print("\n\n\n")
printarray(array4)

for i in range(rows):
	index=0
	for j in range(5):
		k=2**j
		r=errorwithconrol(array4[i], k)
		if(r != int(array4[i][k-1])):
			index+=k
	if(index>0):
		index-=1
		print("Error in "+str(index)+" index in "+str(i+1)+" line.")
		array4[i]=array4[i][:index]+swapa(array4[i][index])+array4[i][index+1:]
print("\n\n\n")
printarray(array4)

