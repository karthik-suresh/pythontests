class A:
	def fn1(self):
		self.var1=5
		print ("m1")
class B(A):
	def fn2(self):
		super().fn1()
		print(self.var1)


x = B()
x.fn2()
