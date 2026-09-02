from src.profile import intern_name, role, department, skills


def test_profile():
    assert intern_name == "Harsh Kumar"
    assert role == "Software Engineering Intern"
    assert department == "Engineering"
    assert "Python" in skills