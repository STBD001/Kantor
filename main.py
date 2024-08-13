import tkinter as tk
from tkinter import ttk, messagebox
import requests
import json

def get_exchange_rate(from_currency, to_currency):
    url = f"https://api.exchangerate-api.com/v4/latest/{from_currency}"
    response = requests.get(url)
    data = response.json()
    return data['rates'][to_currency]

def calculate():
    try:
        amount = float(amount_entry.get())
        from_currency = from_currency_var.get()
        to_currency = to_currency_var.get()
        rate = get_exchange_rate(from_currency, to_currency)
        converted_amount = amount * rate
        result_label.config(text=f"{amount} {from_currency} = {converted_amount:.2f} {to_currency}")
        history.insert(tk.END, f"{amount} {from_currency} = {converted_amount:.2f} {to_currency}")
    except Exception as e:
        messagebox.showerror("Error", f"Could not convert currency: {e}")

# Interfejs użytkownika
root = tk.Tk()
root.geometry("400x450")
root.title("Kalkulator Walutowy")

# Kwota
amount_label = tk.Label(root, text="Kwota:")
amount_label.grid(row=0, column=0, padx=10, pady=10, sticky='e')
amount_entry = tk.Entry(root)
amount_entry.grid(row=0, column=1, padx=10, pady=10)

# Waluta źródłowa
from_currency_var = tk.StringVar()
to_currency_var = tk.StringVar()
currencies = ["USD", "EUR", "GBP", "PLN", "JPY"]

from_currency_label = tk.Label(root, text="Z waluty:")
from_currency_label.grid(row=1, column=0, padx=10, pady=10, sticky='e')
from_currency_menu = ttk.Combobox(root, textvariable=from_currency_var, values=currencies)
from_currency_menu.grid(row=1, column=1, padx=10, pady=10)
from_currency_menu.current(0)

# Waluta docelowa
to_currency_label = tk.Label(root, text="Na walutę:")
to_currency_label.grid(row=2, column=0, padx=10, pady=10, sticky='e')
to_currency_menu = ttk.Combobox(root, textvariable=to_currency_var, values=currencies)
to_currency_menu.grid(row=2, column=1, padx=10, pady=10)
to_currency_menu.current(1)

# Przycisk Przelicz
calculate_button = tk.Button(root, text="Przelicz", command=calculate)
calculate_button.grid(row=3, column=0, columnspan=2, pady=10, sticky='n')

# Wynik
result_label = tk.Label(root, text="")
result_label.grid(row=4, column=0, columnspan=2, pady=10, sticky='n')

# Historia
history_label = tk.Label(root, text="Historia przeliczeń:")
history_label.grid(row=5, column=0, padx=10, pady=10, sticky='e')
history = tk.Listbox(root, height=10, width=30)
history.grid(row=5, column=1, padx=10, pady=10)

# Przycisk Wyjście
exit_button = tk.Button(root, text="Wyjście", command=root.quit)
exit_button.grid(row=6, column=0, columnspan=2, pady=10, sticky='n')

root.mainloop()
