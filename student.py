class Student():
    def __init__(self, name, id_, sex, age, class_, grade):
        '初始化函数'
        self.name = name
        self.id_ = id_
        self.sex = sex
        self.age = age
        self.class_ = class_
        self.grade = grade

    def __lt__(self, other):
        '自定义比较器，这里使用student id来进行比较排序'
        return (self.grade > other.grade)

    def __str__(self):
        '将一个对象实例转换成一个字符串'
        astring = ("%s\t%d\t%s\t%d\t%s\t%d"
                   %
                   (self.name, self.id_, self.sex, self.age, self.class_, self.grade))
                    
        return astring

    def __getitem__(self,index):
        return index

    def getStudentName(self):
        return self.name
    
    def getStudentId(self):
        return self.id_

    def getStudentSex(self):
        return self.sex

    def getStudentAge(self):
        return self.age

    def getStudentClass(self):
        return self.class_

    def getStudentGrade(self):
        return self.grade

    def setStudentName(self, name):
        self.name = name
    
    def setStudentId(self, id_):
        self.id_ = id_

    def setStudentSex(self, sex):
        self.sex = sex

    def setStudentAge(self, age):
        self.sex = age

    def setStudentClass(self, class_):
        self.class_ = class_

    def setStudentGrade(self, grade):
        self.grade = grade
