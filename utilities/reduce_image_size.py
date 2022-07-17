from PIL import Image

def convertIMG(orig_img, new_img):
    """
        reduce image size with this function
        :orig_img ---> original image before reducing it size (width, and height)
        :new_img ---> new image after reducing it size (width, and height)
    """
    img = Image.open(orig_img)

    # checking if the height and width are greater than 450
    if img.height > 450 or img.width > 450:
        pic_size = (450, 450)
        img.thumbnail(pic_size)
        img.save(new_img) # saving new image

convertIMG("/home/usman/Desktop/<my_image>_1.jpg", "/home/usman/Desktop/<my_image>_2.jpg")
