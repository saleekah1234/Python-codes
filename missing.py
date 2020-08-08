
#program  to find the  positive missing number from an array

def missing(a,n):
	test=[]
	dict={}
	for i in range(1,n):
		test.append(i)
	for j in test:
		if j not in a:
			return j		
	

def main():
	inp=[1,-1,2,3,5,-3,-2]
	k=max(inp)
	result=missing(inp,k)
	print(result)

if __name__=="__main__":
	main()

	
