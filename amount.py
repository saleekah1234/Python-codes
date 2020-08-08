def totalamt(p,q,n):
	amount=0
	for i in range(1,n):
		m=p[i]*q[i]
		amount=amount+m
	print(amount)


def main():
	t=["a","b","c","d"]
	p=[2,3,4,1]
	q=[2,1,3,2]
	n=len(p)
	totalamt(p,q,n)

if __name__=="__main__":
	main()
