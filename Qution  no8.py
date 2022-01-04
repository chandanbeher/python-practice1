#8: Write a Python program to solve the Quadratic Equation
#Formula:
#ax2 + bx + c = 0, where
#a, b and c are real numbers and
#a ≠ 0
c=int(input("Enter a cgos: "))
r=int(input("Enter a revenue: ")) 
o=int(input("Enter a operating costs (oc)"))
print("gross profit")
x=int(r-c)
print((x))
print("net profit")
v=int(r-c-o)
print((v))
print("net profit percentage")
m=float((v/r)*100)

print((m))