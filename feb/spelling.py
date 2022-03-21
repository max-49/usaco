import collections

def blocked(word, blockss):
    counts = []
    shift_times = 0
    in_blocks = []
    while True:
        temp = collections.deque(blockss)
        temp.rotate(shift_times)
        blockss = list(temp)
        for letter in word:
            for block in blockss:
                if block in in_blocks:
                    continue
                if letter in block:
                    in_blocks.append(block)
                    break
            else:
                if len(in_blocks) == 0 or shift_times == 3 or all(i < 2 for i in counts):
                    return "NO"
                else:
                    shift_times += 1
                    in_blocks = []
                    break
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
