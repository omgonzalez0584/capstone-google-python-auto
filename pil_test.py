from PIL import Image

im = Image.open('naruto.jpg')
new_im = im.rotate(90).resize((300,300))
new_im.save('naruto_new.jpg')
