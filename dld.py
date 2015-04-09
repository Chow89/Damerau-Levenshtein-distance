a = "Rostock"
b = "Rsotock"
i = len(a)
j = len(b)

def dld(a,b,i,j):
	if min(i,j)==0:
		return max(i,j)
	elif i>1 and j>1 and a[i-1]==b[j-2] and a[i-2]==b[j-1]:
		cost = 1 if a[i-1]!=b[j-1] else 0
		return min(dld(a,b,i-1,j)+1,dld(a,b,i,j-1)+1,dld(a,b,i-1,j-1)+cost, dld(a,b,i-2,j-2)+1)
	else:
		cost = 1 if a[i-1]!=b[j-1] else 0
		return min(dld(a,b,i-1,j)+1,dld(a,b,i,j-1)+1,dld(a,b,i-1,j-1)+cost)

print(str(dld(a,b,i,j)))

