def missing(a,n):
	test=[]
	dict={}
	for i in range(1,n):
		test.append(i)
	for j in test:
		if j not in a:
			missed=j
	for i in a:
		counter=a.count(i)
		if counter>1:
			repeat=i	
			
	print("The missed number is",missed)
	print("The repeated number is", repeat)
def main():
	inp=[1,2,4,3,6,7,6]
	k=max(inp)
	missing(inp,k)
	

if __name__=="__main__":
	main()
