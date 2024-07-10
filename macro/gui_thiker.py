import tkinter as tk
from tkinter import messagebox


def make_gui():
    root = tk.Tk()
    root.title("네이버 GUI")
    root.geometry('800x600')
    label = tk.Label(root, text="안녕하세요, tkinter!")
    label.pack(pady=10)

    button = tk.Button(root, text="클릭하세요", command=on_button_click)
    button.pack(pady=10)
    entry = tk.Entry(root)
    # entry.grid(row=0, column=1, padx=10, pady=10)
    # entry.pack()

    root.mainloop()

    # tk.Label(root, text="Enter URL:").grid(row=0, column=0, padx=10, pady=10)
    # entry_url = tk.Entry(root, width=50)
    # entry_url.grid(row=0, column=1, padx=10, pady=10)

    # run_button = tk.Button(root, text="Run Selenium", command=command)
    # run_button.grid(row=1, columnspan=2, pady=10)

    # root.mainloop()


def on_button_click():
    messagebox.showinfo("정보", "완료 되었습니다")


make_gui()
