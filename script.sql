-- Table: subjects
DROP TABLE IF EXISTS subjects;
CREATE TABLE subjects(
	id INTEGER PRIMARY KEY AUTOINCREMENT,
	subject_name VARCHAR UNIQUE NOT NULL,
	teacher_id INTEGER,
	FOREIGN KEY (teacher_id) REFERENCES teachers (id)
		ON DELETE CASCADE
		ON UPDATE CASCADE 
);

-- Table: students
DROP TABLE IF EXISTS students;
CREATE TABLE students(
	id INTEGER PRIMARY KEY AUTOINCREMENT,
	student_name VARCHAR(255) NOT NULL,
	group_id INTEGER,
	FOREIGN KEY (group_id) REFERENCES students_groups (id)
		ON DELETE CASCADE
		ON UPDATE CASCADE
);

-- Table: students_groups
DROP TABLE IF EXISTS students_groups;
CREATE TABLE students_groups(
	id INTEGER PRIMARY KEY autoincrement,
	group_name varchar(255) NOT NULL
);



-- Table: teachers
DROP TABLE IF EXISTS teachers;
CREATE TABLE teachers(
	id INTEGER PRIMARY KEY autoincrement,
	teacher_name VARCHAR(255) NOT NULL
	
);



-- Table: grades
DROP TABLE IF EXISTS grades;
CREATE TABLE grades(
	id INTEGER PRIMARY KEY autoincrement,
	student_id INTEGER,
	subject_id INTEGER,
	date_of DATE NOT NULL,
	grade INTEGER NOT NULL,
	FOREIGN KEY (student_id) REFERENCES students (id)
		ON DELETE CASCADE
		ON UPDATE cascade
	FOREIGN KEY (subject_id) REFERENCES subjects (id)
		ON DELETE CASCADE
		ON UPDATE cascade
);
