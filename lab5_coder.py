def printarray(arr):
	global columns
	for i in range(columns):
		tprint=""
		for j in range(3):
			tprint+=str(arr[i][j])+" | "
		print(tprint)

def arrInAscii(arr):
	global columns
	newarr=[[' ' for _ in range(3)] for _ in range(columns)]
	for i in range(columns):
		for j in range(3):
			newarr[i][j]=ord(arr[i][j])
	return newarr

def arrInBin(arr):
	global columns
	newarr=[[' ' for _ in range(3)] for _ in range(columns)]
	for i in range(columns):
		for j in range(3):
			newarr[i][j]=bin(arr[i][j])[2:].zfill(8)
	return newarr

def array4func(arr):
	global columns
	arr_row=["" for _ in range(columns)]
	for i in range(columns):
		for j in range(3):
			arr_row[i]+=arr[i][j]
	for i in range(columns):
		count=0
		for n in arr_row[i]:
			count+=int(n)
		arr_row[i]+=str(count%2)
		print("Row "+str(i+1)+" : "+arr_row[i])
	rcol=""
	for i in range(len(arr_row[0])):
		count=0
		for j in range(columns):
			count+=int(arr_row[j][i])
		rcol+=str(count%2)
	print("Rcol "+ rcol)
	result=""
	for a in arr_row:
		result+=a
	result+=rcol
	print("Result: " + result)
	return result

def swapcode(code, pos, error):
	new_code=code[:pos]+error+code[pos+len(error):]
	return new_code

text="learning beautifies in happiness, and comforts in unhappiness."
columns=0
while(True):
	if(len(text)%3==0):
		columns=len(text)//3
		break
	else:
		text+=" "
array1 = [text[i:i+3] for i in range(0, len(text), 3)]
printarray(array1)
array2=arrInAscii(array1)
printarray(array2)
array3=arrInBin(array2)
printarray(array3)
result=array4func(array3)

errorresult=swapcode(result, 8, "10101")
print("Result: "+errorresult)
