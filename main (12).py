class Student:
  def __init__(self, name, roll_number, cgpa):
    self. name = name
    self. roll_number = roll_number
    self. cgpa = cgpa
   
def sort_students(student_list):
  sorted_students =                     sorted(student_list,
                                          key=lambda student: student.cgpa,
                                           reverse=True)
  return sorted_students
 

students = [
      Student("yuvasri", "A123", 7.8),
      Student("vaishnavi","A124",  8.9),   
      Student("monika", "A125", 9.1),
      Student("maha", "A126", 9.5),
      Student("janu", "A127",       9.8),
]

sorted_students =                       sort_students(students)

for student in sorted_students:
   print("Name: {}, Roll Number: {},     CGPA: {}". format(student.name,       student. roll_number, student.cgpa))
  
