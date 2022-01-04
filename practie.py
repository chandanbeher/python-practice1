class A:
    def __init__(self):
        self.a=30
        self.n=0
        self.n1=1
    def m1(self):
        print(self.n,self.n1,end=" ")
        for i in range(self.a):
            self.n2=self.n+self.n1
            print(self.n2,end=" ")
            self.n=self.n1
            self.n1=self.n2
obj=A();
obj.m1()