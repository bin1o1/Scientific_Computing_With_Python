class Category:
    def __str__(self):
        string = ''
        string += self.category.center(30,'*')
        string += '\n'
        for item in self.ledger:
            string += f'{item['description'][:23]:23}'
            string += f'{item["amount"]:7.2f}'
            string += '\n'
        string += f'Total: {self.get_balance()}'
        return string

    def __init__(self, category):
        self.category = category
        self.ledger = []

    def check_funds(self, amount):
        if amount > sum(map(lambda dictionary: dictionary['amount'], (dictionary for dictionary in self.ledger))):
            return False
        return True

    def _deposit(self, amount, description):
        self.ledger.append({'amount':amount, 
                            'description':description})
    
    def deposit(self, amount, description = ''):
        self._deposit(amount, description)

    def withdraw(self, amount, description =''):
        if self.check_funds(amount):
            self._deposit(amount*-1,description)
            return True
        return False
    
    def get_balance(self):
        return sum(map(lambda dictionary: dictionary['amount'], (dictionary for dictionary in self.ledger))) 
    
    def transfer(self, amount, category):
        if self.check_funds(amount):
            self._deposit(amount*-1, f'Transfer to {category.category}')
            category.deposit(amount, f'Transfer from {self.category}')
            return True
        return False

food = Category('Food')
food.deposit(1000, 'deposit')
food.withdraw(10.15, 'groceries')
food.withdraw(15.89, 'restaurant and more food for dessert')
clothing = Category('Clothing')
food.transfer(50, clothing)
print(food)

list = [food, clothing]


def create_spend_chart(categories):
    withdrawn_amount = 0

    for category in categories:
        withdrawn_amount += sum(((dictionary["amount"] if dictionary["amount"]<0 else 0 for dictionary in category.ledger)))
    withdrawn_amount *= (-1)

    string = 'Percentage spent by category\n'
    percentage_list = []

    for category in categories:
        final_value = 0
        for dictionary in category.ledger:
            if dictionary['amount']<0:
                final_value += dictionary['amount']
        final_value *= -1
        percentage_list.append((final_value/withdrawn_amount)*100)

    for i in range(10):
        string += f'{100-i*10:3}' + '| '
        for j in range(len(categories)):
            if percentage_list[j]//(100-i*10) > 0:
                string += f'o  '
            else:
                string += '   '
        string += '\n'
    string += '  0| ' + 'o  '*len(categories)
    string += '\n    -' + '-'*3*len(categories)
    
    name_of_categories = [category.category for category in categories]
    max_length = max(len(name) for name in name_of_categories)
    for i in range(max_length):
        string += '\n     '
        for name in name_of_categories:
            if i < len(name):
                string += f'{name[i]}  '
            else:
                string += '   '
    print(string)

create_spend_chart(list)
