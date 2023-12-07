def add_score(subject_score, subject, score):
    subject_score[subject] = score
    return subject_score


def calc_average_score(subject_score):
    result = 0
    for i in subject_score.values():
        result = result + i
    
    str = f'{result/len(subject_score):.2f}'
    return str
    
tst = {}

print(add_score(tst,"python",20))
