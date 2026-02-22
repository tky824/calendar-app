import tkinter as tk
from tkcalendar import Calendar
import json
import os

# ファイルの場所をカレンダーと同じフォルダに
save_file = os.path.join(os.path.dirname(__file__), "goals.json")

# 保存済みデータを読み込む
if os.path.exists(save_file):
    with open(save_file, "r") as f:
        goals = json.load(f)
else:
    goals = {}

root = tk.Tk()
root.title("カレンダーアプリ")

cal = Calendar(root, selectmode='day')
cal.pack(pady=20)

entry = tk.Entry(root, width=30)
entry.pack()

label = tk.Label(root, text="")
label.pack()

def save_goal():
    date = cal.get_date()
    goal = entry.get()
    goals[date] = goal
    label.config(text=f"{date} の目標: {goal}")
    # ファイルに保存
    with open(save_file, "w") as f:
        json.dump(goals, f)

button = tk.Button(root, text="目標を保存", command=save_goal)
button.pack(pady=10)

# 起動時にラベルに表示
for date, goal in goals.items():
    label.config(text=f"{date} の目標: {goal}")

root.mainloop()
