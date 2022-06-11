from Classes_and_Functions import Expense
from Classes_and_Functions import get_expense_data

data = get_expense_data()
expense = Expense(data[0], data[1], data[2])
print(expense)