import image_format
import index
import text
import Word
import pdf
import powerpoint
import image
def ReadFile(path):
    list_path_files = path.copy()
    index_file = 0
    Index_File_NotDefindType = []
    pointer_fre_word = []
    while index_file < len(path):
        if path[index_file][len(path[index_file])-3:].lower() == 'txt':
            text_read = text.Text(path[index_file])
            index_file += 1
        elif path[index_file][len(path[index_file])-4:].lower() == 'docx':
            text_read = Word.Word(path[index_file])
            index_file += 1
        elif path[index_file][len(path[index_file])-3:].lower() == 'pdf':
            text_read = pdf.PDF(path[index_file])
            index_file += 1
        elif path[index_file][len(path[index_file])-4:].lower() == 'pptx':
            text_read = powerpoint.PowerPoint(path[index_file])
            index_file += 1
        elif bool(image_format.ChiakImageFormat(path[index_file])):
            text_read = image.IMAGES(path[index_file])
            index_file += 1
        else:
            Index_File_NotDefindType .append(index_file)
            list_path_files.remove(path[index_file])
            index_file += 1
            continue
        pointer_fre_word.append(index.fre_word_doc(text_read))
    return pointer_fre_word, Index_File_NotDefindType, list_path_files