from pdfminer.high_level import extract_text
import fitz
import image_format
import image
import PIL.Image
import io
import os
def PDF(path):
    pdf = fitz.open(path)
    imageIndex = 1
    all_text_pdf = extract_text(path).lower().replace('\n', ' ')
    for i in range(len(pdf)):
        page = pdf[i]
        images = page.get_images()
        for imag in images:
            base_img = pdf.extract_image(imag[0])
            image_data = base_img['image']
            img = PIL.Image.open(io.BytesIO(image_data))
            extension = base_img['ext']
            # save image
            img.save(open(f'image{imageIndex}.{extension}', 'wb'))
            # path the image
            path_of_image = f'image{imageIndex}.{extension}'
            # check if type image in image format
            if bool(image_format.ChiakImageFormat(path_of_image)):
                # read text from image
                img_text_png = image.IMAGES(path_of_image)
                # check if image contain on text
                if img_text_png != '':
                    # add text image in all text
                    all_text_pdf += ' ' + img_text_png
            # delete image
            os.remove(path_of_image)
            # number of image
            imageIndex += 1
    return all_text_pdf
#print(PDF('Chapter04 modified.pdf'))