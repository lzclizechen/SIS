import student
import utils

def getIndex(studentList, id):
    count = 0
    for each in studentList:
        if each.getStudentId() == id:
            return count
        else:
            count += 1

def changeStudent(filepath):
    
    studentList = utils.getAllStudent(filepath)

    if len(studentList) == 0:
        print('没有学生信息！请添加学生信息。')
        return

    id = input('请输入学生ID：')
    idx = utils.searchStudentId(studentList, int(id))

    while idx > int((studentList[-1])[1]):
        id = input('学生信息没有找到， 请输入正确学生ID：')
        idx = utils.searchStudentId(studentList, int(id))

    # 简单起见，只能修改分数。
    grade = input('请更改此学生的成绩：')
    while not utils.checkGrade(grade):
        grade = input("格式错误！请输入正确成绩：")

    studentList[getIndex(studentList, idx)].setStudentGrade(grade) 
    instruct = input('确定保存？ (Y/N)：')
    if instruct.lower() == 'y':  
        f = open(filepath, 'w')
        for stu in studentList:
            f.write(str(stu)+'\n')
        f.close()
        print('保存')
