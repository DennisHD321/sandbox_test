import customtkinter as ctk
from tkinter import messagebox

class ModernCalculator:
    def __init__(self, root):
        """
        Initializes the calculator's modern user interface.
        """
        self.root = root
        self.root.title("Modern Calculator")
        self.root.geometry("400x500")

        # --- Appearance Settings ---
        ctk.set_appearance_mode("System")  # Options: "System", "Dark", "Light"
        ctk.set_default_color_theme("blue")  # Options: "blue", "green", "dark-blue"

        # --- Variables ---
        self.expression = ""

        # --- GUI Elements ---
        # Display Screen
        self.display_frame = ctk.CTkFrame(self.root)
        self.display_frame.pack(pady=20, padx=20, fill="x")

        self.display_label = ctk.CTkLabel(self.display_frame, text="", font=ctk.CTkFont(size=35), anchor="e")
        self.display_label.pack(padx=10, pady=10, fill="x")

        # Buttons Frame
        self.buttons_frame = ctk.CTkFrame(self.root)
        self.buttons_frame.pack(pady=10, padx=20, fill="both", expand=True)

        self.create_buttons()

    def create_buttons(self):
        """
        Creates and places all the calculator buttons.
        """
        buttons = [
            ['7', '8', '9', '/'],
            ['4', '5', '6', '*'],
            ['1', '2', '3', '-'],
            ['0', '.', '=', '+']
        ]

        for i, row in enumerate(buttons):
            self.buttons_frame.grid_rowconfigure(i, weight=1)
            for j, button_text in enumerate(row):
                self.buttons_frame.grid_columnconfigure(j, weight=1)
                button = ctk.CTkButton(self.buttons_frame, text=button_text, font=ctk.CTkFont(size=20),
                                       command=lambda text=button_text: self.on_button_click(text))
                button.grid(row=i, column=j, padx=5, pady=5, sticky="nsew")

        # Clear Button
        clear_button = ctk.CTkButton(self.buttons_frame, text="C", font=ctk.CTkFont(size=20),
                                     command=self.clear_display)
        clear_button.grid(row=4, column=0, columnspan=2, padx=5, pady=5, sticky="nsew")

        # Backspace Button
        backspace_button = ctk.CTkButton(self.buttons_frame, text="⌫", font=ctk.CTkFont(size=20),
                                     command=self.backspace)
        backspace_button.grid(row=4, column=2, columnspan=2, padx=5, pady=5, sticky="nsew")


    def on_button_click(self, char):
        """
        Handles button clicks and updates the display.
        """
        if char == "=":
            self.calculate()
        else:
            self.expression += str(char)
            self.update_display()

    def update_display(self):
        """
        Updates the text on the display label.
        """
        self.display_label.configure(text=self.expression)

    def calculate(self):
        """
        Evaluates the expression and shows the result.
        """
        try:
            # Replace any expressions that could be a security risk if needed
            # For a simple calculator, eval() is okay but be aware of its risks
            result = str(eval(self.expression))
            self.expression = result
            self.update_display()
        except ZeroDivisionError:
            messagebox.showerror("Error", "Cannot divide by zero.")
            self.expression = ""
            self.update_display()
        except Exception:
            messagebox.showerror("Error", "Invalid Input")
            self.expression = ""
            self.update_display()

    def clear_display(self):
        """
        Clears the entire display.
        """
        self.expression = ""
        self.update_display()

    def backspace(self):
        """
        Removes the last character from the display.
        """
        self.expression = self.expression[:-1]
        self.update_display()

if __name__ == "__main__":
    root = ctk.CTk()
    app = ModernCalculator(root)
    root.mainloop()