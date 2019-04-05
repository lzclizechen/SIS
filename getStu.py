import random

with open('student.txt','a') as f:
    for i in range(0, 101):
        name = "stu"+str(i)
        id_ = 2000 + i
        sex = "男" if random.randint(0,1) else "女"
        age = random.randint(16,26)
        class_ = str(random.randint(1,4))+"-"+str(random.randint(1,5))
        grade = random.randint(80,100)
        f.writelines("%s\t%d\t%s\t%d\t%s\t%d\n" % (name, id_, sex, age, class_, grade))
