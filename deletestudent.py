import student
import utils

def deleteStudent(filepath):
    
    studentList = utils.fileRead(filepath)

    if len(studentList) == 0:
        print('没有学生信息！请添加学生信息。')
        return

    id = input('请输入学生ID：')
    idx = utils.searchStudentId(studentList, int(id))
    while idx > int(studentList[-1][1]):
        id = input('学生信息没有找到， 请输入正确学生ID：')
        idx = utils.searchStudentId(studentList, int(id))


    instruct = input('确定删除? (Y/N)：')
    if instruct.lower() == 'y':
        del studentList[idx]

        fileWrite(filepath, studentList)
        
        print('保存')
