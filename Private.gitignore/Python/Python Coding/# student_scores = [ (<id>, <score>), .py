# student_scores = [ (<id>, <score>), ... ]
student_scores = [(6, 89), (9, 70), (2, 53), (2, 58), (9, 80), (6, 100), (2, 40), (6, 95), (9, 90)]
 
def highFive(student_scores):
     
    tracker = {}
     
    for student, score in student_scores:
         
        if student in tracker:
             
            tracker[student].append(score)
         
        else:
            tracker[student] = [score]
     
     
    topScoreAvgList = []
     
    for student,scores in tracker.items():
         
            # Reverse sort so that we can easily sum the first 5 indexes via slicing
            scores.sort(reverse=True)
             
            # Integer divison operator not necessary (float is fine)
            topScoreAvgList.append([student, sum(scores[:5]) // 5])
             
     
    # Ask them if they know what a lambda is - although by default, the sort method uses the first element in a nested list
    topScoreAvgList.sort()
             
    return topScoreAvgList

student_scores = [(6, 89), (9, 70), (2, 53), (2, 58), (9, 80), (6, 100), (2, 40), (6, 95), (9, 90)]
print(highFive(student_scores))