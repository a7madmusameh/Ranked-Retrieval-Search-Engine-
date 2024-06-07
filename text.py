def Text(path):
    with open(path) as file_txt:
        text_read = file_txt.read().lower().replace('\n', ' ')
    return text_read
