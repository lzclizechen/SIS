import utils

def addStudent(filepath):
    print('请输入学生信息，其中ID为四位数字')

    # 输入新增学生信息：姓名、学号和成绩
    name = input("请输入学生姓名： ").replace(' ', '')
    id = input("请输入学生ID： ")
    while not utils.checkId(id):
        grade=input("格式错误！请输入正确ID格式：")
    grade = input("请输入学生成绩： ")
    while not utils.checkGrade(grade):
        grade=input("格式错误！请输入正确成绩格式：")
        

    print('你已经成功添加：')
    print('姓名：', name, '，ID：', id, '成绩：', grade)
    instruct = input('保存？ （Y/N）： ')
    if instruct.lower() == 'y' :
        f = open(filepath, 'a')
        f.write(name + '\t' + id + '\t' + grade + '\n')
        f.close()
        print('保存...')
