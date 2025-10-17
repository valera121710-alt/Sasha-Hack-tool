import tkinter as tk
import random
import time
from tkinter import messagebox

# Создаем главное окно
window = tk.Tk()
window.title("⚡ САША-ХАКЕР 3000 ⚡")
window.geometry("600x500")
window.configure(bg='black')

# Стиль хакера
title_label = tk.Label(window, text="СИСТЕМА ВЗЛОМА АКТИВИРОВАНА", 
                      font=("Courier", 16, "bold"), 
                      bg='black', fg='#00ff00')
title_label.pack(pady=20)

# Поле для хакерских логов
log_text = tk.Text(window, height=15, width=70, 
                  bg='black', fg='#00ff00', 
                  font=("Courier", 10))
log_text.pack(pady=10)

# Функция для добавления хакерских сообщений
def add_hack_message(message):
    log_text.insert(tk.END, f"> {message}\n")
    log_text.see(tk.END)
    window.update()

# Хакерские команды
def start_hack():
    add_hack_message("Инициализация взлома...")
    time.sleep(1)
    add_hack_message("Подключение к серверу... УСПЕХ!")
    time.sleep(1)
    add_hack_message("Обход защиты... ВЫПОЛНЕНО!")
    time.sleep(1)
    add_hack_message("Доступ к ядру системы... ПОЛУЧЕН!")
    time.sleep(1)
    add_hack_message("САША-ХАКЕР РУЛИТ! 🎮")
    add_hack_message("ВЗЛОМ ЗАВЕРШЕН НА 100%! 💯")

# Кнопка запуска взлома
hack_button = tk.Button(window, text="🚀 ЗАПУСТИТЬ ВЗЛОМ", 
                       command=start_hack,
                       bg='red', fg='white', 
                       font=("Arial", 14, "bold"),
                       width=20, height=2)
hack_button.pack(pady=10)

# Стартовое сообщение
add_hack_message("Система готова к взлому...")
add_hack_message("Ожидание команд от САША-ХАКЕРА...")

window.mainloop()