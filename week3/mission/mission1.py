def get_average(scores):
    """점수 리스트를 받아 평균을 반환하는 함수"""
    if not scores:
        return 0
    return sum(scores) / len(scores)

def get_grade(avg_score):
    """평균 점수를 받아 학점을 반환하는 함수"""
    if avg_score >= 90:
        return "A"
    elif avg_score >= 80:
        return "B"
    elif avg_score >= 70:
        return "C"
    elif avg_score >= 60:
        return "D"
    else:
        return "F"


scores_list = []  
while True:
    score_input = input("점수를 입력하세요 (종료하려면 'q' 입력): ")
    
    if score_input == 'q':
        break
    
    scores_list.append(int(score_input)) # input은 항상 str으로 받기 때문에, int로 변환


average = get_average(scores_list)
grade = get_grade(average)

print("---")
print(f"평균 점수: {average:.2f}")
print(f"최종 학점: {grade}")