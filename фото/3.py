from PIL import Image
files = ['1.jpg', '2.jpg', '3.jpg', '4.jpg', '5.jpg']

for file in files:
    img = Image.open(file)
    chb_img = img.convert('L')#ч/б фильтр

    chb_img.save(f'filt/chb_{file}') #сохраняем в новую папку

print("всо")