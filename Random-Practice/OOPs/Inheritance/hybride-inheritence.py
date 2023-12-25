class University:
    uni_name = "North South University"
    def __init__(self, name) -> None:
        self.name = name
        
        
    def showDetails(self):
        print(f"The Universiy Name is: {self.uni_name} and My Name: {self.name}")
    
    
class Course(University):
    def __init__(self, name, course_name) -> None:
        super().__init__(name)
        self.course_name = course_name
        
    def showDetails(self):
        print(f"{super().showDetails()} and Course name: {self.course_name} ")
        
        

class Branch(University):
    def __init__(self, name, branch_name) -> None:
        super().__init__(name)
        self.branch_name = branch_name
        
    def showDetails(self):
        print(f"{super().showDetails()}, and Branch Name: {self.branch_name}")
        

class Student(Course, Branch):
    def __init__(self, name, course_name, branch_name, s_id) -> None:
        Course.__init__(self, name, course_name)
        Branch.__init__(self, name, branch_name)
        self.studentID = s_id
        
        
    # def showDetails(self):
    #     print(f"student id: {self.studentID}")
    #     print(super().showDetails())
    
    def showDetails(self):
        print(f"student id: {self.studentID}")
        Course.showDetails(self)
        Branch.showDetails(self)
        

class Faculty(Branch):
    def __init__(self, name, branch_name, fac_id) -> None:
        super().__init__(name, branch_name)
        self.faculty_ID = fac_id
        
        
    def showDetails(self):
        print(f'{super().showDetails()}, and Faculty id: {self.faculty_ID}')
        
        

stu_1 = Student("Md Al Amin", 'Python OOPs', 'Computer Science', '1811904042')
stu_1.showDetails()
    