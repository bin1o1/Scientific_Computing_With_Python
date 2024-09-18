'''Nothing crazy going on here, just manipulating a list containing bunch of dictionaries which describe an expense.
Filtering is done by categories. Lambda function is used.'''

def add_expense(expenses, amount, category):        #adds a dictionary
    expenses.append({'amount': amount, 'category': category})
    
def print_expenses(expenses):       #prints all the dictionaries
    for expense in expenses:
        print(f'Amount: {expense["amount"]}, Category: {expense["category"]}')
    
def total_expenses(expenses):
    return sum(map(lambda expense: expense['amount'], expenses))        #here, lambda function takes the dictionary 'expense' and then returns the value for 'amount' key within that dictionary.
                                                                        #when given as an argument to map function along with 'expenses' list, the lambda function operates on every item in the
                                                                        #expenses list. the map fucntion returns an iterable map object with values which are a result of that function.
                                                                        # sum adds all the values in that object, which is finally returned. 
    
def filter_expenses_by_category(expenses, category):
    return filter(lambda expense: expense['category'] == category, expenses)
    

def main():
    expenses = []
    while True:
        print('\nExpense Tracker')
        print('1. Add an expense')
        print('2. List all expenses')
        print('3. Show total expenses')
        print('4. Filter expenses by category')
        print('5. Exit')
       
        choice = input('Enter your choice: ')

        if choice == '1':
            amount = float(input('Enter amount: '))
            category = input('Enter category: ')
            add_expense(expenses, amount, category)

        elif choice == '2':
            print('\nAll Expenses:')
            print_expenses(expenses)
    
        elif choice == '3':
            print('\nTotal Expenses: ', total_expenses(expenses))
    
        elif choice == '4':
            category = input('Enter category to filter: ')
            print(f'\nExpenses for {category}:')
            expenses_from_category = filter_expenses_by_category(expenses, category)
            print_expenses(expenses_from_category)
    
        elif choice == '5':
            print('Exiting the program.')
            break

main()