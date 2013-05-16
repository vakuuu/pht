# PHT 2013 - Linkkilista
# UEF TKT
# Joona Nissinen
# python 3


class Node:
	def __init__(self, uid, nimi, vakiLuku, pvm):
		self.pvm = pvm
		self.vakiLuku = vakiLuku
		self.nimi = nimi
		self.uid = uid
		self.next = None


class LinkitettyLista:
	def __init__(self):
		self.head = None
		self.tail = None

	def addNode(self, uid, nimi, vakiLuku, pvm):
		new_node = Node(uid, nimi, vakiLuku, pvm)

		if self.head == None:
			self.head = new_node

		if self.tail != None:
			self.tail.next = new_node

		self.tail = new_node


	def removeNode(self, index):
		prev = None
		node = self.head
		i = 0

		while (node != None) and (i < index):
			prev = node
			node = node.next
			i += 1

		if prev == None:
			self.head = node.next
		else:
			prev.next = node.next


	def printList(self):
		node = self.head
		while node != None:
			print (node.uid, node.nimi, node.vakiLuku, node.pvm)
			node = node.next

	def saveTxtFile(self):
		node = self.head
		while node != None:
			open("LinkitettyLista.txt", "a").write(str(node.uid) + " " + node.nimi + " " + str(node.vakiLuku) + " " + node.pvm + "\n")
			node = node.next

	def saveBinFile(self):
		node = self.head
		while node != None:
			#prkl = str(node.uid).encode("utf-8")
			#prkl1 = str(node.vakiLuku).encode("utf-8")
			open("LinkitettyLista.bin", "ab").write(b'node.uid + " " + node.nimi + " " + node.vakiLuku + " " + node.pvm + "\n"')
			node = node.next

	def searchList(self, index):
		node = self.head
		if node.uid == index:
			print ("Node Löytyi: " + str(node.uid), node.nimi, str(node.vakiLuku), node.pvm)
		else:
			node = node.next
		print ("Nodea ei löytyny")

	def readTxtFile(self):
		pass

	def readBinFile(self):
		pass




class Gui:
	def main():
		List = LinkitettyLista()
		List.addNode(1, "tampere", 1000, "10-10-2013")
		List.addNode(2, "kuopio", 123, "12-05-2013")
		List.addNode(3, "oulu", 101, "01-01-2013")
		List.printList()
		List.removeNode(1)
		List.printList()
		List.saveTxtFile()
		print ("\n\n")
		List.printList()
		List.saveBinFile()
		List.searchList(1)
		List.searchList(8)

	main()
