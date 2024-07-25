import webbrowser
from PIL import Image


def resize_img(orig_img_path, new_img_path):
    """Reduce image size with this function
        :orig_img_path ---> original image before reducing it size (width, and height)
        :new_img_path ---> new image after reducing it size (width, and height)
    """
    img = Image.open(orig_img_path)

    # checking if the height and width are greater than 450
    if img.height > 450 or img.width > 450:
        pic_size = (450, 450)
        img.thumbnail(pic_size)
        img.save(new_img_path) # saving new image


new_path_for_resize_img = "/home/usman/Desktop/media/resize_img.jpg"

resize_img("/home/usman/Desktop/media/ai.jpg", new_path_for_resize_img)

# open it on browser
webbrowser.get().open(new_path_for_resize_img)
