def div(str):
	print(str)

def smart_div(func):
	def inner(str):
		str= str +"\t"+"hello"+"\t"+"how are you"
		return func(str)
	return inner
def main():
	str=input("enter string::")
	div1=smart_div(div)
	div1(str)
if __name__=="__main__":
	main()
