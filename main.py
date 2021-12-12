# Problem 20

give_num = 100
answer = 1
real_answer = 0
for i in range(1,give_num+1):
    answer *= i
digit = len(str(answer))
for r in range(0,digit -1):
    real_answer += int((str(answer))[r])
print(real_answer)