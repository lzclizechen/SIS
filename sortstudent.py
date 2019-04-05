import student
import utils

def printStudent(student):
    print('姓名\tID\t性别\t年龄\t成绩\t班级')
    print(student)

def printAll(studentList):
    print('姓名\tID\t性别\t年龄\t成绩\t班级')
    for each in studentList:
        print(each)

def sortStudent(filepath):

    studentList = utils.fileRead(filepath)
    if len(studentList) == 0:
        print('没有学生信息！请添加学生信息。')
        return

    sortStandard = input("请输入排序方式或退出（姓名、年龄、学号、班级、性别、成绩、退出）：").replace(" ", "") 
    
    if sortStandard == "姓名":
        sortedStudentList = sorted(studentList,
                                   key = lambda stut:stut.getStudentName(),
                                   reverse = True)
    elif sortStandard == "年龄":
        sortedStudentList = sorted(studentList,
                                   key = lambda stut:stut.getStudentAge(),
                                   reverse = True)
    elif sortStandard == "学号":
        sortedStudentList = sorted(studentList,
                                   key = lambda stut:stut.getStudentId(),
                                   reverse = True)
    elif sortStandard == "班级":
        sortedStudentList = sorted(studentList,
                                   key = lambda stut:stut.getStudentClass(),
                                   reverse = True)
    elif sortStandard == "性别":
        sortedStudentList = sorted(studentList,
                                   key = lambda stut:stut.getStudentSex(),
                                   reverse = True)
    elif sortStandard == "成绩":
        sortedStudentList = sorted(studentList,
                                   key = lambda stut:stut.getStudentSex(),
                                   reverse = True)
    elif sortStandard == "退出":
        return
    else:
        print("输入有误，默认按成绩排序！\n")
        sortedStudentList = sorted(studentList,
                                   key = lambda stut:stut.getStudentSex(),
                                   reverse = True)
        
    printAll(sortedStudentList)


