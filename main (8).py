"""
Implement a function called sort_students that takes a list of student objects as input and sorts the 
list based on their CGPA (Cumulative Grade Point Average) in descending order. Each student object
has the following attributes: name (string), roll_number (string), and cgpa (float). Test the function
with different input lists of students.
"""

class Student:  
 
  def __init__(self, name, roll_number, cgpa):

    self.roll_number = roll_number
    self.cgpa = cgpa

  def sort_student(student_list):
  # sort the list of students in descending order of CGPA
    sorted_students = sorted(student _list,
                            key=Lambda student: student.cgpa
  reverse=True)
# syntax - Lambda arg:exp
return sorted_students


# Example usage:

student = [
    student("Hari", "A123", 7.8),
    student("Srikanth", "A124", 8.9),
    student("Saumya", "A125", 9.1),
    student ("Mahidhar", "A126", 9.9),
]

sorted_students = sorted_students(student)

# print the sorted list of students
for student in sorted_students:
  print("Name: {}, Roll_Number: {}, CGPA: {}".format(student.name,
                                                     student.roll_number,
                                                     
