class A:
    def m1(self):
        print("hi")
    def m2(self):
        print("hello")
class b(A):
    def m3(self):
        print("madam")
    def m4(self):
        print("how are you")
class c(b):
    def m5(self):
        print("kk")
    def m1(self):
        print("how hold you")
obj=c();
obj.m1()
    
