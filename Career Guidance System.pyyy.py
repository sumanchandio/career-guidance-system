import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

print("===== Advanced Career Guidance System =====")

# Function for career suggestion
def suggest_career(marks, interest):
    if interest == "science":
        if marks >= 80:
            return "Doctor / Engineer"
        elif marks >= 60:
            return "Computer Science / Lab Technician"
        else:
            return "Diploma in Science"

    elif interest == "commerce":
        if marks >= 70:
            return "CA / BBA / Accounting"
        else:
            return "Office Management / Sales"

    elif interest == "arts":
        if marks >= 60:
            return "Teacher / Media / CSS"
        else:
            return "Fine Arts / Social Work"
    else:
        return "Invalid Interest"

# Lists to store data
names = []
marks_list = []
interests = []
careers = []

# Number of students
n = int(input("Enter number of students:"))

# Input data
for i in range(n):
    print(f"\nStudent {i+1}")
    name = input("Enter name: ")
    marks = int(input("Enter percentage marks: "))
    interest = input("Enter interest (science/arts/commerce): ").lower()

    career = suggest_career(marks, interest)

    names.append(name)
    marks_list.append(marks)
    interests.append(interest)
    careers.append(career)

# NumPy analysis
marks_array = np.array(marks_list)

avg_marks = np.mean(marks_array)
max_marks = np.max(marks_array)
min_marks = np.min(marks_array)

# Pandas DataFrame
df = pd.DataFrame({
    "Name": names,
    "Marks": marks_array,
    "Interest": interests,
    "Suggested Career": careers
})

print("\n===== Student Career Report =====")
print(df)

print("\n===== Marks Analysis =====")
print("Average Marks:", avg_marks)
print("Highest Marks:", max_marks)
print("Lowest Marks:", min_marks)

# Save CSV
df.to_csv("career_guidance_report.csv", index=False)
print("\nReport saved as career_guidance_report.csv")

# =====================
# Matplotlib Graphs
# =====================

# Bar chart of marks
plt.figure()
plt.bar(names, marks_array)
plt.xlabel("Students")
plt.ylabel("Marks")
plt.title("Students Marks Comparison")
plt.show()

# Line chart
plt.figure()
plt.plot(names, marks_array, marker='o')
plt.xlabel("Students")
plt.ylabel("Marks")
plt.title("Marks Trend")
plt.show()
