from menu.freeorder.regularorder import regularorder
from tabulate import tabulate

class kidsmeal(regularorder):
    def __init__(self, order=[], gift='Book'):
        regularorder.__init__(self,order = [])
        self.gift = gift
        print("Please choose [Book] or [Toy] for this kids meal and no more than 4 items for the order!\n")
         
    def setGift(self,gift):
        self.gift = gift
        
    def menu(self):
          print(tabulate([['22. Cheeseburger', '26. Milk', '30. Apple Slice'], 
                          ['23. Hamburger', '27. Orange Juice','31. Chicken Nuggest'],
                          ['24. Chrispy Chicken Wrap', '28. Pineapple Smoothie','32. Mini Fry'],
                          ['25. Grilled Chicken Wrap', '29. Every Flavor Yoghurt','33. Carrot Muffin']], 
                          headers=['Burger & Wrap', 'Beverage','Snack']), "\n")
                 
        
    def review_order(self):
        if len(self.order) == 0:
            print("Please choose [Book] or [Toy] for this kids meal and no more than 4 items for the order!\n")
            
        elif len(self.order) > 4:
            print("Please review your order and make sure no more than 4 items selected for this kids meal, thank you!")
        else:
            regularorder.review_order(self)
            print('Gift [{}]'.format(self.gift))