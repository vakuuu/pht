# PTH 2013 - Joona Nissinen

class Linkkilista:
	'''Linkkilista class'''

	class __Node:
		'''privaatti node objekti. Node osoittaa aina seuraavaan objektiin lista rakenteessa.'''
		def __init__(self,element=None):
			self.element = element
			self.next = None

		def __str__(self):
			'''Node:n merkkijonoksi vaihto'''
			return str(self.element)

		def onkoSeuraava(self):
			'''palauttaa true arvon, mikäli Node ei saa arvokseen Nonea'''
			return self.next != None

		def getSeuraava(self):
			'''get seuraava Node'''
			return self.next

		def getElementti(self):
			'''get kyseisen Noden elementti'''
			return self.element

		def setSeuraava(self, nextItem):
			'''set seuraava Node'''
			self.next = nextItem

		def setElement(self, element):
			'''set nykyisen Noden elementti'''
			self.element = element

		

