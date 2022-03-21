def blocked(word, blockss):
    for letter in word:
        for block in blockss:
            if letter in block:
                blockss.remove(block)
                break
        else:
            # letter in no blocks
            return "NO"
    return "YES"

n = int(input())
blocks = []
words = []
for i in range(4):
    blocks.append(list(input()))
for i in range(n):
    words.append(input())
for word in words:
    print(blocked(word, [item for item in blocks]))