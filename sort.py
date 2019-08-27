a=[3,4,56,2,1]

c=[]

while len(a)>0 :
	tmp=a[0]
	for x in a:
		if x<tmp :
			
			tmp=x

	c.append(tmp)
	a.remove(tmp)
print(c)