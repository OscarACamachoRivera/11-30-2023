# Student Data
students = [
    {"name": "William Torres", "id": "923-21", "score": 75},
    {"name": "Alice", "id": "101-21", "score": 89},
    {"name": "Bob", "id": "102-21", "score": 92}
]

# Print student results with IDs and scores
for student in students:
    print(f"Name: {student['name']}, ID: ({student['id']}), Score: {student['score']}")

# Calculate sum and average
suma = sum(student["score"] for student in students)
promedio = suma / len(students)

# Print overall results
print("\nSum of scores:", suma)
print("Average of scores:", promedio)

