from nltk.corpus import stopwords
def query(query):
    stop_words_english = set(stopwords.words('english'))
    stop_words_Arabic = set(stopwords.words('Arabic'))
    punctuations = '''!()-[]{}\;:'",\n<>./?@#$%^&*_~'''
    list_querys = []
    text = ''
    # ===============================================
    for word_query in query:
        for char in word_query:
            if char not in punctuations:
                text += char
        if text != '':
            if text[0] in 'abcdefghigklmnopqrstuvwxyz':
                if text not in stop_words_english:
                    list_querys.append(text)
            else:
                if text[0] in 'د ج ح خ ه ع غ ف ق ث ص ض ذ ط ك م ن ت ا ل ب ي س ش ظ ز و ة ى ر ؤ ء ئ لا':
                    if text not in stop_words_Arabic:
                        list_querys.append(text)
        text = ''
    set_querys = set(list_querys)
    return set_querys
