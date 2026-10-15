import tkinter as tk

root = tk.Tk()
root.title("grid関数：縦に並べる")
root.geometry("400x250")

# ウィジェットの数
WIDGET_MAX = 8

# Labelウィジェットのリストを生成
labels = [
    tk.Label(root, text="NO_" + str(num), relief=tk.SOLID)
    for num in range(WIDGET_MAX)
]

# 同じ列に、行番号を変えて上から順に配置する
for num in range(WIDGET_MAX):
    labels[num].grid(column=0, row=num)

root.mainloop()
