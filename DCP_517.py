class Node:
	def __init__(self, data = None):
		self.data = data
		self.next = None

class SLinkedList:
	def __init__(self):
		self.head = None
		
	def listprint(self):
		printval = self.head
		while printval is not None:
			print (printval.data)
			printval = printval.next

def length(head):
	if not head:
		return 0
	return 1 + length(head.next)

def intersection(a, b):
	m, n = length(a), length(b)
	cur_a, cur_b = a, b
	if m > n:
		for _ in range(m - n):
			cur_a = cur_a.next
	else:
		for _ in range(n - m):
			cur_b = cur_b.next

	while cur_a.data != cur_b.data:
		cur_a = cur_a.next
		cur_b = cur_b.next
	return cur_a.data

list1 = SLinkedList()
list1.head = Node(4)
e2 = Node(3)
e3 = Node(2)
e4 = Node(1)
e5 = Node(0)
list1.head.next = e2
e2.next = e3
e3.next = e4
e4.next = e5

list2 = SLinkedList()
list2.head = Node(0)
n2 = Node(1)
n3 = Node(2)
n4 = Node(3)
n5 = Node(4)
list2.head.next = n2 
n2.next = n3
n3.next = n4
n4.next = n5

list1.listprint()
list2.listprint()

answer = intersection(list1.head, list2.head)
print("The value of node of intersection!")
print(answer)
