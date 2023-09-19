# [Mechanical Horse Logical Puzzle🔗](https://www.youtube.com/watch?v=i-xqRDwpilM)

#### Recently I encountered a fun problem that is meant to be a little logical puzzle, but I thought it would be fun to code an answer.

```
There are 25 mechanical horses and a single racetrack. Each horse completes the track in a pre-programmed time, and the horses all have different finishing times, unknown to you. You can race 5 horses at a time. After a race is over, you get a printout with the order the horses finished, but not the finishing times of the horses. What is the minimum number of races you need to identify the fastest 3 horses?
```

#### This is a fun experiment, because every operation you do regarding the horses must be limited to 5 horses. I encourage others to try it as it was very fun.

# First Approach

## Code

```python
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
```

## Explanation

To understand what's going on here, we have to look at what each section of code is actually doing. 

### First For Loop
```python
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
```
In this block of code, the first 5 horses are raced, and the top 3 are saved.

### Second For Loop

```python
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
```
This may be the more confusing section. First, let me explain why I chose to race the first 5 horses separately.

#### The reason I decided upon this was how I initially solved the problem:

1. Race the first 5 horses and record the top 3
1. Race the top 3 horses against 2 new horses
1. Repeat until all horses raced

Now, what is happening in the second for loop? Well, after offset is set to 5, the next two horses "race" the top three horses. This happens 10 times because after the first 5 horses race, there are 20 horses left, which can be checked in 10 "races".

For those who did not understand anything mentioned above, the total number of races is 11

- 1 for the first 5 horses
- 10 for the remaining 20 horses

# Second Approach

## Code

```python
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
```

#### This implementation solves the problem in the fastest number of races.

## Explanation

Finding the fastest horse is quite easy
1. Race 5 groups of 5 horses to determine the fastest and second fastest horse in each group.
1. Race the 5 fastest horses to find the fastest

However, to find the second and third fastest, isn't as easy. Let's consider what it means to be the second or third fastest.

*Get ready for some confusion.*

To be second means you only had one horse that beat you. Which can only be the second fastest horse of the fastest horses, or the horse that came second to the fastest horse in one of the first five races.

To be third means you only had two horses that beat you. Which can only be these three horses:
1. The third fastest horse of the fastest horses
1. The horse that came second to the second fastest horse of the fastest horses
1. The horse that came third to the fastest of the fastest horses

Conveniently, these five horses can all be raced at once to determine the second and third fastest horses.

I'm sure you're thoroughly confused by now, and only wish to know the minimum number of races required. It's 7.

---

Thank you to Mind Your Decisions for this lovely puzzle. If you would like to attempt the problem, or hear a much better explanation, go check out their video attached at the title.