import student
import utils

def changeStudent(filepath):
    f = open(filepath, 'r')
    studentList = []
    for line in f.readlines():
        stuInfo = line.strip().split()
        stu = student.Student(stuInfo[0],int(stuInfo[1]), int(stuInfo[2]))
        studentList.append(stu)
    f.close()

    if len(studentList) == 0:
        print('没有学生信息！请添加学生信息。')
        return

    id = input('请输入学生ID：')
    idx = utils.searchStudentId(studentList, int(id))
    while idx >= len(studentList):
        id = input('学生信息没有找到， 请输入正确学生ID：')
        idx = utils.searchStudentId(studentList, int(id))

    # 简单起见，只能修改分数。
    grade = input('请更改此学生的成绩：')
    while not utils.checkGrade(grade):
        grade = input("格式错误！请输入正确成绩：")

    studentList[idx].setStudentGrade(grade) 
    instruct = input('确定保存？ (Y/N)：')
    if instruct.lower() == 'y':  
        f = open(filepath, 'w')
        for stu in studentList:
            f.write(str(stu)+'\n')
        f.close()
        print('保存')
