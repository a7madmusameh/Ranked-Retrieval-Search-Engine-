import math
import Quick_Sort
def Rank(ReadAllTypeFiles, Querys):
    frequnency_word, Index_File_NotDefindType, list_path_files = ReadAllTypeFiles
    set_querys = Querys
    set_fre_text = {}
    list_fre_text = []
    query_idf_weight = []
    tf_idf_weight = {}
    tf_idf_list = []
    list_score = []
    set_score = {}
    cosine_score = {}
    list_cosine_score = []
    list_cosine_score_text = []
    index2 = 0
    index_list_count_fre_text = 0
    index4 = 0
    list_count_fre_text = list(0 for j in range(len(set_querys)))
    for index1 in range(len(list_path_files)):
        for word in set_querys:
            if word in frequnency_word[index1]:
                list_fre_text.append(frequnency_word[index1].get(word))
                list_count_fre_text[index_list_count_fre_text] += 1
                index_list_count_fre_text += 1
            else:
                list_fre_text.append(0)
        index_list_count_fre_text = 0
        set_fre_text.setdefault(list_path_files[index1], list_fre_text)
        list_fre_text = []
    for index3 in range(len(list_count_fre_text)):
        if list_count_fre_text[index3] != 0:
            idf = math.log(len(list_path_files) / list_count_fre_text[index3])
            query_idf_weight.append(idf)
        else:
            query_idf_weight.append(0)
    if len(list_path_files) == 1:
        if sum(set_fre_text.get(list_path_files[0])) < 1:
            return 'No results were found'
    else:
        for path in list_path_files:
            while index2 < len(set_fre_text.get(path)):
                if set_fre_text.get(path)[index2] != 0 and list_count_fre_text[index2] != 0:
                    tf_idf = (1 + math.log(set_fre_text.get(path)[index2])) * math.log(len(list_path_files) / list_count_fre_text[index2])
                    index2 += 1
                    tf_idf_list.append(tf_idf)
                else:
                    tf_idf_list.append(0)
                    index2 += 1
            index2 = 0
            tf_idf_weight.setdefault(path, tf_idf_list)
            tf_idf_list = []
            for index3 in range(len(query_idf_weight)):
                score = tf_idf_weight.get(path)[index3] * query_idf_weight[index3]
                list_score.append(score)
            set_score.setdefault(path, list_score)
            list_score = []
            cosine_score.setdefault(path, sum(set_score.get(path)))
            if cosine_score.get(path) != 0:
                list_cosine_score.append(cosine_score.get(path))
    Quick_Sort.Quick_Sort(list_cosine_score, 0, len(list_cosine_score)-1)
    list_order = list(cosine_score.items())
    if len(list_cosine_score) != 0:
        while index4 < len(list_cosine_score):
            for item in list_order:
                if item[1] == list_cosine_score[index4] and item[1] != 0:
                    if item[0] not in list_cosine_score_text:
                        list_cosine_score_text.append(item[0])
                        index4 += 1
                        break
        return str(list_cosine_score[:10]) + '\n' + str(list_cosine_score_text[:10])
    else:
        return 'No results were found'