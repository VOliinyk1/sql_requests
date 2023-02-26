from datetime import datetime
import faker
from random import randint, choice
import sqlite3

NUM_STUDENTS = 45
NUM_TEACHERS = 4
NUM_SUBJECTS = 7
NUM_GROUPS = 3
NUM_GRADES = 20

def generate_fake_data(number_students, number_teachers):
    fake_students = []
    fake_teachers = []
    subjects = ['trigonometry', 'biology', 'calculus', 'data analysis', 'statistics', 'philosofy', 'algorithms']
    groups = ['first', 'second', 'third']

    fake_data = faker.Faker()

    for _ in range(number_students):
        fake_students.append(fake_data.name())
    
    for _ in range(number_teachers):
        fake_teachers.append(fake_data.name())
    
    return fake_students, fake_teachers, subjects, groups
    
def prepare_data(students, teachers, subjects, groups):
    for_students = []
    for stud in students:
        for_students.append((stud, choice((range(1, NUM_GROUPS+1)))))
    
    for_teachers = []
    for tchr in teachers:
        for_teachers.append((tchr, ))

    for_subjects = []
    for sub in subjects:
        for_subjects.append((sub, choice((range(1, NUM_TEACHERS+1)))))
    
    for_groups = []
    for grp in groups:
        for_groups.append((grp, ))

    for_grades = []
    for std_id in range(1, NUM_STUDENTS+1):
        for _ in range(NUM_GRADES):
            grade_date = datetime(2022, choice((range(1, 12+1))), randint(1, 25)).date()
            for_grades.append((std_id, choice((range(1, NUM_SUBJECTS+1))), grade_date, choice((range(1, 5+1)))))
    return for_students, for_teachers, for_subjects, for_groups, for_grades

def insert_data_to_db(students, teachers, subjects, groups, grades):
    with sqlite3.connect('student-progress.db') as con:
        cur = con.cursor()

        sql_to_students = """INSERT INTO STUDENTS(student_name, group_id)
                                VALUES (?, ?)"""
        cur.executemany(sql_to_students, students)

        sql_to_teachers = """INSERT INTO TEACHERS(teacher_name)
                                VALUES(?)"""
        cur.executemany(sql_to_teachers, teachers)

        sql_to_subjects = """INSERT INTO SUBJECTS(subject_name, teacher_id)
                                VALUES(?, ?)"""
        cur.executemany(sql_to_subjects, subjects)

        sql_to_groups = """INSERT INTO STUDENTS_GROUPS(group_name)
                                VALUES(?)"""
        cur.executemany(sql_to_groups, groups)

        sql_to_grades = """INSERT INTO GRADES(student_id, subject_id, date_of, grade)
                                VALUES(?, ?,?,?)"""
        cur.executemany(sql_to_grades, grades)


if __name__ == '__main__':
    insert_data_to_db(*prepare_data(*generate_fake_data(NUM_STUDENTS, NUM_TEACHERS)))
    