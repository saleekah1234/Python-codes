def palindrome(str):
	x=str[::-1]
	if(str==x):
		print("The string is palindrome")
	else:
		print("The string is not palindrome")

def main():
	str=input("enter the string::")
	palindrome(str)
if __name__=="__main__":
	main()
