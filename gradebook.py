"""
Title  : GradeBook Analyzer
Author : Chandra Prakash Mishra
Date   : 05/12/2025
"""

def print_welcome():
    print("=" * 40)
    print("      GRADEBOOK ANALYZER (CLI)")
    print("=" * 40)
    print("1. Enter student data manually")
    print("2. Load student data from CSV file")
    print("3. Exit")
    print("-" * 40)

def manual_entry():
    """
    Ask user for number of students, then read name and marks.
    Return a dictionary: {name: marks}
    """
    marks = {}
    n = int(input("How many students? "))

    for i in range(n):
        name = input(f"Enter name for student {i+1}: ")
        score = float(input(f"Enter marks for {name}: "))
        marks[name] = score

    return marks
def calculate_average(marks_dict):
    if not marks_dict:
        return 0
    total = sum(marks_dict.values())
    return total / len(marks_dict)

def calculate_median(marks_dict):
    if not marks_dict:
        return 0
    scores = sorted(marks_dict.values())
    n = len(scores)
    mid = n // 2
    if n % 2 == 1:          # for odd no
        return scores[mid]
    else:                   # for even no
        return (scores[mid - 1] + scores[mid]) / 2

def find_max_score(marks_dict):
    if not marks_dict:
        return None, None
    max_name = max(marks_dict, key=marks_dict.get)
    return max_name, marks_dict[max_name]

def find_min_score(marks_dict):
    if not marks_dict:
        return None, None
    min_name = min(marks_dict, key=marks_dict.get)
    return min_name, marks_dict[min_name]
def get_grade(score):
    if score >= 90:
        return "A"
    elif score >= 80:
        return "B"
    elif score >= 70:
        return "C"
    elif score >= 60:
        return "D"
    else:
        return "F"
def assign_grades(marks_dict):
    grades = {}
    for name, score in marks_dict.items():
        grades[name] = get_grade(score)
    return grades

def grade_distribution(grades_dict):
    dist = {"A": 0, "B": 0, "C": 0, "D": 0, "F": 0}
    for grade in grades_dict.values():
        if grade in dist:
            dist[grade] += 1
    return dist
def print_grade_summary(dist):
    print("\nGrade Distribution:")
    for grade, count in dist.items():
        print(f"{grade}: {count} student(s)")
def pass_fail_lists(marks_dict):
    passed_students = [name for name, score in marks_dict.items() if score >= 40]
    failed_students = [name for name, score in marks_dict.items() if score < 40]

    print("\nPass/Fail Summary:")
    print(f"Passed ({len(passed_students)}): {', '.join(passed_students) if passed_students else 'None'}")
    print(f"Failed ({len(failed_students)}): {', '.join(failed_students) if failed_students else 'None'}")
def print_results_table(marks_dict, grades_dict):
    print("\nName\t\tMarks\tGrade")
    print("-" * 32)
    for name, score in marks_dict.items():
        grade = grades_dict.get(name, "-")
        print(f"{name:10}\t{score:5.1f}\t{grade}")
def run_analysis(marks):
    if not marks:
        print("No data to analyze.")
        return

    avg = calculate_average(marks)
    median = calculate_median(marks)
    max_name, max_score = find_max_score(marks)
    min_name, min_score = find_min_score(marks)

    grades = assign_grades(marks)
    dist = grade_distribution(grades)

    print_results_table(marks, grades)
    print("\nSummary Statistics:")
    print(f"Average score: {avg:.2f}")
    print(f"Median score : {median:.2f}")
    print(f"Highest score: {max_score} ({max_name})")
    print(f"Lowest score : {min_score} ({min_name})")

    print_grade_summary(dist)
    pass_fail_lists(marks)

    # CSV export (bonus)
    choice = input("\nDo you want to export the results to a CSV file? (y/n): ").lower()
    if choice == "y":
        export_to_csv(marks, grades)


def main():
    while True:
        print_welcome()
        choice = input("Enter your choice (1-3): ")

        if choice == "1":
            marks = manual_entry()
            run_analysis(marks)

        elif choice == "2":
            marks = load_from_csv()
            run_analysis(marks)

        elif choice == "3":
            print("Exiting GradeBook Analyzer. Goodbye!")
        input("\nPress Enter to return to the main menu...")


import csv

def load_from_csv():
    """
    Load student data from a CSV file.
    Return a dictionary: {name: marks}
    """
    marks = {}
    filename = input("Enter CSV filename to load (e.g. grades.csv): ").strip()
    
    try:
        with open(filename, "r") as f:
            reader = csv.reader(f)
            next(reader)  # skip header row
            for row in reader:
                if len(row) >= 2:
                    name = row[0].strip()
                    score = float(row[1].strip())
                    marks[name] = score
        print(f"Data loaded successfully from '{filename}'.")
    except FileNotFoundError:
        print(f"File '{filename}' not found.")
    except Exception as e:
        print("Something went wrong while reading the file:", e)
    
    return marks


def export_to_csv(marks_dict, grades_dict):
    """
    Export the final results table (Name, Marks, Grade) to a CSV file.
    """
    if not marks_dict:
        print("No data available to export.")
        return

    filename = input("\nEnter filename to save (e.g. results.csv): ").strip()
    if filename == "":
        filename = "gradebook_output.csv"

    try:
        with open(filename, "w", newline="") as f:
            writer = csv.writer(f)
            # header row
            writer.writerow(["Name", "Marks", "Grade"])
            # data rows
            for name, score in marks_dict.items():
                grade = grades_dict.get(name, "-")
                writer.writerow([name, score, grade])

        print(f"Results exported successfully to '{filename}'.")
    except Exception as e:
        print("Something went wrong while saving the file:", e)


if __name__ == "__main__":
    main()

