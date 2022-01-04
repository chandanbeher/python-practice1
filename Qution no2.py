#2. Indus Bank accepts both short- and long-term deposits from its clients and offers an interest according to the scheme chosen.
#If the amount is left in the bank as a fixed deposit for a period of 7 years, the interest rate given by the bank is 7.5% per annum, and for any other scheme that is lesser than 7 years, the interest rate is 4.5% per annum. Mr.Ravi wants to deposit Rs.50,000 in either short term or long term scheme based on the returns.
#According to Mr.Ravi’s choice of the scheme, display the following details
#• Interest amount he will get per annum.
#• Interest amount he will for the entire term.
#Total Principal Amount + Interest for the entire term
amount=int(input("enter the amount="))
if time>=7:
    interest=(1*amount*7.5)/100
    print("interest for 1 years is",interest)
    interest=(time*amount*7.5)/100
    print("interest for ",time ," years is",interest)
else:
    interest=(1*amount*7.5)/100
    print("interest for 1 years is",interest)
    interest=(time*amount*4.5)/100
    print("interest for ",time ,"is",interest)
