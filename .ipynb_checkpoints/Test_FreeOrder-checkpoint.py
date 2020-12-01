# Need to install this package "tabulate" first to show correct contents in Package "menu"
#!pip install tabulate

##### To Order Regular Meal
from menu.freeorder import regularorder 
o = regularorder.regularorder()

# Check out our menu
o.menu()

# Order 1
o.burger(1)
o.burger(3)
o.beverage(8)
o.beverage(10)
o.snack(17)
o.snack(18)

# Review your order
o.review_order()

# Ready to take the next customer
o.next_customer()

## Order 2
o.snack(17)
o.review_order()
o.next_customer()
    
    
    
##### To Order Kids Meal
from menu.freeorder import kidsmeal
k = kidsmeal.kidsmeal()

# Check out our special kids meal menu
# make sure you choose no more than 4 items for each kids meal
k.menu()

# Order 1
k.burger(22)
k.beverage(26)
k.snack(32)

# Choose Toy or Book for your kids meal
k.setGift("Toy")

# Review your order
k.review_order()

# Ready to take the next customer
k.next_customer()

# Order 2
k.burger(25)
k.beverage(28)
k.snack(31)
k.setGift("Book")
k.review_order()
k.next_customer()

## Order 3
k.burger(24)
k.beverage(27)
k.beverage(29)
k.snack(30)
k.snack(33)
k.setGift("Toy")
k.review_order()
k.next_customer()