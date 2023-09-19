import random

horses = list(range(26))
for i in range(len(horses)):
    horses[i] = round(random.random(), 2)

print(horses)

first = 0
second = 0
third = 0

firsts = [0, 0, 0, 0, 0]
seconds = [0, 0, 0, 0, 0]
thirds = [0, 0, 0, 0, 0]


offset = 5
for i in range(5):
    for j in range(5):
        index = offset*i + j
        if (horses[index] > firsts[i]):
            thirds[i] = seconds[i]
            seconds[i] = firsts[i]
            firsts[i] = horses[index]
        elif (horses[index] > seconds[i]):
            thirds[i] = seconds[i]
            seconds[i] = horses[index]
        elif (horses[index] > thirds[i]):
            thirds[i] = horses[index]


first = firsts.pop(firsts.index(max(firsts)))

final = []
final.append(firsts.pop(firsts.index(max(firsts))))
final.append(firsts.pop(firsts.index(max(firsts))))
final.append(seconds.pop(seconds.index(max(seconds))))
final.append(seconds.pop(seconds.index(max(seconds))))
final.append(thirds.pop(thirds.index(max(thirds))))

second = final.pop(final.index(max(final)))
third = final.pop(final.index(max(final)))

print(first)
print(second)
print(third)