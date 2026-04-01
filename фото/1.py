from PIL import Image

file_name = '5.jpg'
img = Image.open(file_name)

img.show() #показываем картинку

width, height = img.size
print(f"размер изображения: {width} x {height} пикселей")

print(f"формат изображения: {img.format}")

print(f"цветовая модель: {img.mode}")