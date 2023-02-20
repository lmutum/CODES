class Student:
    school = "Pobbo High"
    def __init__(ten,name,roll_num,mark):
        ten.name = name
        ten.roll_num = roll_num
        ten.mark = mark
        
        
    def Talk(ten):
        print(Student.school, ten.name, ten.roll_num, ten.mark)

p1 =Student("p1",1,99)
p1.Talk()
p2 = Student("p2",2,98)
p2.Talk()