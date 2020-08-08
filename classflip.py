class flipkart():
	def __init__(self,t,p,q,n):
		self.t=t
		self.p=p
		self.q=q
		self.n=n
	def totalamt(self):
		amount=0
		for i in range(0,self.n):
			m=self.p[i]*self.q[i]
			amount=amount+m
		print(amount)

s=flipkart(["A","B"],[2,1],[2,3],2)
s.totalamt()

