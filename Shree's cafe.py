menu = {
    'Cake': 150,
    'Pizza':100,
    'Burger':80,
    'Dosa': 50,
    'Chowmin': 100,
    'Veg roll': 90,
    'Pasta': 100

}
#greet
print("WELCOME TO SHREE'S CAFE")
print(" Cake: Rs 150\n Pizza: Rs 100\n Burger: Rs 80\n Dosa: Rs 50\n Chowmin: 100\n Veg roll: Rs 90\n Pasta: Rs 100")

order_total = 0

item_1= input("enter the name of item you want to order:")
if item_1 in menu:
    order_total += menu[item_1]
    print(f"your order{item_1} has been added to the cart")

else:
    print(f"Sorry,the item {item_1} is not available")  


another_order = input("Would you like to order anything else? (Yes/No)")
if another_order =="Yes":
    item_2 = input("Select your second order: ")
    if item_2 in menu:
        order_total += menu[item_2]
        print(f"Item {item_2}has been added to the cart")

    else:
         print(f"Sorry,the item {item_2} is not available") 


print(f"The total amount to pay is{order_total}")