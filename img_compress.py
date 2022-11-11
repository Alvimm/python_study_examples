import tkinter.filedialog

from PIL import Image

fl = tkinter.askopenfilenames()
img = Image.open(fl[0])
img.save("test.jpg", 'JPEG', optimaze=True, quality=10)
Image.open('test.jpg')
