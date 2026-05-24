import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


data = {
    "Name": [
        "Rahul","Anu","Kiran","Priya","Ravi","Sneha","Arjun","Pooja","Vijay","Neha"
    ],

    "Math": [
        78,92,65,88,45,73,95,67,81,56
    ],

    "Science": [
        85,89,70,91,50,68,98,72,79,60
    ],

    "English": [
        80,94,60,87,40,75,90,65,83,58
    ]
}
df=pd.DataFrame(data)
df.to_csv("student.csv", index=False)
print("student.csv created successfully!")

df=pd.read_csv("student.csv")
print("\n =======STUDENT DATASET======\n")
print(df)

df["Total"]=(
    df["Math"] + df["Science"] + df["English"]
)

df["Average"]=df["Total"] / 3

df["Result"] = np.where(
    df["Average"] >= 50,
    "Pass",
    "Fail"
)

print("\n==========UPDATED DATASET========\n")
print(df)

topper=df.loc[df["Total"].idxmax()]

print("\n=========TOPPER STUDENT=======\n")
print(topper)

class_average=df["Average"].mean()

print("\n==========CLASS AVERAGE=========\n")
print(class_average)

failed_students = df[df["Result"] == "Fail"]

print("\n================ FAILED STUDENTS ================\n")
print(failed_students)

# SUBJECT-WISE AVERAGE
math_avg = df["Math"].mean()
science_avg = df["Science"].mean()
english_avg = df["English"].mean()

print("\n================ SUBJECT AVERAGES ================\n")

print("Math Average :", math_avg)
print("Science Average :", science_avg)
print("English Average :", english_avg)

# SORT STUDENTS BY TOTAL MARKS
sorted_students = df.sort_values(
    by="Total",
    ascending=False
)

print("\n================ RANKED STUDENTS ================\n")
print(sorted_students)

# FILTER STUDENTS WITH AVERAGE > 80

excellent_students = df[df["Average"] > 80].sort_values(
    by="Average",
    ascending=False

)

print("\n================ EXCELLENT STUDENTS ================\n")
print(excellent_students)


# BAR CHART - TOTAL MARKS
plt.figure(figsize=(10, 5))

plt.bar(
    df["Name"],
    df["Total"]
)

plt.title("Student Total Marks")
plt.xlabel("Student Names")
plt.ylabel("Total Marks")
plt.show()

# SUBJECT-WISE AVERAGE BAR CHART

subjects = [
    "Math",
    "Science",
    "English"
]

subject_averages = [
    math_avg,
    science_avg,
    english_avg
]
plt.figure(figsize=(7, 5))

plt.bar(
    subjects,
    subject_averages
)

plt.title("Subject Wise Average")
plt.xlabel("Subjects")
plt.ylabel("Average Marks")

plt.show()

# HISTOGRAM - AVERAGE DISTRIBUTION

plt.figure(figsize=(7,5))
plt.hist(df["Average"],
        bins=15
)
plt.title("Average Marks Distribution")
plt.xlabel("Average Marks")
plt.ylabel("Number of Students")

plt.show()

# BOX PLOT

plt.figure(figsize=(7, 5))

plt.boxplot([
    df["Math"],
    df["Science"],
    df["English"]
])

plt.xticks(
    [1, 2, 3],
    ["Math", "Science", "English"]
)

plt.title("Subject Marks Boxplot")

plt.show()


# PIE CHART - PASS VS FAIL
result_counts = df["Result"].value_counts()

plt.figure(figsize=(6, 6))

plt.pie(
    result_counts,
    labels=result_counts.index,
    autopct="%1.1f%%"
)

plt.title("Pass vs Fail")

plt.show()

# LINE CHART - STUDENT AVERAGES

plt.figure(figsize=(10,5))
plt.plot(
    df["Name"],
    df["Average"],
    marker='o'
)

plt.title("Student Average Marks")
plt.xlabel("Students")
plt.ylabel("Average Marks")

plt.grid(True)

plt.show()

# SCATTER PLOT
plt.figure(figsize=(7, 5))

plt.scatter(
    df["Math"],
    df["Science"]
)

plt.title("Math vs Science Marks")
plt.xlabel("Math Marks")
plt.ylabel("Science Marks")

plt.show()

df.to_csv("final_student_report.csv",index=False)
print("\nfinal_student_report.csv saved successfully!")