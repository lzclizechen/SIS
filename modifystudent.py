import student
import utils

def getIndex(studentList, id_):
    #print("do_getIndex")
    count = 0
    for each in studentList:
        if each.getStudentId() == id_:
            return count
        else:
            count += 1
    return count

def modifyStudent(filepath):
          
    #print("do_changeStudent")
    studentList = utils.fileRead(filepath)

    if len(studentList) == 0:
        print('没有学生信息！请添加学生信息。')
        return

    id_ = input('请输入学生ID：')
    idx = getIndex(studentList, int(id_))
    #print("id:"+str(id_), " ", "idx:"+str(idx), "len(stu):",str(len(studentList)))
    while idx >= len(studentList):
        id_ = input('学生信息没有找到， 请输入正确学生ID：')
        idx = getIndex(studentList, int(id_))


    choice = input("请选择要修改的内容(0：姓名 1：ID 2：性别 3：年龄 4：班级 5:分数)：").replace(' ', '')

    # 简单起见，只能修改分数。
    if choice == '0':
        name = input('请更改此学生的姓名：').replace(' ', '')
        studentList[idx].setStudentName(name)

    elif choice == '1':
        id_ = input("请输入学生ID： ")
        while not utils.checkId(id_):
            id_=input("格式错误！请输入正确ID格式：")

    elif choice == '2':
        sex = input('请更改此学生的性别：').replace(' ', '')
        studentList[getIndex(studentList, id_)].setStudentSex(sex)

    elif choice == '3':
        age = input('请更改此学生的年龄：')
        while not utils.checkAge(age):
            age = input("格式错误！请输入正确成绩：")

        studentList[getIndex(studentList, id_)].setStudentGrade(grade)

    elif choice == '4':
        class_ = input('请更改此学生的班级：').replace(' ', '')
        studentList[getIndex(studentList, id_)].setStudentClass(class_)

    elif choice == '5':
        grade = input('请更改此学生的成绩：')
        while not utils.checkGrade(grade):
            grade = input("格式错误！请输入正确成绩：")

        studentList[getIndex(studentList, id_)].setStudentGrade(grade)
        
    instruct = input('确定保存？ (Y/N)：')
    if instruct.lower() == 'y':  
        utils.fileWrite(filepath, studentList)
        print('保存')
