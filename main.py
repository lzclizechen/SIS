import os
import addstudent
import deletestudent
import sortstudent
import modifystudent

filepath = 'student.txt'

def main():
    if not os.path.isfile(filepath):
        open(filepath, 'a').close()

    while True:
        print('\n\n')
        print(' ------------------学生信息管理系统------------------ ')
        print('|  菜单                                              |')
        print('|  1：添加学生信息                                   |')
        print('|  2：删除学生信息                                   |')
        print('|  3：更改学生信息                                   |')
        print('|  4：给学生排序                                     |')
        print('|  5：使用帮助                                       |')
        print('|  0：退出                                           |')
        print(' ---------------------------------------------------- ')

        instruction = input("请输入选项： ")
        if instruction == "0":
            exit(0)
        elif instruction == '1':
            addstudent.addStudent(filepath)
        elif instruction == '2':
            deletestudent.deleteStudent(filepath)
        elif instruction == '3':
            modifystudent.modifyStudent(filepath)
        elif instruction == '4':
            sortstudent.sortStudent(filepath)
        else:
            print('输入错误！ 请输入正确选项。')

if __name__ == '__main__':
    main()
