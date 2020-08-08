def binarytodecimal(n):
	x=[]
	while(n!=1):
		n=n/2
		x.append(n%2)
	y=x[::-1]
	z="".join(y)
	print(z)
def main():
	binarytodecimal(3)

if __name__=="__main__":
	main()
