"""
Program: invest_calculator.py
Author: Jack Cacela
Generates and displays an investment calculator GUI that
can calculate a balance's total after a period of accrued interest.
"""

import tkinter as tk

class InvestmentCalculator:
    """A simple investment calculator using tkinter GUI."""

    def __init__(self):
        """Initialize the GUI and features."""
        self.root = tk.Tk() #instantiate the main application window object.
        self.root.title("Investment Calculator")

        # Labels and entry fields for user input
        tk.Label(self.root, text="Initial amount").grid(row=0, column=0)
        tk.Label(self.root, text="Years").grid(row=1, column=0)
        tk.Label(self.root, text="Interest rate %").grid(row=2, column=0)

        # Create variables of types double and integer to hold data
        self.amount = tk.DoubleVar() 
        tk.Entry(self.root, textvariable=self.amount).grid(row=0, column=1)

        self.period = tk.IntVar()
        tk.Entry(self.root, textvariable=self.period).grid(row=1, column=1)

        self.rate = tk.DoubleVar()
        tk.Entry(self.root, textvariable=self.rate).grid(row=2, column=1)

        # Text area for output
        self.outputArea = tk.Text(self.root, width=50, height=15)
        self.outputArea.grid(row=4, column=0, columnspan=2)

        # Button to trigger computation
        tk.Button(self.root, text="Compute", command=self.compute).grid(row=3, column=0, columnspan=2)

    def compute(self):
        """Compute and display the investment details."""
        start_balance = self.amount.get()
        rate = self.rate.get() / 100
        years = self.period.get()

        if start_balance == 0 or rate == 0 or years == 0:
            return

        self.outputArea.delete('1.0', tk.END) # Delete info in the output area
        self.outputArea.insert(tk.END, f"{'Year':<4}{'Starting balance':>18}{'Interest':>10}{'Ending balance':>16}\n") #Insert the header

        total_interest = 0.0
        for year in range(1, years + 1):
            interest = start_balance * rate
            end_balance = start_balance + interest
            self.outputArea.insert(tk.END, f"{year:<4}{start_balance:>18.2f}{interest:>10.2f}{end_balance:>16.2f}\n")
            start_balance = end_balance
            total_interest += interest

        self.outputArea.insert(tk.END, f"\nEnding balance: ${end_balance:.2f}\n")
        self.outputArea.insert(tk.END, f"Total interest earned: ${total_interest:.2f}\n")

    def run(self):
        """Run the tkinter main loop after the setup tasks above are complete, and this
        mainloop method here keeps the GUI responsive to user actions."""
        self.root.mainloop() 

if __name__ == "__main__":
    app = InvestmentCalculator() # This automatically and only triggers the __init__ method of InvestmentCalculator and stores the results in the app variable.
    app.run() # Then, this line invokes the run method so that the GUI can be listening for user actions such as when they press the compute button.