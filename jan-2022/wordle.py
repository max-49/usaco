answer_grid = [list(input()), list(input()), list(input())]
guess_grid = [list(input()), list(input()), list(input())]

num_green = 0
num_yellow = 0

for i, (x,y) in enumerate(zip(answer_grid, guess_grid)):
    for j, (a,b) in enumerate(zip(x,y)):
        if a == b:
            num_green += 1
            guess_grid[i][j] = 'GREEN'
            answer_grid[i][j] = 'GREN'

for answer_lst in answer_grid:
    for letter in answer_lst:
        if len(letter) > 1:
            continue
        for guess_lst in guess_grid:
            if letter in guess_lst:
                num_yellow += 1
                break

print(num_green)
print(num_yellow)