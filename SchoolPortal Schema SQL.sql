CREATE TABLE `Students` (
  `Students_Name` TEXT,
  `Student_Id` integer,
  `Student_Courses` TEXT,
  `Student_Email` TEXT
);

CREATE TABLE `Lecturers` (
  `Lecturers_Name` TEXT,
  `Lecturer_Id` integer,
  `Lecturer_Email` text
);

CREATE TABLE `College` (
  `Faculty` text,
  `Faculty_Id` integer
);

CREATE TABLE `Marks` (
  `Marks_Id` integer,
  `GPA` integer
);

CREATE TABLE `University` (
  `Student1_Id` integer,
  `Marks1_Id` integer,
  `Lecturer1_Id` integer,
  `Faculty1_Id` integer
);

ALTER TABLE `Students` ADD FOREIGN KEY (`Student_Id`) REFERENCES `University` (`Student1_Id`);

ALTER TABLE `Lecturers` ADD FOREIGN KEY (`Lecturer_Id`) REFERENCES `University` (`Lecturer1_Id`);

ALTER TABLE `College` ADD FOREIGN KEY (`Faculty_Id`) REFERENCES `University` (`Faculty1_Id`);

ALTER TABLE `Marks` ADD FOREIGN KEY (`Marks_Id`) REFERENCES `University` (`Marks1_Id`);
