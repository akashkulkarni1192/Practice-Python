def naiive(a,b):
	x=a;y=b
	z=0
	while x>0:
		z=z+y
		x=x-1
	return z

print naiive(1,2)
print naiive(65536,65536)
