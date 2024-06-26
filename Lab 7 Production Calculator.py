
"""
Project Name: Production Calculator/ Lab 2
Description: This program allows users to calculate production costs and view receipts.
Authors: Braden Gerlach
Date: 5.12.2024

===== Header =====
The program includes a GUI for users to input their name, item details, and calculate production costs.
Users can view receipts showing their order details and costs.
The program uses Tkinter for the GUI and implements arithmetic calculations and date-time functions.

===== Changes Made =====
- Modified color scheme to create a purple city pop theme.
- Added descriptive prompts for user inputs.
- Implemented calculation of production costs based on user inputs.
- Included functionality to view receipts.
- Integrated datetime module for date-time functions.
- Updated formatting of numeric values using round() and string formatting.
- Ensured compliance with Python Style Guide rules.
"""
import tkinter as tk
from tkinter import messagebox
from datetime import datetime

# Global variables... They wisper to me, I dare not change them
entry_user_name = None
entry_item_name = None
entry_item_cost = None
entry_item_amount = None
result_label = None
main_window = None
receipt_calc = []

# Function to record current date and time
def current_datetime():
    return datetime.now().strftime("%Y-%m-%d %H:%M:%S")

# Main function to generate GUI
def main():
    generate_main_window_gui()

# Function to generate main window GUI
def generate_main_window_gui():
    global entry_user_name, entry_item_name, entry_item_cost, entry_item_amount, result_label, main_window

    main_window = tk.Tk()
    main_window.geometry("420x520")
    main_window.title("Production Calculator")
    main_window.config(background="#5E4FA2")  # Purple background
    main_window.resizable(width=False, height=False)

    # Name of user
    label_user = tk.Label(main_window,
                          text="What's the name of the user",
                          font=('Arial', 11,),
                          background="#5E4FA2",  # Purple background
                          fg="white")  # White text
    label_user.pack(pady=5)

    entry_user_name = tk.Entry(main_window, font=('Arial', 10))
    entry_user_name.pack(pady=5)

    # Name of item
    label_name = tk.Label(main_window,
                          text="What is the name of your item",
                          font=('Arial', 11,),
                          background="#5E4FA2",  # Purple background
                          fg="white")  # White text
    label_name.pack(pady=5)

    entry_item_name = tk.Entry(main_window, font=('Arial', 10))
    entry_item_name.pack(pady=5)

    # Cost of item
    label_cost = tk.Label(main_window,
                          text="What is the cost to produce one item in (USD)",
                          font=('Arial', 11,),
                          background="#5E4FA2",  # Purple background
                          fg="white")  # White text
    label_cost.pack(pady=10)

    entry_item_cost = tk.Entry(main_window, font=('Arial', 10))
    entry_item_cost.pack(pady=5)

    # Amount of item
    label_amount = tk.Label(main_window, text="How much of your item would you like to produce",
                            font=('Arial', 11,),
                            background="#5E4FA2",  # Purple background
                            fg="white")  # White text
    label_amount.pack(pady=10)

    entry_item_amount = tk.Entry(main_window, font=('Arial', 10))
    entry_item_amount.pack(pady=5)

    # Submit button
    submit_button = tk.Button(main_window, text="Calculate")
    submit_button.config(command=submit)
    submit_button.pack(pady=5)

    # View Receipt button
    receipt_button = tk.Button(main_window, text="View Receipt")
    receipt_button.config(command=lambda: receipt(main_window))
    receipt_button.pack(pady=5)

    # Results label
    result_label = tk.Label(main_window,
                            text="",
                            width=0,
                            bg="#5E4FA2",  # Purple background
                            fg="white")  # White text
    result_label.pack(pady=20)

    main_window.mainloop()

# The Submit and Calc
def submit():
    global entry_user_name, entry_item_name, entry_item_cost, entry_item_amount, result_label
    item_name = entry_item_name.get()
    user_name = entry_user_name.get()

    try:
        item_cost = float(entry_item_cost.get())
        item_amount = int(entry_item_amount.get())

        # Check for negative values
        if item_cost < 0 or item_amount < 0:
            result_label.config(text="Invalid input: Cost and amount cannot be negative")
            return

        item_sale = 0.35 * item_cost
        sale_cost = item_sale * item_amount
        no_sale_cost = item_cost * item_amount

        if sale_cost >= 100 and sale_cost:
            result = (f"Hello {user_name}, due to bulk order you have received a 25% sale on the cost\n"
                      f"to produce {item_amount} of {item_name} it is now {sale_cost:.2f} dollars"
                      f"\n\nThe price without a sale would be {no_sale_cost:.2f}."
                      )
            result_label.config(text=result)
        else:
            result = (f"Hello {user_name}, the cost to produce {item_amount} of {item_name}"
                      f" is {no_sale_cost:.2f} dollars")
            result_label.config(text=result)

        # Record the calculation and date-time
        receipt_calc.append((user_name, item_name, item_cost, item_amount, no_sale_cost, sale_cost, current_datetime()))

    except ValueError:
        result_label.config(text="Invalid Input: Goofball")

# Receipt Window and all that Jazz
def receipt(main_window):
    global receipt_calc

    if messagebox.askokcancel(title='View Receipt?', message='Would you like to view your receipt?'):
        # Hide the main window
        main_window.withdraw()

        new_window = tk.Toplevel()
        new_window.title("Receipt of production")
        new_window.geometry("350x550")
        new_window.config(background="#5E4FA2")  # Purple background

        # Display receipt
        for calc in receipt_calc:
            if len(calc) >= 6:
                user_name, item_name, item_cost, item_amount, no_sale_cost, sale_cost, date_time = calc[:7]
                if len(calc) > 6:
                    sale_cost = calc[5]
                else:
                    sale_cost = None

                if item_amount >= 35:
                    calc_str = (f"##########################################"
                                f"#\n #User: {user_name}, Ordered\n"
                                f"\n# Item:  {item_name}\n"
                                f"# Cost per Item: \n#  {item_cost:.2f}\n"
                                f"# The amount you Produced: \n#  {item_amount}\n"
                                f"# Cost before Sale of 25%\n"
                                f"# the Bulk Sale Cost: \n#  {sale_cost:.2f}\n"
                                f"# -----------------------------\n"
                                f"# Total Cost to Produce: \n#  {no_sale_cost:.2f}"
                                f"\n# Date & Time: {date_time}"
                                f"\n##########################################")
                else:
                    calc_str = (f"##########################################"
                                f"#\n User: {user_name}, Ordered\n"
                                f"\n# Item: {item_name}\n"
                                f"# Cost per Item:\n#  {item_cost:.2f}\n"
                                f"# The amount you Produced: \n#  {item_amount}\n"
                                f"# ------------------------\n"
                                f"# Total Cost to Produce: \n#  {no_sale_cost:.2f}"
                                f"\n# Date & Time: {date_time}"
                                f"\n##########################################")

                receipt_label = tk.Label(new_window, text=calc_str, justify="left", background="#5E4FA2", fg="white")
                receipt_label.pack(pady=20)

        new_window.mainloop()

# Calls the main function
main()