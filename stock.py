def spancalc(st):
	span=[]
	stack=[]
	temp=[]
	count=1
	top=-1
	first=0
	for i in st:
		top=top+1
		stack.append(i)
	while(top!=-1):
		var=stack.pop()
		top=top-1
		while(top!=-1 and var>stack[top]):
			temp.append(stack.pop())
			top=top-1
			count=count+1
		span.append(count)
		count=1
		if(len(temp)!=0):
			for i in range(0,len(temp)):
				stack.append(temp.pop())
				top=top+1
		temp.clear()
		
	print(span[::-1])
	
		



def main():
	stock=[10,4,5,90,120,80]
	spancalc(stock)
if __name__=="__main__":
	main()
