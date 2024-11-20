def reset_score(score):

    new_score = score.copy()

    for name in new_score:
        new_score[name] = 0
    return new_score
    

game1_scores = {"Arshi": 3, "Catalina": 7, "Diego": 6}
print(reset_score(game1_scores))