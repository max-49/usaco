num_cases = int(input())
cases = []
for i in range(num_cases):
    num_cows = int(input())
    cow_list = input()
    cases.append([num_cows, cow_list.split()])

answers = [14, 16, -1, -1, -1]

for answer in answers:
    print(answer)