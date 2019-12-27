class Fracao():
	def __init__(self, n,d):  # inicializa o numerador e denominador
		try:
			if d != 0:
				self.n = n
				self.d = d
			else:
				raise Exception
		except Exception:
			print('zero nao')

	def __add__(self, other): # sobrescreve +
		d = self.d * other.d
		n = self.n * other.d + other.n * self.d
		return Fracao(n,d)

	def __iadd__(self, other): # sobrescreve +=
		d = self.d * other.d
		n = self.n * other.d + other.n * self.d
		return Fracao(d, n)

	def __mul__(self, other): # sobrescreve *
		n = self.n * other.n
		d = self.d * other.d
		return Fracao(n,d)

	def __sub__(self, other): # sobrescreve - 
		d = self.d * other.d
		n = self.n * other.d - other.n * self.d
		return Fracao(n,d)

	def __div__(self, other): # sobrescreve /
		pass
	
	def __eq__(self, other): # sobrescreve ==, simplifica frações antes de comparar
		pass
	




a = Fracao(2,3)
print(a.n, a.d)

b = Fracao(3,2)
print(b.n, b.d)

#c = a*b
#c = a+b
#c = a-b
#a += Fracao(1,3)
#c = a/b
#c = a == b

#print(a.n, a.d)
#print(c.n, c.d)

