'''
AABCDD
afzz
09121
a8EWg6
P5h3kx
'''

# 문자열 개념 복습

### Try-except
word_list = []
max_length = 0
for _ in range(5):
    word = input()
    if max_length < len(word):
        max_length = len(word)
    word_list.append(word)

result = ''
for i in range(max_length):
    for word in word_list:
        # try-except 말고 극복할 수 있는 방법은?
        try:
            result += word[i]
        except IndexError:
            pass

print(result)

### length check
wordList = []
maxLength = 0
for _ in range(5):
    word = input()
    n = len(word)
    wordList.append((word, n))
    if maxLength < n:
        maxLength = n

result = ''
for i in range(maxLength):
    for word, length in wordList:
        if length <= i:
            continue
        else:
            result += word[i]

print(result)