def diff(a,b):
	print(a-b)

def positive(func):
	def pos(a,b):
		if(a<b):
			a,b=b,a
		return func(a,b)
	return pos
def main():
	a=int(input("enter no"))
	b=int(input("enter no"))
	x=positive(diff)
	x(a,b)

if __name__=="__main__":
	main()
