import jieba
import sklearn

s1 = "我来贪心学院学习python"

s1_result = jieba.cut(s1)
print(list(s1_result))

s1_result = jieba.cut(s1, cut_all=True)
print(list(s1_result))

s1_result = jieba.cut_for_search(s1)
print(list(s1_result))

word_vector_list = ["我们", "来", "贪心", "学院", "学习", "人工智能", "和", "Python"]
question = "Python学习多久"
s1 = "我来贪心学院学习Python"
s2 = "我学习人工智能"
s3 = "Python课程的学习周期是多久"

import numpy as np


def get_vector(data):
    vector_list = []

    for i in word_vector_list:
        if i in list(jieba.cut(data)):
            vector_list.append(1)
        else:
            vector_list.append(0)
    print(vector_list)
    return np.array(vector_list).reshape(1, -1)


questions_vector_list = get_vector(question)
s1_vector_list = get_vector(s1)
s2_vector_list = get_vector(s2)
s3_vector_list = get_vector(s3)

from sklearn.metrics.pairwise import cosine_similarity

print(cosine_similarity(questions_vector_list, s1_vector_list))
print(cosine_similarity(questions_vector_list, s2_vector_list))
print(cosine_similarity(questions_vector_list, s3_vector_list))

