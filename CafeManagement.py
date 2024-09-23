menu={
    "pizza":100,
    "Burger":150,
    "Chinese":80,
    "Coffee":50,
    "Salad":40
    
}

# print(menu)
print("Welcome to Prasanna's Cafe \n Please Select what you want to order")
print(" pizza: 100 Rs \n Burger: 150 Rs \n Chinese: 80 Rs \n Coffee: 50 Rs \n Salad: 40 Rs")

total_amount=0

first_item=(input("Enter the item which you want to order: "))
if first_item in menu:
    total_amount += menu[first_item]
    print(f"Your item {first_item} is added in order ")
else:
    print("please enter the item which shows in menu")


another_item=(input("Do you want to add another item? (Yes/No): "))
if another_item == "Yes" or "yes":
    second_item=input("Enter the item which you want to order: ")
    if second_item in menu:
        total_amount += menu[second_item]
        print(f"Your item {second_item} is added in order ")
    else:
          print("please enter the item which shows in menu")
elif another_item == "no" or "No":
    print("your final item cost is below")
    
    
     

print(f"Your total item cost is {total_amount}")
    
