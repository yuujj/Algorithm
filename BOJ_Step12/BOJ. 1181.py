### 단어 정렬 ###
n = int(input())
words = []
for _ in range(n):
    words.append(input())

words = sorted(set(words), key=lambda x: (len(x), x))

for word in words:
    print(word)