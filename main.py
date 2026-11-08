import csv
from pathlib import Path

# Student submission information
STUDENT_NAME = "Chukwunoso Excel Munachinso"
MATRIC_NUMBER = "24/14500"
LEVEL = "300 Level"
DEPARTMENT = "Computer Science"
INSTITUTION = "Caleb University"


def display_students():
    """Read and display fictional student records from students.csv."""
    csv_file = Path(__file__).with_name("students.csv")

    print("ASSIGNMENT 3: FICTIONAL STUDENT DATASET")
    print("=" * 60)
    print(f"Name: {STUDENT_NAME}")
    print(f"Matric Number: {MATRIC_NUMBER}")
    print(f"Level: {LEVEL}")
    print(f"Department: {DEPARTMENT}")
    print(f"Institution: {INSTITUTION}")
    print("=" * 60)

    try:
        with csv_file.open("r", newline="", encoding="utf-8") as file:
            reader = csv.DictReader(file)
            records = list(reader)

        if not records:
            print("No student records found.")
            return

        print("\nFICTIONAL STUDENT RECORDS")
        print("-" * 92)
        print(
            f"{'Student ID':<12}"
            f"{'Department':<27}"
            f"{'Level':<9}"
            f"{'Attendance (%)':<19}"
            f"{'Average Score':<15}"
        )
        print("-" * 92)

        for student in records:
            print(
                f"{student['Student ID']:<12}"
                f"{student['Department']:<27}"
                f"{student['Level']:<9}"
                f"{student['Attendance Percentage']:<19}"
                f"{student['Average Examination Score']:<15}"
            )

        print("-" * 92)
        print(f"Total students: {len(records)}")

    except FileNotFoundError:
        print("Error: students.csv was not found. Keep it in the same folder as main.py.")
    except (KeyError, csv.Error) as error:
        print(f"Error reading the dataset: {error}")


if __name__ == "__main__":
    display_students()
