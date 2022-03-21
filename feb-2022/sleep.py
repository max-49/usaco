def sleep(case):
    times = 0
    while True:
        num = max(case)
        if all(element == case[0] for element in case):
            return times
        if len(case) <= 3:
            case[0] = case[0] + case[1]
            case.pop(1)
            times += 1
        else:
            for i in range(len(case)-1):
                if case[i] + case[i + 1] <= num:
                    case[i] = case[i] + case[i + 1]
                    case.pop(i+1)
                    times += 1
                    i -= 1

t = int(input()) 
test_cases = []
for i in range(t):
    n = int(input())
    test_cases.append([int(i) for i in input().split()])
for case in test_cases:
    print(sleep(case))
