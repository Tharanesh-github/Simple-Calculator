# importing the necessary libraries
from tkinter import Tk, Entry, Button, StringVar


# class for handling the logic of the calculator
class CalculatorLogic:
    # Initializes the class with an empty string entry_value to store the calculator's current input
    def __init__(self):
        self.entry_value = ''

    # Adds the given value to the current expression
    def add_to_expression(self, value):
        # Convert 'x' to '*' for multiplication
        if value == 'x':
            value = '*'
        self.entry_value += str(value)

    # Resets the entry_value to an empty string
    def clear(self):
        self.entry_value = ''

    # Evaluates the current expression using eval and returns the result as a string. If an error occurs, it returns
    # "Error"
    def evaluate(self):
        try:
            # Using eval is risky, ideally replace with a proper parser in production code
            return str(eval(self.entry_value))
        except Exception:
            return "Error"


# Class that handles the Graphical User Interface(GUI) of the calculator
class CalculatorGUI:
    def __init__(self, master, logic):
        self.logic = logic

        # Sets the title, size, background color, and resizable property of the main window
        master.title("Calculator")
        master.geometry('357x420+0+0')
        master.config(bg='gray')
        master.resizable(False, False)

        self.equation = StringVar()
        Entry(width=17, bg='#ccddff', font=('Arial Bold', 28), textvariable=self.equation).place(x=0, y=0)

        # A list of tuples representing the buttons' text and their positions
        buttons = [
            ('(', 0, 50), (')', 90, 50), ('%', 180, 50),
            ('1', 0, 125), ('2', 90, 125), ('3', 180, 125),
            ('4', 0, 200), ('5', 90, 200), ('6', 180, 200),
            ('7', 0, 275), ('8', 180, 275), ('9', 90, 275),
            ('0', 90, 350), ('.', 180, 350), ('+', 270, 275),
            ('-', 270, 200), ('/', 270, 50), ('x', 270, 125),
            ('=', 270, 350), ('C', 0, 350)
        ]

        # Creates buttons based on the list. The command parameter specifies the function to call when the button is
        # pressed
        for (text, x, y) in buttons:
            if text == '=':
                Button(width=11, height=4, text=text, relief='flat', bg='lightblue', command=self.solve).place(x=x, y=y)
            elif text == 'C':
                Button(width=11, height=4, text=text, relief='flat', command=self.clear).place(x=x, y=y)
            else:
                Button(width=11, height=4, text=text, relief='flat', bg='white',
                       command=lambda t=text: self.show(t)).place(x=x, y=y)

    def show(self, value):
        self.logic.add_to_expression(value)
        self.equation.set(self.logic.entry_value)

    def clear(self):
        self.logic.clear()
        self.equation.set(self.logic.entry_value)

    def solve(self):
        result = self.logic.evaluate()
        self.equation.set(result)


root = Tk()
logic = CalculatorLogic()
gui = CalculatorGUI(root, logic)
root.mainloop()
