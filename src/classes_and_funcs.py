from datetime import date

TAGS = ['grocery', 'entertainment', 'wants']

class Expense:
    """
    An expense will need to follow suit with the characterstics in this class

    Instance Variables:
        name (string)
        date 
        tag (string)
        amount (float)

    Functions:
        edit
    """

    def __init__(self, name, tag, amount):
        self.name = name
        self.date = date.today()
        self.tag = tag
        self.amount = amount

    def __str__(self):
        return str("${0:.2f} was spent on {1} for {2} and was placed under the category of {3}.".format(self.amount, self.date, self.name, self.tag))
    

# function to obtain values needed to create an expense object
def get_expense_data():
    print("Please input the name of the expense.")
    name = input()

    tag = None
    while tag == None:
        try:
            print("Please select what category this expense falls under. (type the number of the category in the list below)")
            for count, tag in enumerate(TAGS):
                print("{}. {}".format(count, tag))
            tag = TAGS[int(input())]
        except ValueError:
            print("Input a valid number from the list above. Try again.")

    amount = None
    while amount == None:
        try:
            print("How much was the expense?")
            amount = float(input())
        except ValueError:
            print("Please enter a valid number. Try again")

    data = [name, tag, amount]
    return data