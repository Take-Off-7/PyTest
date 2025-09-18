import pytest
from unittest.mock import Mock
from source.school import Classroom, Teacher, Student, TooManyStudents


# ---------------- Fixtures ----------------
@pytest.fixture
def hogwarts_teacher():
    return Teacher("Professor McGonagall")


@pytest.fixture
def hogwarts_students():
    return [
        Student("Harry Potter"),
        Student("Hermione Granger"),
        Student("Ron Weasley"),
    ]


@pytest.fixture
def transfiguration_class(hogwarts_teacher, hogwarts_students):
    return Classroom(
        teacher=hogwarts_teacher,
        students=hogwarts_students,
        course_title="Transfiguration"
    )


# ---------------- Tests ----------------
def test_initial_setup(transfiguration_class):
    assert transfiguration_class.course_title == "Transfiguration"
    assert len(transfiguration_class.students) == 3
    assert transfiguration_class.teacher.name == "Professor McGonagall"


@pytest.mark.parametrize("student_name", ["Neville Longbottom", "Draco Malfoy"])
def test_add_student(transfiguration_class, student_name):
    new_student = Student(student_name)
    transfiguration_class.add_student(new_student)
    assert any(s.name == student_name for s in transfiguration_class.students)


def test_add_too_many_students(transfiguration_class):
    for i in range(7):  # Fill to 10 total
        transfiguration_class.add_student(Student(f"Extra Student {i}"))

    with pytest.raises(TooManyStudents):
        transfiguration_class.add_student(Student("Overflow Student"))


def test_remove_student(transfiguration_class):
    transfiguration_class.remove_student("Hermione Granger")
    names = [s.name for s in transfiguration_class.students]
    assert "Hermione Granger" not in names


def test_change_teacher_with_mock(transfiguration_class):
    fake_teacher = Mock()
    fake_teacher.name = "Professor Snape"

    transfiguration_class.change_teacher(fake_teacher)

    assert transfiguration_class.teacher.name == "Professor Snape"
