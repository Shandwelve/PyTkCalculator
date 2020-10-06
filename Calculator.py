from tkinter import *


class Calculator:
    window = Tk()

    buttons = []

    display = None

    buttons_template = [
        [
            '7', '8', '9', '/'
        ],
        [
            '4', '5', '6', '*'
        ],
        [
            '1', '2', '3', '-'
        ],
        [
            '0', '00', '%', '+'
        ],
        [
            'C', 'AC', '.', '='
        ]
    ]

    def __init__(self):
        self.window.geometry('600x600')
        self.window['background'] = 'black'
        self.window.title('Py Calculator')
        self.window.iconbitmap('calculator-icon.ico')
        self.make_calculator_template()

    def make_calculator_template(self):
        self.display = Label(self.window, width=50, height=2, font='Arial 35', borderwidth=0, bg='black', fg='white',
                             anchor='e')
        self.display.grid(column=0, row=0, columnspan=4)

        for i in range(len(self.buttons_template)):
            self.window.columnconfigure(i, weight=1)
            self.window.rowconfigure(i, weight=1)
            for j in range(len(self.buttons_template[i])):
                self.buttons.append(
                    Button(self.window, text=self.buttons_template[i][j], bg='black', fg='white', width=32, height=3,
                           borderwidth=0, font='Arial 20',
                           command=lambda row=i, column=j: self.calculate(str(self.buttons_template[row][column]))))
                self.buttons[-1].grid(column=j, row=i + 2)
                self.buttons[-1].bind("<Enter>", self.on_enter)
                self.buttons[-1].bind("<Leave>", self.on_leave)

    def on_enter(self, event):
        event.widget.configure(fg="cyan")

    def on_leave(self, event):
        event.widget.configure(fg="white")

    def calculate(self, button_value):
        if self.validate(button_value):
            if button_value == 'AC':
                self.clear_display()
            elif button_value == 'C':
                self.delete_last()
            elif button_value == '=':
                self.solve()
            else:
                self.add_on_display(button_value)

    def validate(self, button_value):
        operators = ['%', '/', '*', '+', '-']
        if self.display['text'] == 'Cannot divide by zero':
            self.clear_display()
        if button_value == '.' and self.display['text'].find('.') != -1:
            return 0
        if (button_value in operators or button_value == '.') and len(self.display.cget('text')) == 0:
            return 0
        if button_value in operators and self.display['text'][-1] in operators:
            self.display.configure(text=self.display['text'][:-1] + button_value)
            return 0
        if button_value == '.' and self.display['text'][-1] in operators:
            return 0
        if button_value in operators and self.display['text'][-1] == '.':
            return 0
        if button_value == '00' and (self.display['text'] == '0' or len(self.display.cget('text')) == 0 or
                                     self.display['text'][-1] in operators):
            return 0
        if button_value == '0' and self.display['text'] == '0':
            return 0
        return 1

    def clear_display(self):
        self.display.configure(text='')

    def delete_last(self):
        if len(self.display.cget('text')) == 0:
            self.clear_display()
        else:
            self.display.configure(text=self.display['text'][:-1])

    def solve(self):
        if self.display['text'][-1] in ['%', '/', '*', '+', '-']:
            self.display.configure(text=self.display['text'][:-1])
        try:
            result = str(eval(self.display.cget('text')))
        except ZeroDivisionError:
            result = 'Cannot divide by zero'
        self.display.configure(text=result)

    def add_on_display(self, button_value):
        self.display.configure(text=self.display['text'] + button_value)

    def run(self):
        self.window.mainloop()
