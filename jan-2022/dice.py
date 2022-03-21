import random

num_cases = int(input())
cases = []
answers = []
for i in range(num_cases):
    case = input()
    cases.append(case.split())

for case in cases:
    times_win = 0
    die_a = [int(a) for a in case[:4]]
    die_b = [int(b) for b in case[4:]]
    for num in die_a:
        for numm in die_b:
            if num > numm:
                times_win += 1
    if times_win < 8:
        answers.append("no")
        continue
    else:
        if((1 in die_a or 1 in die_b) and (10 in die_a or 10 in die_b) or min(die_a) == 10 or die_b.count(1) == 4):
            answers.append("no")
        else:
            answers.append("yes")

for answer in answers:
    print(answer)

'''
or min(die_b)+1 >= 10
or max(die_a)-1 <= 1
'''

'''
10 5 3 4
1 7 2 3

1 1 10 10
'''