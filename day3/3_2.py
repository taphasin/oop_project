def add_score(subject_score, student, subject, score):
    if student not in subject_score.keys():
        subject_score[student] = {}
    subject_score[student][subject] = score
    return subject_score

def calc_average_score(subject_score):
    result = 0
    count = 0
    for a in subject_score:
        for i in subject_score[a].values():
            result = result + i
            count += 1

        dic = {a : f'{result/count:.2f}'}
    return dic

tst = {}

print(add_score(tst,"65010710","python",100))
print(add_score(tst,"65010710","cal",50))
print(calc_average_score(tst))