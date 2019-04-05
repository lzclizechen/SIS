import student

def searchStudentId(studentList, id_):
    '查找需要操作的学生ID'
    print("do_searchStudentId")
    idx = 0
    for stu in studentList:
        if stu.getStudentId() == int(id_):
            return idx
        else:
            idx += 1

    return idx
    
def searchStudentName(studentList, name):
    '查找需要操作的学生姓名'
    idx = 0
    for stu in studentList:
        if stu.getStudentName() == name:
            return name
        else:
            print("没有此学生信息或输入的格式不正确！\n")
            name = ''

    return name



def fileRead(filepath):
    '读入存储学生信息的文件， 将所有学生信息读入内存'
    f = open(filepath, 'r')
    studentList = []

    for line in f.readlines():
        stuInfo = line.strip().split()
        stu = student.Student(stuInfo[0],int(stuInfo[1]), stuInfo[2], int(stuInfo[3]), stuInfo[4], int(stuInfo[5]))
        studentList.append(stu)
    f.close()
    return studentList

def fileWrite(filepath, studentList):
    '将存储学生信息的列表写入文件中'
    f = open(filepath, 'w')
    for stu in studentList:
        f.write(str(stu) + '\n')
    f.close()


def checkId(id_):
    '检查学号为4位且全是数字'
    if len(id_) == 4 and id_.isdigit():
        return True
    else:
        return False

def checkAge(age):
    '检查学号为4位且全是数字'
    if 0 < len(age) < 3 and age.isdigit():
        return True
    else:
        return False

def checkGrade(grade):
    '检查输入成绩是否符合要求，这里假设成绩是0到100之间的整数'
    if grade.isdigit() and int(grade) >= 0 and int(grade) < 101:
        return True
    else:
        return False


