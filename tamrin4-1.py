class Student:

    def __init__(self, first_name, last_name, national_number, student_number, GPA , age ):
        self.first_name = first_name 
        self.last_name = last_name
        self.age = age 
        self.national_number = national_number
        self.student_number =  student_number
        self.GPA = GPA
    
    def get_age(self):
        return ("The "+self.first_name + 's age is ' + str(self.age))

    def get_firsr_name(self):
        return ("The first name: "+ self.first_name)

student_1 = Student('Mehdi', 'Norozi' ,  '00222240082013' , 3560253170 , 19 , 25)
student_2 = Student('Alireza', 'Nikouei' ,  '00222240082012' , 3560253180 ,18 , 23)
student_3 = Student('Ruhollah', 'Sharif' ,  '02121040709021' ,'3560253160' , 17 , 21)

print(student_3.get_firsr_name())
print(student_3.get_age())
