import tkinter as tk
from tkinter import messagebox

def make_gui(command):
    root = tk.Tk()
    root.title("Selenium GUI")

    tk.Label(root, text="Enter URL:").grid(row=0, column=0, padx=10, pady=10)
    entry_url = tk.Entry(root, width=50)
    entry_url.grid(row=0, column=1, padx=10, pady=10)

    run_button = tk.Button(root, text="Run Selenium", command=command)
    run_button.grid(row=1, columnspan=2, pady=10)

    root.mainloop()
