import student
import utils

def deleteStudent(filepath):
    f = open(filepath, 'r')
    studnetList = []
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


    instruct = input('确定删除? (Y/N)：')
    if instruct.lower() == 'y':
        del studentList[idx]
  
        f = open(filepath, 'w')
        for stu in studentList:
            f.write(str(stu)+'\n')
        f.close()
        print('保存')
