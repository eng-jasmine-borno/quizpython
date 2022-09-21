price = float(input("Enter the price of your item:"))
discountRate = int(input("Enter the percentage discount:"))
discount = float(price * (discountRate/ 100))
discountedPrice = price - discount
print("price before discount = €" , price)
print("discount Rate =%" ,discountRate)
print("discount = €" ,discount)
print( "price after discount = €",discountedPrice)