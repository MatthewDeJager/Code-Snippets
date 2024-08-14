import tkinter as tk
import string
import random
from tkinter import messagebox

class App:
    def __init__(self, root):
        self.root = root
        self.root.title("Password generator")
        self.root.geometry("300x439+800+308")    

        self.labelAmount = tk.Label(root, width=18, text="Amount of characters:")
        self.labelAmount.grid(row=0, column=0, pady=10)
        self.entryAmount = tk.Entry(root, width=10)
        self.entryAmount.grid(row=0, column=1)
    
        self.buttonIncLet = tk.Button(root, text="Include letters", command=lambda: self.toggle_letters(self.buttonIncLet))
        self.buttonIncLet.grid(row=1, column=0)

        self.buttonLower = tk.Button(root, text="Include lowercase letters", height=1, state="disabled", command=lambda: self.toggle_button(self.buttonLower))
        self.buttonLower.grid(row=2, column=0)

        self.buttonUpper = tk.Button(root, text="Include uppercase letters", height=1, state="disabled", command=lambda: self.toggle_button(self.buttonUpper))
        self.buttonUpper.grid(row=3, column=0)

        self.buttonNumber = tk.Button(root, text="Include numbers", width=19, command=lambda: self.toggle_button(self.buttonNumber))
        self.buttonNumber.grid(row=4, column=0)

        self.buttonSpecial = tk.Button(root, text="Include special characters", relief="raised", command=lambda: self.toggle_button(self.buttonSpecial))
        self.buttonSpecial.grid(row=5, column=0)

        self.buttonSubmit = tk.Button(root, text="Submit", command=self.calculate, height=1, font=(15), width=12)
        self.buttonSubmit.grid(row=7, column=0, pady=(0, 20))

        self.labelPassword = tk.Label(root, text="Generated password:", font=(5))
        self.labelPassword.grid(row=8, column=0)

        self.textPassword = tk.Text(root, width = 20, height = 5, wrap=None, state="disabled")
        self.textPassword.grid(row=9, column=0, padx=(10, 0))
 
        self.buttonExit = tk.Button(root, text="Exit application", command=root.destroy, font=(15))
        self.buttonExit.grid(row=10, column=0, pady=(50, 0))

        self.include_lower = False
        self.include_upper = False
        self.include_digits = False
        self.include_special = False

    def toggle_letters(self, button):
        if self.buttonLower.config('state')[-1] == "disabled":
            self.buttonLower.config(state="normal")
            self.buttonUpper.config(state="normal")
            self.buttonLower.config(relief="raised")
            self.buttonUpper.config(relief="raised")
            self.include_lower = False
            self.include_upper = False
        else:
            self.buttonLower.config(state="disabled")
            self.buttonUpper.config(state="disabled")
            self.buttonLower.config(relief="raised")
            self.buttonUpper.config(relief="raised")
            self.include_lower = False
            self.include_upper = False

    def toggle_button(self, button):
        if button.config('relief')[-1] == "raised":
            button.config(relief="sunken")
            if button == self.buttonLower:
                self.include_lower = True
            elif button == self.buttonUpper:
                self.include_upper = True
            elif button == self.buttonNumber:
                self.include_digits = True
            elif button == self.buttonSpecial:
                self.include_special = True
        else:
            button.config(relief="raised")
            if button == self.buttonLower:
                self.include_lower = False
            elif button == self.buttonUpper:
                self.include_upper = False
            elif button == self.buttonNumber:
                self.include_digits = False
            elif button == self.buttonSpecial:
                self.include_special = False
      
    def calculate(self):
        try:
            length_pass = int(self.entryAmount.get())
            if length_pass > 0 and length_pass <= 100:
                special = string.punctuation
                lower = string.ascii_lowercase
                upper = string.ascii_uppercase
                letters = string.ascii_letters
                digits = string.digits
                password = ''
                pool = ''

                if self.include_special:
                    pool+=special
                if self.include_digits:
                    pool+=digits
                if self.include_lower and self.include_upper:
                    pool += lower
                    pool += upper
                elif self.include_lower:
                    pool += lower
                elif self.include_upper:
                    pool+=upper

                try:
                    length_pool = len(pool)
                    for i in range(length_pass):
                        rnd = random.randrange(0, length_pool)
                        password += pool[rnd]
                except:
                    print("Please make sure at least one of the character sets is included")
                self.textPassword.config(state="normal")
                self.textPassword.delete(1.0, tk.END)
                self.textPassword.insert(tk.END, password)
                self.textPassword.config(state="disabled")
            else:
                self.entryAmount.delete(0, tk.END)
                self.textPassword.config(state="normal")
                self.textPassword.delete(1.0, tk.END)
                self.textPassword.config(state="disabled")
                messagebox.showinfo("Password length error", "Password can only be between 1 and 100 characters long")

        except:
            self.entryAmount.delete(0, tk.END)
            messagebox.showinfo("Password length error", "Please enter a valid number as the length of the password")

root = tk.Tk()

app = App(root)

root.mainloop()