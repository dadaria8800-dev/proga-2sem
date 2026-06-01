import tkinter as tk
from datetime import datetime
import json
import random
import os
from PIL import Image, ImageTk

with open("motivation.json", "r", encoding="utf-8") as f:
    data = json.load(f)
    phrases_dict = data["phrases"]


def get_phrase_by_time_left(delta_hours):
    if delta_hours < 1:
        return random.choice(phrases_dict["critical"])
    elif delta_hours < 6:
        return random.choice(phrases_dict["few_hours"])
    elif delta_hours < 30:
        return random.choice(phrases_dict["one_day"])
    elif delta_hours < 120:
        return random.choice(phrases_dict["few_days"])
    else:
        return random.choice(phrases_dict["many_days"])


def update_current_time():
    now = datetime.now().strftime("%d.%m %H:%M:%S")
    label_now.config(text=now)
    root.after(1000, update_current_time)


def load_local_image(total_hours):
    if total_hours < 6:
        img_path = "images/panic.jpg"
    elif total_hours < 30:
        img_path = "images/study.jpg"
    else:
        img_path = "images/relax.jpg"

    if os.path.exists(img_path):
        img = Image.open(img_path)
        img.thumbnail((450, 400), Image.Resampling.LANCZOS)
        photo = ImageTk.PhotoImage(img)
        label_image.config(image=photo)
        label_image.image = photo


def calculate_deadline():
    try:
        deadline_str = entry_deadline.get()
        now = datetime.now()

        day_month, time_part = deadline_str.split()
        day, month = map(int, day_month.split('.'))
        hour, minute = map(int, time_part.split(':'))

        year = now.year
        deadline = datetime(year, month, day, hour, minute)

        if deadline < now:
            deadline = datetime(year + 1, month, day, hour, minute)

        delta = deadline - now
        days = delta.days
        hours = delta.seconds // 3600
        minutes = (delta.seconds % 3600) // 60
        total_hours = delta.total_seconds() / 3600

        if days > 0:
            time_text = f"{days} дн {hours} час {minutes} мин"
        elif hours > 0:
            time_text = f"{hours} час {minutes} мин"
        else:
            time_text = f"{minutes} мин"

        label_result.config(text=time_text)
        phrase = get_phrase_by_time_left(total_hours)
        label_phrase.config(text=phrase)

        if total_hours < 6:
            root.configure(bg="#ff6666")
            label_result.config(fg="#cc0000", font=("Arial", 38, "bold"))
            label_phrase.config(fg="#cc0000")
        elif total_hours < 30:
            root.configure(bg="#ffcc80")
            label_result.config(fg="#e65c00", font=("Arial", 38, "bold"))
            label_phrase.config(fg="#e65c00")
        else:
            root.configure(bg="#66ff66")
            label_result.config(fg="#008000", font=("Arial", 38, "bold"))
            label_phrase.config(fg="#008000")

        load_local_image(total_hours)

    except:
        label_result.config(text="Ошибка!\nДД.ММ ЧЧ:ММ", fg="#cc0000")


root = tk.Tk()
root.title("Дедлайн?")
root.geometry("520x750")
root.configure(bg="white")

tk.Label(root, text="дата и время сейчас", font=("Arial", 12), bg="white", fg="gray").pack(pady=(20, 0))
label_now = tk.Label(root, text="", font=("Arial", 18, "bold"), bg="white")
label_now.pack()
update_current_time()

tk.Label(root, text="дата и время дедлайна", font=("Arial", 12), bg="white", fg="gray").pack(pady=(20, 0))
entry_deadline = tk.Entry(root, font=("Arial", 16), justify="center", width=20)
entry_deadline.pack(pady=8)

tk.Button(root, text="посмотреть", command=calculate_deadline,
          font=("Arial", 14), bg="black", fg="white", padx=30, pady=8).pack(pady=15)

label_result = tk.Label(root, text="", font=("Arial", 38, "bold"), bg="white")
label_result.pack(pady=10)

label_phrase = tk.Label(root, text="", font=("Arial", 14, "italic"),
                        bg="white", wraplength=450, padx=10, pady=10)
label_phrase.pack(pady=5)

label_image = tk.Label(root, bg="white", text="")
label_image.pack(pady=10, expand=True)

root.mainloop()