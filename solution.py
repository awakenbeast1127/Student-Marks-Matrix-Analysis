# Case Study 42: Student Marks Matrix Analysis

def analyse_marks(student_names, subject_names, marks):
    if len(marks) != len(student_names):
        raise ValueError("There must be one marks row per student.")
    if not marks or any(len(row) != len(subject_names) for row in marks):
        raise ValueError("Every student row must contain one mark per subject.")

    for row in marks:
        for score in row:
            if score < 0 or score > 100:
                raise ValueError("Marks must be between 0 and 100.")

    student_stats = []
    for index in range(len(student_names)):
        total = sum(marks[index])
        average = total / len(subject_names)
        student_stats.append((student_names[index], total, average))

    subject_averages = []
    weak_subjects = []
    for column in range(len(subject_names)):
        total = 0
        for row in marks:
            total += row[column]
        average = total / len(student_names)
        subject_averages.append((subject_names[column], average))
        if average < 50:
            weak_subjects.append(subject_names[column])

    highest_average = max(item[2] for item in student_stats)
    toppers = [item[0] for item in student_stats if item[2] == highest_average]
    return student_stats, subject_averages, toppers, weak_subjects


def main():
    students = ["Aisha", "Bilal", "Zoya", "Hamza"]
    subjects = ["Python", "Maths", "Physics"]
    marks = [
        [85, 78, 90],
        [72, 88, 69],
        [91, 94, 89],
        [45, 42, 48],
    ]
    student_stats, subject_stats, toppers, weak = analyse_marks(students, subjects, marks)

    print("STUDENT MARKS MATRIX ANALYSIS")
    print("-" * 48)
    print("Student-wise results:")
    for name, total, average in student_stats:
        print(f"{name:10} Total={total:3} Average={average:.2f}")
    print("\nSubject-wise averages:")
    for subject, average in subject_stats:
        print(f"{subject:10} {average:.2f}")
    print(f"Top performer(s): {', '.join(toppers)}")
    print(f"Subjects below 50 average: {weak if weak else 'None'}")


if __name__ == "__main__":
    main()
