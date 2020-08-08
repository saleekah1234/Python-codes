def binarypal(n):
	binary=bin(n)
	print(binary)
	rev=binary[::-1]
	print(rev)
	if(binary==rev):
		print("palindrome")
	else:
		print("not palin")

def main():
	ip=int(input("entet the num \t"))
	binarypal(ip)

if __name__=="__main__":
	main()
