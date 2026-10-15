import tkinter as tk

root = tk. Tk()
root.title("grid関数")
root.geometry('400x200')

# ウィジェットの数
WIDGET_MAX = 9

# Labelウィジェットのリストを生成
labels = [
    tk.Label(
        root,
        text="NO_"+str(num),
        relief=tk.SOLID
    )
    for num in range(WIDGET_MAX)
]

for i in range(3):
    root.columnconfigure(i, weight=1, uniform="columns")
    root.rowconfigure(i, weight=1, uniform="rows")

# grid関数で配置
# デフォルトでは、ウィジェットは左端に配置される
for num in range(WIDGET_MAX):
    column = num % 3
    row = num // 3
    labels[num].grid(column=column, row=row, padx=5, pady=5, sticky="nsew")

root.mainloop()