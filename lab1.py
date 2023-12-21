import math
def findY(x1, x2):
	return (2*(1.5*x1+x2)+x1+x2)

def printTable2(y, p):
	for key, value in y.items():
		print(key, value, p[key])

def funcTable3(y, x1, n):
	result = 0
	condition = (y - 4 * x1) / 3
	if (condition >= 1 and condition <= n and condition - int(condition) == 0):
		result = 1 / pow(n, 2)
	return result

def printTable3(table, x, y):
	print("x1 y")
	for i in range(len(x)):
		for j in range(len(y)):
			print(x[i], y[j], table[i][j])

def funcTable4(y, x1, n, p):
	result = 0
	condition = (y - 4 * x1) / 3

	if condition >= 1 and condition <= n and condition - int(condition) == 0:
		result = (1 / pow(n, 2)) * math.log((1 / n) / p, 2)
		print((1 / n) / y)

	return result

def printTable4(table, x, y):
	print("x1 y")
	for i in range(len(x)):	
		sum_row=0
		for j in range(len(y)):
			print(x[i], y[j], table[i][j])
			sum_row+=table[i][j]
		print("Sum row = " + str(sum_row))


n=20
table1 = [[0] * n for _ in range(n)]
for x1 in range(n):
	for x2 in range(n):
		table1[x1][x2]=findY(x1+1 , x2+1)

for i in range(n):
	print(table1[i])

dict_y2={}
dict_p={}
for y2 in range(int(table1[0][0]), int(table1[n-1][n-1])+1):
	dict_y2[y2]=sum(x.count(y2) for x in table1)
# print(dict_y2)

for key, value in dict_y2.items():
	dict_p[key]=value/pow(n, 2)

printTable2(dict_y2, dict_p)


y2 = range(int(table1[0][0]), int(table1[n-1][n-1])+1)
x1 = range(1,n+1)
table3=[[0] * len(y2) for _ in range(len(x1))]
table4=[[0] * len(y2) for _ in range(len(x1))]
sum_table4=0
for i in range(len(x1)):
	for j in range(len(y2)):
		table3[i][j]=funcTable3(y2[j], x1[i], n)
		table4[i][j]=funcTable4(y2[j], x1[i], n, dict_p[y2[j]])
		sum_table4+=table4[i][j]

printTable3(table3, x1, y2)
printTable4(table4, x1, y2)
print("Sum table4 = "+ str(sum_table4))