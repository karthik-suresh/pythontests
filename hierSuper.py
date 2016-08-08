class A:
	def fn2(self):
		self.var1=5
		print ("m1")
class C(A):
	def fn2(self):
		super().fn2()
		print("m2")
class B(C):
	def fn2(self):
		super().fn2()
		print(self.var1)


x = B()
x.fn2()
