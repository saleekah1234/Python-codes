def cycleornot(self,head):
	head=self.head
	p1=self.head
	p2=self.head
	p2=p2.next.next
	while(p1!=p2):
		p1=p1.next
		p2=p2.next.next
		if(p1==p2):
			print("cycle detected")
	
		
