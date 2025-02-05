def add_expense(expenses, amount, category):
      expenses.append({'amount': amount, 'category': category})

def print_expenses(expenses):
      for expense in expenses:
            print(f"Amount: {expense['amount']}, Category: {expense['category']}")

def total_expenses(expenses):
      lambda expense: expense['amount']
      return(sum(map(lambda expense: expense['amount'], expenses)))

def filter_expenses_by_category(expenses, category):
      lambda expense: expense['category'] == category
      return (filter(lambda expense: expense['category'] == category, expenses))

def main():
      expense = []
      while True:
            print('\nExpense tracker')
            print('1. Add an expense')
            print('2. List all expenses')
            print('3. Show total expenses')
            print('4. Filter expenses by category')
            print('5. Exit')

            choice = input('Enter your choice: ')
            if choice == '1':
                  amount = float(input('Enter amount: '))
                  category = input('Enter category: ')
                  add_expense(expense, amount, category)
            elif choice == '2':
                  print_expenses(expense)
            elif choice == '3':
                  print(f'Total expenses: {total_expenses(expense)}')
            elif choice == '4':
                  category = input('Enter category: ')
                  expenses = filter_expenses_by_category(expense, category)
                  print_expenses(list(expenses))
            elif choice == '5':
                  break
            else:
                  print('Invalid choice')

      
#test = lambda x: x * 2
#map(test, [2, 3, 5, 8])
#print(list(map(test, [2, 3, 5, 8])))