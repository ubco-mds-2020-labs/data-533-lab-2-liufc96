## Package: MENU Demonstration
<br/>

### - combo subpackage:
<br/>This package is used for help user customizing their own combo when going to Mcdonald's, which contains two module.

1. `regularcombo` module
<br/>This module contains a class: `Regularcombo`, which is used for ordering regular combo(includes a big mac as default burger, fries as default snack and coca as default drink)if user does not enter what specific burger, snack or drink that they want.
<br/> - Class: `Regularcombo` contains 5 functions
<br/> - `burger_custom()`: enable user customize their own burger, such as double meat, add lettuce or add extra salad sauce
<br/> - `snack_custom()`: enable user customize their own snack, such as add one more portion of nuggets or chickenfingers
<br/> - `drink_custom()`: enable user customize their own drink, such as with ice or no ice
<br/> - `display()`: display user's customized combo
<br/> - `total_price()`: calculate user's total combo price

2. `dietcombo` module
<br/>This module contains a class: `Dietcombo`, which inherits from Regularcombo 
<br/> - Class: `Dietcombo` contains 3 functions, this class does not allow user to customize their burger and drink, in order to control the calories intake
<br/> - `calories_check()`: check the user's intake calories, for burger, the calories is 200, for each piece of snack, the calories is 100, if user request a specific drink that does not contain "diet", the drink calories should be calculated as 50, the total calories are added together of all three parts. If total calories is larger than 500, the function will return a warning to user that calories is higher than standard.
<br/> - `drink_check()`: check whether user's drink is diet, if not, return a warning to user that drink is not diet.
<br/> - `burger_cal_control()`: check whether user's burger is regular(only one entry allowed), if not, return a warning and change burger back to regular one
<br/>

### - freeorder subpackage:
<br/>Modules are designed to take free orders for both adults and kids; to make your order as a meal, please check out the `combo` subpackage.

1. `regularorder` module
<br/>!!!`pip install tabulate` required before using this module
<br/>This module contains a class(): `regularorder`, which contains 6 functions
<br/> - Class: `regularorder` contains 6 functions, it allow users order food they want
<br/> - `burger()`: Take burger or wrap order
<br/> - `beverage()`: Take beverage order
<br/> - `snack()`: Take snack and dessert order
<br/> - `review_order()`: Review your order details and checkout
<br/> - `menu()`: To view our regular menu
<br/> - `next_customer()`: Clear the order history and ready to take next customer in line

2. `kidsmeal` module
<br/>This module contains a class(): `kidsmeal`, which inherits from regularorder, it allow user select gift for kid and order food for kid, but 4 more food will trigger a warning when review the order
<br/> - Class: `kidsmeal` contains 3 functions, it allow users order children's food and set gift they want
<br/> - Methods inherited from class in regularorder module: Take burger or wrap order; Take beverage order; Take snack order; Clear the order history and ready to take next customer in line
<br/> - `setGift(Book/Toy)`: Select Book or Toy as a gift with the kids meal
<br/> - `menu()`: To view our special kids menu
<br/> - `review_order()`: make sure no more than 4 items selected per kids meal Review your order details and checkout
