from tkinter import messagebox
import tkinter as tk

# ハンドラ関数
def morning():
    messagebox.showinfo("6:00~10:30", "おはよう!")
# ハンドラ関数
def afternoon():
    messagebox.showinfo("10:30~17:00", "こんにちは!")
# ハンドラ関数
def evening():
    messagebox.showinfo("17:00~21:30", "こんばんは!")

root = tk.Tk()
root.title("イベントドリブン")
root.geometry("250x150")

root.columnconfigure(0, weight=1)

# ラベル
label = tk.Label(root, text="Press the button")
label.grid(row=0, column=0)

# Buttonウィジェットの生成と配置
button_morning = tk.Button(
    root,
    text="morning",
    command=morning
)
button_morning.grid(row=1, column=0, pady=5)
# Buttonウィジェットの生成と配置
button_afternoon = tk.Button(
    root,
    text="afternoon",
    command=afternoon
)
button_afternoon.grid(row=2, column=0, pady=5)
# Buttonウィジェットの生成と配置
button_evening = tk.Button(
    root,
    text="evening",
    command=evening
)
button_evening.grid(row=3, column=0, pady=5)

root.mainloop()
