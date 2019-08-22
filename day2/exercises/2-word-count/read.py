
from collections import Counter
def word_stats(file_name, n):

    file_object = open(file_name, "r")
    f = file_object.read().lower()
    list_f = f.split()

    counter = Counter(list_f)
    most_occ = counter.most_common(n)
    print(most_occ)

word_stats("article.txt", 10)
# for line in file_object:
#     words = line.split()
#     counter = Counter(words)
#     most_occ = counter.most_common(2)
#     print(most_occ)