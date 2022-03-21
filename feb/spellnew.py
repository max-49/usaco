import itertools

def search(word, permutation):
    for letter in word:
        for block in permutation:
            if letter in block:
                permutation.remove(block)
                break
        else:
            return False
    return True

def blocked(word, blockss):
    permutations = [list(i) for i in list(itertools.permutations(blockss))]
    for permutation in permutations:
        if(search(word, permutation)):
            return "YES"
    return "NO"

n = int(input())
blocks = []
words = []
for i in range(4):
    blocks.append(list(input()))
for i in range(n):
    words.append(input())
for word in words:
    print(blocked(word, [item for item in blocks]))