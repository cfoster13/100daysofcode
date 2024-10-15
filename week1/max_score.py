student_scores = [67, 95, 65, 45, 89, 45, 90, 95, 37, 58]

max_score = 0
index = 0

for scores in student_scores:
    if student_scores[index] > max_score:
        max_score = student_scores[index]
        index += 1

    else:
        index += 1

print(max_score)