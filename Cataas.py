
from tkinter import *
from PIL import Image, ImageTk
import requests
from io import BytesIO

def load_image(url):
    try:
        # Отправляем GET-запрос с использованием requests.get()
        response = requests.get(url)

        # Проверяем успешность запроса (код ответа 200)
        response.raise_for_status()

        # Читаем байты из ответа в объект BytesIO
        image_data = BytesIO(response.content)

        # Открываем изображение с помощью PIL
        img = Image.open(image_data)
        img.thumbnail((600, 480), Image.Resampling.LANCZOS)
        return ImageTk.PhotoImage(img)
    except Exception as e:
        print(f"Ошибка при загрузке изображения: {e}")
        return None


def set_image():
     img = load_image(url)  # Вызываем функцию для загрузки изображения

     if img:
         # Устанавливаем изображение в метку
         label.config(image=img)
         # Необходимо сохранить ссылку на изображение, чтобы избежать сборки мусора
         label.image = img


window = Tk()
window.title("Cats!")
window.geometry("600x520")

# Создаем метку без изображения
label = Label()
label.pack()

# Добавляем кнопку для обновления изображения
update_buttun = Button(text='Обновить', command=set_image)
update_buttun.pack()

url = 'https://cataas.com/cat'

# Вызываем функцию для установки изображения в метку
set_image()


window.mainloop()