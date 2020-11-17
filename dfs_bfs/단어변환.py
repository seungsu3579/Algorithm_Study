# 단어변환


class Node:
    def __init__(self, word):
        self.word = word
        self.edges = []


def wordCompare(word1, word2):
    count = 0
    for k in range(len(word1)):
        if word1[k] != word2[k]:
            count += 1
    return count


def solution(begin, target, words):
    answer = 0
    wordList = dict()
    for word in words:
        wordList[word] = Node(word)
    wordList[begin] = Node(begin)

    for word, node in wordList.items():
        for c_word in words:
            if word != c_word:
                if wordCompare(word, c_word) == 1:
                    node.edges.append(c_word)
                else:
                    pass

    cursor = begin
    queue = [begin]
    searched = [begin]
    while target not in searched:
        new_queue = []
        for word in queue:
            for n_word in wordList[word].edges:
                if n_word not in searched:
                    new_queue.append(n_word)
                    searched.append(n_word)
        queue = new_queue
        answer += 1
        if len(queue) == 0:
            return 0

    return answer
