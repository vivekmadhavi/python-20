class Node:
	def __init__(self,data):
		self.data = data
		self.next = None

class SinglyLinkedList:
	def __init__(self):
		self.head = None

	def add(self, ele):
		if self.head == None:
			self.head = Node(ele)
			print("added")
		else:
			ptr = self.head
			while ptr.next != None:
				ptr = ptr.next
			ptr.next = Node(ele)
			print("added")
		
	def show(self):
		if self.head == None:
			print("EMPty linked list")
		else:
			print("head --> ", end="")
			ptr = self.head
			while ptr != None:
				print(ptr.data , end=" --> ")
				ptr = ptr.next
			print("Null")
s=SinglyLinkedList()
	

while True:
		op = int(input("1 add , 2 show and 3 exist"))
		if op == 1:
			ele = int(input("enter the element"))
			s.add(ele)
		elif op == 2:
			s.show()
		elif op == 3:
			break
		else:
			print("invalid option")