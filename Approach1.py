import random

horses = list(range(25))
for horse in horses:
    horse = round(random.random(), 2)

first = 0
second = 0
third = 0

for i in range(5):
    if (horses[i] > first):
        third = second
        second = first
        first = horses[i]
    elif (horses[i] > second):
        third = second
        second = horses[i]
    elif (horses[i] > third):
        third = horses[i]

offset = 4
for i in range(10):
    for j in range(2):
        index = offset + j
        if (horses[index] > first):
            third = second
            second = first
            first = horses[index]
        elif (horses[index] > second):
            third = second
            second = horses[index]
        elif (horses[index] > third):
            third = horses[index]
    offset += 2

print(first)
print(second)
print(third)