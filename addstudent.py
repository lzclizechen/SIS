import utils

def addStudent(filepath):
    print('请输入学生信息，其中学号为四位数字')

    # 输入新增学生信息：姓名、学号和成绩
    name = input("请输入学生姓名： ").replace(' ', '')
    
    id_ = input("请输入学生学号： ")
    while not utils.checkId(id_):
        id_=input("格式错误！请输入正确学号格式：")

    sex = input("请输入学生性别： ").replace(' ', '')

    age = input("请输入学生年龄： ")
    while not utils.checkAge(age):
        grade=input("格式错误！请输入正确年龄格式：")

    class_ = input("请输入学生班级： ").replace(' ', '')
    
    grade = input("请输入学生成绩： ")
    while not utils.checkGrade(grade):
        grade=input("格式错误！请输入正确成绩格式：")
        
    print('你已经成功添加：')
    print('姓名：', name,
          '，学号：', id_,
          '，性别：', sex,
          '，年龄：', age,
          '，班级：', class_,
          ', 成绩：', grade)
    
    instruct = input('保存？ （Y/N）： ')
    if instruct.lower() == 'y' :
        f = open(filepath, 'a')
        f.write(name 
                + '\t' + id_
                + '\t' + sex
                + '\t' + age
                + '\t' + class_
                + '\t' + grade + '\n')
        f.close()
        print('保存...')
