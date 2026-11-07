def add_bonus(scores, bonus):
    for i in range(len(scores)):
        scores[i] = min(100, scores[i] + bonus)
def with_bonus(scores, bonus):
    new_scores = scores[:]
    add_bonus(new_scores, bonus)
    return new_scores
scores = [70, 95, 88, 100]
print(with_bonus(scores, 10))
print(scores)
add_bonus(scores[:], 10)
print(scores)
add_bonus(scores, 10)
print(scores)
