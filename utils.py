def add_vat(price, vat_percent=18):
    return price + (price * vat_percent / 100)
def build_username(first, last, year=""):
    username = first.lower() + "." + last.lower()
    if year:
        username += str(year)
    return username
def add_bonus(scores, bonus):
    for i in range(len(scores)):
        scores[i] = min(100, scores[i] + bonus)
def with_bonus(scores, bonus):
    new_scores = []
    for score in scores:
        new_scores.append(min(100, score + bonus))
    return new_scores
def average(*numbers):
    if not numbers:
        return 0
    return sum(numbers) / len(numbers)
def make_course(code, **details):
    course = {"code": code}
    for key, value in details.items():
        course[key] = value
    return course
