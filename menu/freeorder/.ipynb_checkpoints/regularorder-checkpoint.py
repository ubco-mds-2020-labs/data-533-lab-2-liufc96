from tabulate import tabulate

regular = {'Big Mac': 5.3,'Cheese Burger' : 4.2,'Mighty Angus':3.2,'Chrispy Chicken Wrap':5.3,
           'Grilled Chicken Wrap':3.2,'Carsar McWrap':2.1, 'Chicken & Bacon McWrap':1.9,
           'Coke':1.2,'Diet Coke':1.2,'Ice Tea':1.1, 'Every Flavor Smoothie':2.1,'McCafe':2.2, 'Hot Chocolate':1.2,'Water':1,
           'Poutine':3.2,'Chicken Nuggest':2.1, 'Fries':2.1,'Muffin':2.2,'Brownie Cookie':2.1, 'Apple Pie':2.1,'McFlurry':2.1, 
           'Cheeseburger':2.2,'Hamburger':2.3, 'Kids Chrispy Chicken Wrap':2.4, 'Kids Grilled Chicken Wrap':2.5,
           'Milk':1.1,'Orange Juice':1.2,'Pineapple Smoothie':1.3, 'Every Flavor Yoghurt':1.4,
           'Apple Slice':1.5,'Kids Chicken Nuggest':1.6,'Mini Fry':1.7,'Carrot Muffin':1.8 }
 
item = list(regular)
values = list(regular.values())

class regularorder:
   
    def __init__(self, order=[], price=0):
        self.order = list(order)
        self.price = price
        print("Welcome!\n")
    
    def burger(self, order):
        self.order.append(item[order-1])
        self.price += values[order-1]
        
    def beverage(self, order):
        self.order.append(item[order-1]) 
        self.price += values[order-1]
        
    def snack(self, order):
        self.order.append(item[order-1])  
        self.price += values[order-1]
        
    def review_order(self):
        return print('Your Orders: \n{}'.format(self.order),'\n\n   Price: {}\n'.format(round(self.price,2)),
                     'GST(5%): {}\n'.format(round(self.price*0.05,2)),
                     'PST(7%): {}\n'.format(round(self.price*0.07,2)),
                     '  Total: {}\n'.format(round(self.price*1.12,2)),)
    
    def menu(self):
        print(tabulate([['1. Big Mac', '8. Coke', '15. Poutine'], 
                        ['2. Cheese Burger', '9. Diet Coke','16. Chicken Nuggest'],
                        ['3. Mighty Angus', '10. Ice Tea','17. Fries'],                   
                        ['4. Chrispy Chicken Wrap', '11. Every Flavor Smoothie','18. Muffin'],
                        ['5. Grilled Chicken Wrap', '12. McCafe','19. Brownie Cookie'], 
                        ['6. Carsar McWrap', '13. Hot Chocolate','20. Apple Pie'],
                        ['7. Chicken & Bacon McWrap', '14. Water','21. McFlurry']],
                        headers=['Burger & Wrap', 'Beverage','Snack & Dessert']), "\n")

        
    def next_customer(self):
        self.order.clear()
        self.price = 0