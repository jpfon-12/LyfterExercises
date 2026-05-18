
def get_average_score(scores):
    return (scores["spanish_score"] + scores["science_score"] + scores["history_score"]) / 3 

def is_student_exempted(scores):
    return scores["average_score"] > 70

students = [
    {
    "name": "Juan",
    "spanish_score": 75,
    "science_score": 56,
    "history_score": 54,
    },
    {
    "name": "Sofia",
    "spanish_score": 64,
    "science_score": 56,
    "history_score": 98,
    },
    {
    "name": "Paul",
    "spanish_score": 32,
    "science_score": 75,
    "history_score": 79,
    }
]

for student in students:
    student["average_score"] = get_average_score(student)
    student["is_exempted"] = is_student_exempted(student)
    print(f"El estudiante {student["name"]} tiene como resultado de eximido: {student["is_exempted"]}")

#juan_scores["average_score"] = (juan_scores["spanish_score"] + juan_scores["science_score"] + juan_scores["history_score"]) / 3 

#juan_scores["is_exempted"] = juan_scores["average_score"] > 70







# juan_scores["average_score"] = get_average_score(juan_scores)
# juan_scores["is_exempted"] = is_student_exempted(juan_scores)



# for key, value in juan_scores.items():
#     print(key, value)