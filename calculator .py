import tkinter as tk
from tkinter import messagebox

class Calculator:
    def __init__(self, root):
        self.root = root
        root.title("Simple Calculator")
        root.geometry("320x420")
        root.resizable(False, False)
        self.expression = ""
        self.display = tk.Entry(root, font=("Arial", 22), justify="right", state="readonly")
        self.display.pack(fill="x", padx=12, pady=15, ipady=12)

        buttons = [
            ["7", "8", "9", "/"],
            ["4", "5", "6", "*"],
            ["1", "2", "3", "-"],
            ["0", ".", "=", "+"],
        ]
        for row in buttons:
            frame = tk.Frame(root)
            frame.pack(expand=True, fill="both", padx=8)
            for label in row:
                tk.Button(frame, text=label, font=("Arial", 18),
                          command=lambda value=label: self.press(value)).pack(
                              side="left", expand=True, fill="both", padx=3, pady=3)
        tk.Button(root, text="Clear", font=("Arial", 14),
                  command=self.clear).pack(fill="x", padx=12, pady=10)

    def show(self, value):
        self.display.config(state="normal")
        self.display.delete(0, tk.END)
        self.display.insert(0, value)
        self.display.config(state="readonly")

    def press(self, value):
        if value == "=":
            try:
                # Only allow digits and basic arithmetic characters.
                if not self.expression or any(ch not in "0123456789.+-*/() " for ch in self.expression):
                    raise ValueError
                result = eval(self.expression, {"__builtins__": {}}, {})
                self.expression = str(result)
                self.show(self.expression)
            except Exception:
                messagebox.showerror("Error", "Invalid calculation.")
                self.clear()
        else:
            self.expression += value
            self.show(self.expression)

    def clear(self):
        self.expression = ""
        self.show("")

if __name__ == "__main__":
    root = tk.Tk()
    Calculator(root)
    root.mainloop()
