"""
Lacuna-C 'Lacuna Compiler'
"""
import os, sys, ctypes
import tkinter as tk
from tkinter import messagebox

' Lacuna Objects '
winDLL = ctypes.windll
user32 = winDLL.user32
def on_select(event):
    selected_items = [listbox.get(idx) for idx in listbox.curselection()]
    print(f"Selected: {', '.join(selected_items)}")
def compile_selected():
    selected_items = [listbox.get(idx) for idx in listbox.curselection()]
    webhook_url = webhook_entry.get()
    if selected_items and webhook_url:
        print(selected_items)
        print(webhook_url)
    else:
        user32.MessageBoxW(None, f"Please make sure to have options selected & a webhook URL", "Lacuna", 0)

' Lacuna Interface '
root = tk.Tk()
root.title("Lacuna Compiler")
root.geometry("300x300")
root.resizable(False,False)

listbox = tk.Listbox(root, selectmode=tk.MULTIPLE)
listbox.pack(padx=20, pady=20)
for item in ["Token Logging", "Option 2", "Option 3", "Option 4", "Option 5"]:
    listbox.insert(tk.END, item)
listbox.bind("<<ListboxSelect>>", on_select)

webhook_label = tk.Label(root, text="Webhook URL:")
webhook_label.pack(pady=5)
webhook_entry = tk.Entry(root, width=50)
webhook_entry.pack(pady=5)

compile_button = tk.Button(root, text="Compile", command=compile_selected)
compile_button.pack(pady=10)

root.mainloop()