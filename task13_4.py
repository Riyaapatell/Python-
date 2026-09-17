# E-cart system
products = [
    ("Laptop",50000),
    ("Ipad",80000),
    ("Watch",10000),
    ("Phone",60000)
]
print("---Products---")
for i,product in enumerate(products):
     print(product[0],":",product[1])
print("---Cart---")
display = [
     ("Add product"),
     ("View Cart"),
     ("Remove product"),
     ("Bill"),
     ("Exit")
]
cart = []
for i, dis in enumerate(display,1):
     print(i,dis)
choice = input("Enter your choice: ")
if choice == "1":
     cart1 = input("Enter product to add in cart: ")
     for product in products:
        if cart1.lower() == product[0].lower():
            cart.append(product)
        else:
            print("Enter valid product")
        

