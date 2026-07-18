import os
import numpy as np
import pandas as pd

# -----------------------------
# Create Required Folders
# -----------------------------
os.makedirs("data", exist_ok=True)

# -----------------------------
# Random Seed
# -----------------------------
np.random.seed(42)

# -----------------------------
# Sample Student Names
# -----------------------------
first_names = [
    "Aarav", "Vivaan", "Aditya", "Krishna", "Arjun",
    "Rahul", "Kiran", "Rohan", "Sai", "Aryan",
    "Priya", "Sneha", "Ananya", "Meera", "Diya",
    "Pooja", "Aisha", "Riya", "Nisha", "Ishita"
]

last_names = [
    "Sharma", "Patel", "Rao", "Kumar", "Shetty",
    "Singh", "Nair", "Gupta", "Verma", "Joshi"
]

departments = [
    "Computer Science",
    "Information Science",
    "Electronics",
    "Mechanical",
    "Civil"
]

students = []

# -----------------------------
# Generate 100 Students
# -----------------------------
for i in range(1, 101):

    student_id = f"STU{i:03d}"

    full_name = (
        np.random.choice(first_names)
        + " "
        + np.random.choice(last_names)
    )

    department = np.random.choice(departments)

    semester = np.random.randint(1, 9)

    marks = np.random.randint(35, 101, size=5)

    students.append([
        student_id,
        full_name,
        department,
        semester,
        marks[0],
        marks[1],
        marks[2],
        marks[3],
        marks[4]
    ])

# -----------------------------
# Create DataFrame
# -----------------------------
columns = [
    "Student_ID",
    "Student_Name",
    "Department",
    "Semester",
    "Subject_1",
    "Subject_2",
    "Subject_3",
    "Subject_4",
    "Subject_5"
]

df = pd.DataFrame(students, columns=columns)

# -----------------------------
# Save CSV
# -----------------------------
file_path = "data/student_results.csv"

df.to_csv(file_path, index=False)

print("=" * 60)
print("Student Dataset Generated Successfully!")
print("=" * 60)

print(df.head())

print("\nCSV saved successfully at:")
print(file_path)