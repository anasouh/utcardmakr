from PIL import Image

def resize_or_thumbnail(img: Image, size: tuple) -> Image:
    if img.size[0] > size[0] or img.size[1] > size[1]:
        img.thumbnail(size, Image.LANCZOS)
    else:
        img = img.resize(size)
    return img