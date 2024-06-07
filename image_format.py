import aspose.pydrawing as drawing
def get_image_format(image_type):
    return {
        "jpeg": drawing.imaging.ImageFormat.jpeg,
        "emf": drawing.imaging.ImageFormat.emf,
        "bmp": drawing.imaging.ImageFormat.bmp,
        "png": drawing.imaging.ImageFormat.png,
        "wmf": drawing.imaging.ImageFormat.wmf,
        "gif": drawing.imaging.ImageFormat.gif,
        "jpg": drawing.imaging.ImageFormat.jpeg,
    }.get(image_type, drawing.imaging.ImageFormat.jpeg)

def ChiakImageFormat(path):
    if path[len(path)-4:].lower() == "jpeg":
        result = True
    elif path[len(path)-3:].lower() in ["png", "jpg"]:
        result = True
    else:
        result = False
    return result