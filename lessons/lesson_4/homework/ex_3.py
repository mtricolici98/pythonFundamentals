persons = []
scores = []
for time in range(int(input('How many times ? '))):
    name = input('Name ? ')
    score = float(input('Score ? '))
    persons.append(name)
    scores.append(score)

# Solution 1
high_score = max(scores)  # Get high score value
# Find index of high score value and get person at that index
person_with_high_score = persons[scores.index(high_score)]
print(f"{person_with_high_score} are cel mai mare scor")

# Solution 2
max_index = -1  # Index of highest score unknown
max_score = 0  # Max score inital value
for a in range(len(persons)):
    if scores[a] > max_score:
        max_index = a
        max_score = scores[a]
person_with_high_score = persons[max_index]
print(f"{person_with_high_score} are cel mai mare scor")
