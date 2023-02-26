import sqlite3

def execute_query(sql: str) -> list:
    with sqlite3.connect('student-progress.db') as con:
        cur = con.cursor()
        cur.execute(sql)
        return cur.fetchall()

# Найти 5 студентов с наибольшим средним баллом по всем предметам.
sql1 = """
SELECT AVG(g.grade), s.student_name
FROM grades as g
LEFT JOIN students as s ON g.student_id = s.id
GROUP BY s.student_name
ORDER BY AVG(g.grade) DESC
LIMIT 6;
"""

# print(execute_query(sql))

# Найти студента с наивысшим средним баллом по определенному предмету.
sql2 = """
SELECT std.student_name, sbj.subject_name, AVG(g.grade)
FROM students as std
LEFT JOIN grades as g ON g.student_id = std.id
LEFT JOIN subjects as sbj ON g.subject_id = sbj.id
WHERE  sbj.subject_name = 'statistics'
GROUP BY std.student_name
ORDER BY AVG(g.grade) DESC
LIMIT 1;
"""
# print(execute_query(sql))

# Найти средний балл в группах по определенному предмету.
sql3 = """
SELECT std.group_id, sbj.subject_name, AVG(g.grade)
FROM students as std
LEFT JOIN grades as g ON g.student_id = std.id
LEFT JOIN subjects as sbj ON g.subject_id = sbj.id
WHERE sbj.subject_name = "trigonometry"
GROUP BY std.group_id;
 
        """ 
# print(execute_query(sql))
# Найти средний балл на потоке (по всей таблице оценок).
sql4 = """
SELECT AVG(grade) FROM grades;
"""
# print(execute_query(sql))

# Найти какие курсы читает определенный преподаватель.
sql5 = """
SELECT tchr.teacher_name, sbj.subject_name
FROM teachers as tchr
LEFT JOIN subjects as sbj ON sbj.teacher_id = tchr.id
WHERE tchr.teacher_name = "Bruce Drake";
"""
# print(execute_query(sql))

# Найти список студентов в определенной группе.
sql6 = """
SELECT std.student_name
FROM students as std
WHERE std.group_id = 1;
"""
# print(execute_query(sql))
# Найти оценки студентов в отдельной группе по определенному предмету.
sql7= """
SELECT grds.grade
FROM grades as grds
LEFT JOIN students as std ON std.group_id = 3
WHERE grds.subject_id = 1
;

"""
# print(execute_query(sql))

# Найти средний балл, который ставит определенный преподаватель по своим предметам.
sql8= """
SELECT tchrs.teacher_name , sbj.subject_name, AVG(grds.grade)
FROM teachers as tchrs 
LEFT JOIN subjects as sbj ON tchrs.id = sbj.teacher_id
LEFT JOIN grades as grds ON grds.subject_id = sbj.id
WHERE tchrs.teacher_name = "Jessica Blair PhD"
GROUP BY sbj.subject_name
;

"""
# print(execute_query(sql))

# Найти список курсов, которые посещает определенный студент.

sql9 = """
SELECT grds.student_id, sbj.subject_name
FROM subjects as sbj
LEFT JOIN grades as grds ON sbj.id = grds.subject_id
WHERE grds.student_id = 4                               --student with id 4
GROUP BY sbj.subject_name
"""

# print(execute_query(sql))

# Список курсов, которые определенному студенту читает определенный преподаватель.
sql10 = """
SELECT sbj.subject_name, tchrs.teacher_name
FROM subjects as sbj
LEFT JOIN grades as grds ON sbj.id = grds.subject_id
LEFT JOIN teachers as tchrs ON tchrs.id = sbj.teacher_id
WHERE grds.student_id = 1 AND tchrs.teacher_name = 'Bruce Drake'
GROUP BY sbj.subject_name;
"""

sql_d = {'sql1': sql1,'sql2': sql2,'sql3': sql3,'sql4': sql4,'sql5': sql5,'sql6': sql6,'sql7': sql7,'sql8': sql8,'sql9': sql9,'sql10': sql10,}

new_input = input('''1.Найти 5 студентов с наибольшим средним баллом по всем предметам.
2.Найти студента с наивысшим средним баллом по определенному предмету.
3.Найти средний балл в группах по определенному предмету.
4.Найти средний балл на потоке (по всей таблице оценок).
5.Найти какие курсы читает определенный преподаватель.
6.Найти список студентов в определенной группе.
7.Найти оценки студентов в отдельной группе по определенному предмету.
8.Найти средний балл, который ставит определенный преподаватель по своим предметам.
9.Найти список курсов, которые посещает определенный студент.
10.Список курсов, которые определенному студенту читает определенный преподаватель.
0 - EXIT!''')

while new_input != '0':
        print(execute_query(sql_d[f'sql{new_input}']))
        new_input  = input('>')
        