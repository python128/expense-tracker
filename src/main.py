import tkinter
import customtkinter

from classes_and_funcs import Expense, get_expense_data, TAGS

# Global Variables
expenses = []

customtkinter.set_appearance_mode("dark")  # Modes: "System" (standard), "Dark", "Light"
customtkinter.set_default_color_theme("blue")  # Themes: "blue" (standard), "green", "dark-blue"

app = customtkinter.CTk()
app.geometry("400x580")
app.title("CustomTkinter simple_example.py")

# Function for clearing text inside of an entry widget
def clearText(entryWidget):
    entryWidget.delete(0,tkinter.END)

# Function that activates when hitting submit button for new expenses
def submitExpense():
    global expenses

    print("Expense Submitted")
    name = nameEntry.get()
    tag = TAGS[radiobutton_var.get()]
    try:
        price = float(priceEntry.get())
        expense = Expense(name, tag, price)
        expenses.append(expense)
        clearText(nameEntry)
        clearText(priceEntry)
        for expense in expenses:
            print(expense)
    except ValueError:
        print("Please input a valid amount.")
        clearText(priceEntry)
        name = None
        tag = None

# gui set up for a basic new expense
frame_1 = customtkinter.CTkFrame(master=app)
frame_1.pack(pady=20, padx=60, fill="both", expand=True)

expenseTitle = customtkinter.CTkLabel(master=frame_1, justify=tkinter.LEFT, text="New Expense")
expenseTitle.pack(pady=12, padx=10)

nameEntry = customtkinter.CTkEntry(master=frame_1, placeholder_text="Expense Name")
nameEntry.pack(pady=12, padx=10)

priceEntry = customtkinter.CTkEntry(master=frame_1, placeholder_text="Cost")
priceEntry.pack(pady=12, padx=10)

radiobutton_var = tkinter.IntVar(value=1)

for i, tag in enumerate(TAGS):
    radioButton = customtkinter.CTkRadioButton(master=frame_1, variable=radiobutton_var, value=i, text=tag)
    radioButton.pack(pady=12, padx=10)

submitButton = customtkinter.CTkButton(master=frame_1, command=submitExpense, text="Submit")
submitButton.pack(pady=12, padx=10)


# gui mainloop
app.mainloop()