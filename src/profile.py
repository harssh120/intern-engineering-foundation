intern_name = "Harsh Kumar"
role = "Software Engineering Intern"
department = "Engineering"

skills = [
    "Python",
    "Git",
    "GitHub"
]


def print_profile():
    print("Intern Name:", intern_name)
    print("Role:", role)
    print("Department:", department)
    print("Skills:", ", ".join(skills))


print_profile()