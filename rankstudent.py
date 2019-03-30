import student
import utils

def rankStudent(filepath):
    
    studentList = utils.getAllStudent(filepath)
    

    if len(studentList) == 0:
        print('没有学生信息！请添加学生信息。')
        return

    # 方法1：使用lamda表达式给学生排序，成绩由高到低
    sortedStudentList = sorted(studentList, key = lambda stut:stut.getStudentGrade(), reverse=True)
    
    # 方法2：Student类中，__lt__ 函数比较
    #sortedStudentList = sorted(studentList)
    print('姓名\tID\t成绩')
    for stu in sortedStudentList:
        print(stu.getStudentName() + '\t' + str(stu.getStudentId()) + '\t' + str(stu.getStudentGrade()))
    
