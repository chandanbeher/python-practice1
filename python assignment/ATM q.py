# ATM Operations:
#. 1. Display list of options to user: 1. Disposite 2. Withdraw 3. balEnquiry 0. EXIT
#. Methods: validate(), deposite(), withdraw(), balEnquir
    
class Atm:
    bal=10000
    total=0
    def validate(self):
        password=int(input("enter the password"))
        if password==1432:
            print("password validate")
            print('''press 0,1,2,3 for below options.
            0.exit
            1.deposite
            2.with draw
            3.balancewnquiry
            ''')
            a=int(input())
            if a==1:
                b=int(input("enter the deposite amount"))
                self.bal=self.bal+b
                print("remaining amount",self.bal)
            elif a==2:
                c=int(input("enter the withdraw amount"))
                self.bal=self.bal-c
                print("remaining amount",self.bal)
            elif a==3:
                print("balance",self.bal)
            else:
                print("exit")
        else:
            print("password is invalid")
                
obj=Atm()
obj.validate()