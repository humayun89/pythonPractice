# Determine the Price of a product  after the discount :
price=float(input("Enter the price of a product :"))
if price <=500:
    discount = 20
    discounted_price = float(price - (price * (discount / 100)))
    print(discounted_price)
elif price <=1000:
    discount = 25
    discounted_price = float(price - (price * (discount / 100)))
    print(discounted_price)
else:
    discount = 30
    discounted_price = float(price - (price * (discount / 100)))
    print(discounted_price)