from PIL import Image

def resize():

    img = Image.open('C:/Users/BTLsub/realsite/media/input/원본.jpg')

    img_resize = img.resize((256, 256))
    img_resize.save('C:/Users/BTLsub/realsite/media/input/원본.png')

# 얘는 또 왜 png로만 변환 가능하고 난리.. 
