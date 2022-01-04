#3. Mr.Kumar went to purchase stationary items for his office. He asked the shopkeeper for a discount. The shopkeeper said that if he purchases more than 200 quantity of the item, then a discount of 20% can be applied on the total bill amount, excluding the GST.
#Get the Quantity and price per item as an input and calculate and tell whether Mr.Kumar is eligible for the discount and what would be the net amount he has to pay after the discount.
#Take the GST at 18%.
#Net Amount = Total bill amount after discount + GST
Quantity=int(input("enter the requried quantity:"))
Price=int(input("Price pe unit is:"))
if (Quantity>200):
    total=Price*Quantity*0.20
else:
    total=Price*Quantity
gst=total*0.18
finalmount=total+gst
print(finalamount)
    