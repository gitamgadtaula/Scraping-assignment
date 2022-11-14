from nltk.tokenize import word_tokenize, sent_tokenize
from collections import Counter
import matplotlib.pyplot as plt
f = open('stopwords01.txt', 'r')  # Importing stopwords
stop_text = f.read()
tokenize_words = word_tokenize(stop_text)
list = open("corpus.txt", "r").read().split()
word_dict = Counter(list)
c = {k: v for k, v in word_dict.items() if k not in tokenize_words}
counts = Counter(c).most_common()[:20]
fig = plt.figure(figsize=(10, 5))
x_axis, y_axis = [], []

for item in counts:
    x_axis.append(item[0])
    y_axis.append(item[1])
print(x_axis, y_axis)
plt.bar(x_axis, y_axis, color='maroon', width=0.4)
plt.show()
