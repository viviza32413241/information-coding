import math

def func(text, buffer, cb, z, ce):
	symbol=text.pop(0)
	s=0
	for i in buffer.values():
		s+=i
	q=0
	p=0
	for key, value in buffer.items():
		if key!=symbol:
			q+=value
			p+=value
		else:
			p+=value
			break
	cb_n=cb*s+q*(ce-cb)
	ce_n=cb*s+p*(ce-cb)
	z_n=z*s
	if(len(text)==0):
		return cb_n, z_n, ce_n
	buffer[symbol]+=1
	print(cb, z, ce)
	return func(text, buffer, cb_n, z_n, ce_n)

def gcd_three(a, b, c):
    result = math.gcd(a, b)
    result = math.gcd(result, c)
    return result

def find(n):
	a=2
	i=1
	b=0
	while(b<n):
		b=a**i
		i+=1
	return b, i

text=list("без розуму ні сокирою рубати, ні личака в'язати.")

print(text)
buffer = {}
for i in text[::-1]:
    if i not in buffer:
        buffer[i] = 1
print(buffer)
cb, z, ce = func(text, buffer, 0, 1, 1)
print(cb, z, ce)

gcd=gcd_three(cb, z, ce)
print(gcd)
cb=int(cb/gcd)
z=int(z/gcd)
ce=int(ce/gcd)
print(cb, z, ce)
number, step = find(z)
print(cb*number/z)
