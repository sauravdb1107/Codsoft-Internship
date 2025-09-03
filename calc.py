import tkinter as tk

class Calculator:
    def __init__(self, root):
        self.root = root
        self.root.title("Simple GUI Calculator with Keyboard Support")
        self.expression = ""

        # Entry field
        self.entry = tk.Entry(root, font=("Arial", 20), bd=10, insertwidth=2, width=14, borderwidth=4, justify='right')
        self.entry.grid(row=0, column=0, columnspan=4)
        self.entry.focus_set()

        # Key bindings
        self.root.bind("<Key>", self.key_press)
        self.root.bind("<Return>", lambda event: self.calculate())
        self.root.bind("<BackSpace>", lambda event: self.backspace())
        self.root.bind("<Escape>", lambda event: self.clear())

        # Buttons layout
        buttons = [
            ('7',1,0), ('8',1,1), ('9',1,2), ('/',1,3),
            ('4',2,0), ('5',2,1), ('6',2,2), ('*',2,3),
            ('1',3,0), ('2',3,1), ('3',3,2), ('-',3,3),
            ('0',4,0), ('.',4,1), ('=',4,2), ('+',4,3),
            ('C',5,0), ('←',5,1)
        ]

        for (text, row, col) in buttons:
            if text == '=':
                tk.Button(root, text=text, padx=30, pady=20, font=("Arial", 14), command=self.calculate).grid(row=row, column=col)
            elif text == 'C':
                tk.Button(root, text=text, padx=30, pady=20, font=("Arial", 14), command=self.clear).grid(row=row, column=col)
            elif text == '←':
                tk.Button(root, text=text, padx=30, pady=20, font=("Arial", 14), command=self.backspace).grid(row=row, column=col)
            else:
                tk.Button(root, text=text, padx=30, pady=20, font=("Arial", 14), command=lambda t=text: self.on_click(t)).grid(row=row, column=col)

    def on_click(self, char):
        self.expression += str(char)
        self.update_entry()

    def key_press(self, event):
        char = event.char
        if char in '0123456789.+-*/':
            self.expression += char
            self.update_entry()

    def update_entry(self):
        self.entry.delete(0, tk.END)
        self.entry.insert(tk.END, self.expression)

    def clear(self):
        self.expression = ""
        self.update_entry()

    def backspace(self):
        self.expression = self.expression[:-1]
        self.update_entry()

    def calculate(self):
        try:
            result = str(eval(self.expression))
            self.expression = result
            self.update_entry()
        except Exception:
            self.entry.delete(0, tk.END)
            self.entry.insert(tk.END, "Error")
            self.expression = ""

if __name__ == "__main__":
    root = tk.Tk()
    app = Calculator(root)
    root.mainloop()
