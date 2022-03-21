input_line_1, input_line_2 = input(), input()

count = 0
for i in range(3, int(input_line_1)+1):
    for j in range(len(input_line_2)):
        if(j+i <= len(input_line_2)):
            string = input_line_2[j:j+i]
            if string.count('G') == 1 or string.count('H') == 1:
                count += 1
        else:
            break

print(count)