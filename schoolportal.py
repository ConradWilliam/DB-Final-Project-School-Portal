import csv

from cs50 import SQL 

open("schoolportal.db","w").close()

db = SQL("sqlite:///schoolportal.db")


db.execute("CREATE TABLE Students (Student_Id INTEGER, Students_Name TEXT, Student_Courses TEXT, Student_Email TEXT, PRIMARY KEY(Student_Id))")

db.execute("CREATE TABLE University(Student1_Id INTEGER, Lecturer1_Id INTEGER, Faculty1_Id INTEGER, Marks1_Id INTEGER, FOREIGN KEY(Student1_Id) REFERENCES Students(Student_Id), FOREIGN KEY(Marks1_Id) REFERENCES Marks(Marks_Id), FOREIGN KEY(Lecturer1_Id) REFERENCES Lecturers(Lecturer_Id), FOREIGN KEY(Faculty1_Id) REFERENCES College(Faculty_Id))")

db.execute("CREATE TABLE Lecturers(Lecturer_Id INTEGER, Lecturers_Name TEXT, Lecturer_Email TEXT, PRIMARY KEY(Lecturer_Id))")

db.execute("CREATE TABLE Marks(Marks_Id INTEGER, GPA INTEGER,PRIMARY KEY(Marks_Id))")

db.execute("CREATE TABLE College(Faculty TEXT, Faculty_Id INTEGER, PRIMARY KEY(Faculty_Id))")





with open("portal.csv","r") as file:
    reader = csv.DictReader(file)

    for row in reader:
        StudentName = row["Students_Name"].strip().capitalize()
        StudentCourse = row["Student_Courses"].strip().capitalize()
        StudentEmail= row["Student_Email"].strip().capitalize()
        id = db.execute("INSERT INTO Students(Students_Name,Student_Courses,Student_Email) VALUES (?,?,?)",StudentName,StudentCourse,StudentEmail)

        LecturerEmail= row["Lecturer_Email"].strip().capitalize()
        LecturersName= row["Lecturers_Name"].strip().capitalize()
        id = db.execute("INSERT INTO Lecturers(Lecturer_Email,Lecturers_Name) VALUES (?,?)",LecturerEmail,LecturersName)

        
        Progress= row["GPA"].strip().capitalize()
        id = db.execute("INSERT INTO Marks(GPA) VALUES (?)",Progress)

        College = row["Faculty"].strip().capitalize()
        id = db.execute("INSERT INTO College(Faculty) VALUES (?)",College)
       

        id = db.execute("INSERT INTO University(Marks1_Id,Student1_Id,Lecturer1_Id,Faculty1_Id) VALUES ((SELECT Marks_Id FROM Marks WHERE GPA = ?),(SELECT Student_Id FROM Students WHERE Student_Courses = ?),(SELECT Lecturer_Id FROM Lecturers WHERE Lecturers_Name = ?),(SELECT Faculty_Id FROM College WHERE Faculty = ?))",Progress,StudentCourse,LecturersName,College)

    
        
        

        


        