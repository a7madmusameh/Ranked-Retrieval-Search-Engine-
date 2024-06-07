import aspose.words as aw
import docx2txt
import image_format
import image
import os
def Word(path):
    # open the file and read text
    all_text_word = docx2txt.process(path).lower().replace('\n', ' ')
    # load the Word document
    doc = aw.Document(r''+path)
    # retrieve all shapes
    shapes = doc.get_child_nodes(aw.NodeType.SHAPE, True)
    imageIndex = 1
    # loop through shapes
    for shape in shapes:
        shape = shape.as_shape()
        if (shape.has_image) :
            # set image file's name
            path_of_image = f"Image{imageIndex}{aw.FileFormatUtil.image_type_to_extension(shape.image_data.image_type)}"
            # save image
            shape.image_data.save(path_of_image)
            # check if type image in image format
            if bool(image_format.ChiakImageFormat(path_of_image)):
                # read text from image
                img_text_png = image.IMAGES(path_of_image)
                # check if image contain on text
                if img_text_png != '':
                    # add text image in all text
                    all_text_word += ' ' + img_text_png
            # delete image
            os.remove(path_of_image)
            # number of image
            imageIndex += 1
    return all_text_word
#print(Word("First CIS260 summer 2018-2019 v2.docx"))