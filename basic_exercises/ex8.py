students = [
    {"name": "Ana", "grades": [8.5, 7.0, 9.0]},
    {"name": "Luis", "grades": [5.0, 4.5, 6.0]},
    {"name": "Maria", "grades": [9.5, 9.0, 10.0]},
    {"name": "Pedro", "grades": [3.0, 4.0, 2.5]},
    {"name": "Sofia", "grades": [7.0, 7.5, 8.0]},
]

def averages(students):
    results = {}
    for p in students:
        if p["name"] not in results:
            mean = round(sum(p["grades"]) / len(p["grades"]), 2)
            results[p["name"]]  = mean
    return results

n = averages(students)
for name, mean in n.items():
    print(f"{name}: {mean}")