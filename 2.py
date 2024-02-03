class Tree:
	def __init__(self,data):
		self.data = data
		self.left = None
		self.right = None

	def add(self, ele):
		if ele < self.data:
			if self.left == None:
				self.left = Tree(ele)
				print("added")

			else:
				self.left.add(ele)
		if ele >= self.data:
			if self.right == None:
				self.right = Tree(ele)
				print("added")

			else:
				self.right.add(ele)

	def show(self):
		if self.left != None:
			self.left.show()
		print(self.data)
		if self.right != None:
			self.right.show()

root = None

while True:
	op = int(input("1 add , 2 show and 3 exit "))
	if op == 1:
		ele = int(input("enter the element"))
		if root == None:
			root = Tree(ele)
			print("added")
		else:
			root.add(ele)
	elif op == 2:
		if root == None:
			print("empty")
		else:
			root.show()
	elif op == 3:
		break

	else:
		print("invalid")




