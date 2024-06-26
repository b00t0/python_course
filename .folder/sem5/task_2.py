"""
Хакер Василий получил доступ к классному журналу и хочет заменить все свои минимальные оценки 
на максимальные. Напишите программу, которая заменяет оценки Василия, но наоборот: все максимальные – на минимальные.
"""

scores = [1, 3, 3, 3, 4]

def change_scores(scores, index=0, max_score=max(scores), min_score=min(scores)):
    if index < len(scores):
        if scores[index] == max_score:
            scores[index] = min_score
        change_scores(scores, index + 1)
    return scores

print(*change_scores(scores))