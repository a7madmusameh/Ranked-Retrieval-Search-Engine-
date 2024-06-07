from nltk.corpus import stopwords
from nltk.corpus import wordnet
def fre_word_doc(text_read):
    punctuations = '''!()-[]{}\;:'",\n<>./?@#$%^&*_~'''
    stop_words_english = set(stopwords.words('english'))
    stop_words_Arabic = set(stopwords.words('Arabic'))
    set_fre_word = {}
    list_final_text2 = []
    list_lemmas_text = []
    final_list_lemmas = []
    text = ''
    #print(text_read)
    list_text_read = list(map(str, text_read.split()))
    #print(list_text_read)
    #print('=========================================================')
    for word in list_text_read:
        for char in word:
            if char not in punctuations:
                text += char
        if text != '':
            if text[0] in 'abcdefghigklmnopqrstuvwxyz':
                if text not in stop_words_english:
                    list_final_text2.append(text)
            else:
                if text[0] in 'د ج ح خ ه ع غ ف ق ث ص ض ذ ط ك م ن ت ا ل ب ي س ش ظ ز و ة ى ر ؤ ء ئ لا':
                    if text not in stop_words_Arabic:
                        list_final_text2.append(text)
        text = ''
    for index in range(len(list_final_text2)):
        for synset in wordnet.synsets(list_final_text2[index]):
            for lemma in synset.lemmas():
                if lemma.name() not in list_lemmas_text:
                    list_lemmas_text.append(lemma.name())
        if list_final_text2[index] not in list_lemmas_text:
            list_lemmas_text.append(list_final_text2[index])
        for word in list_lemmas_text:
            final_list_lemmas.append(word)
        list_lemmas_text = []
    set_lemmas_text = set(final_list_lemmas)
    for word in set_lemmas_text:
        set_fre_word.setdefault(word, final_list_lemmas.count(word))
    return set_fre_word