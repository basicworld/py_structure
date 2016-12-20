# -*- coding: utf-8 -*-

"""
使用ADT抽象数据类型实现事务管理系统的Person Student Staff类

ADT Person:  #定义人员抽象数据类型
    Person(self, strname, strsex, tuple birthday, str ident)  #构造人员对象
    id(self)   #获取id
    name(self)  #获取姓名
    sex(self)  #获取性别
    birthday(self)  #获取生日
    age(self)  #获取年龄
    set_name(self, str name)  #修改姓名
    <(self, Person another)  #基于人员编号比较两个记录
    details(self)  #给出人员记录里保存的数据详情

ADT Student(Person):
    Student(self, strname, strsex, tuple birthday, str department)  #构造学生对象
    department(self)  #获取院系
    en_year(self)  # 获取入学年度
    scores(self)  # 获取成绩单
    set_course(self, str course_name  # 设置选课
    set_score(self, str course_name, int score)  # 设置分数

ADT Staff(Person):
    Staff(self, strname, strsex, tuple birthday, tuple entry_date)  # 构造教职工对象
    department(self)  # 获取院系
    salary(self)  # 获取工资
    entry_date(self)  # 获取入职时间
    position(self)  # 获取职位
    set_salary(self, int amount)  # 获取工资额

"""
import datetime


class PersonTypeError(TypeError):
    pass


class PersonValueError(ValueError):
    pass


class Person(object):
    _num = 0  # 记录人数

    def __init__(self, name, sex, birthday, ident):
        if not (isinstance(name, str) and sex in ('male', 'female')):
            raise PersonValueError(name, sex)

        try:
            birth = datetime.date(*birthday)
        except:
            raise PersonValueError('wrong date', birthday)

        self._name = name
        self._sex = sex
        self._birthday = birth
        self._id = ident
        Person._num += 1

    def id(self):
        return self._id

    def name(self):
        return self._name

    def sex(self):
        return self._sex

    def birthday(self):
        return self._birthday

    def age(self):
        return datetime.date.today().year - self._birthday.year

    def set_name(self, name):
        if not isinstance(name, str):
            raise PersonValueError('set_name', name)
        self._name = name

    def __lt__(self, another):
        if not isinstance(another, Person):
            raise PersonTypeError(another)
        return self._id < another.id()

    def __str__(self):
        return self.details()

    @classmethod
    def num(self):
        return Person._num

    def details(self):
        return ', '.join(('ID：' + self._id,
                         '姓名：' + self._name,
                         '性别：' + self._sex,
                         '生日：' + str(self._birthday)))


class Student(Person):
    _id_num = 0  # 学生类id

    @classmethod
    def _id_gen(cls):
        """自动生成学生id"""
        cls._id_num += 1
        year = datetime.date.dotay().year
        return '1{:04}{:05}'.format(year, cls._id_num)

    def __init__(self, name, sex, birthday, department):
        Person.__init__(self, name, sex, birthday, Student._id_gen())
        self._department = department
        self._enroll_date = datetime.date.today()
        self._courses = {}

    def set_course(self, course_name):
        """设置课程"""
        self._courses[course_name] = None

    def set_score(self, course_name, score):
        """设置分数"""
        if course_name not in self._courses:
            raise PersonValueError('No this course:', course_name)
        self._courses[course_name] = score

    def scores(self):
        return self._courses.items()

    def details(self):
        return ', '.join((Person.details(self),
                         '学院：' + (self._department)))


class Staff(Person):
    _id_num = 0

    @classmethod
    def _id_gen(cls, birthday):
        cls._id_num += 1
        birth_year = datetime.date(*birthday).year
        return '0{:04}{:05}'.format(birth_year, cls._id_num)

    def __init__(self, name, sex, birthday, entry_date=None):
        super(Staff, self).__init__(name, sex, birthday, Staff._id_gen(birthday))

        if entry_date:
            try:
                self._entry_date = datetime.date(*entry_date)
            except:
                raise PersonValueError('Wrong date:', entry_date)
        else:
            self._entry_date = datetime.date.today()

        self._salary = 1720
        self._department = 'None'
        self._position = 'None'

    def set_salary(self, amount):
        if not isinstance(amount, int):
            raise TypeError
        self._salary = amount

    def set_position(self, position):
        if not isinstance(position, str):
            raise TypeError
        self._position = position

    def details(self):
        return ', '.join((Person.details(self),
                         '职位：' + (self._position)))



if __name__ == '__main__':
    p = Person('wlfei', 'male', (2010,1,1), '13')
    print p
    print p.age()
    p2 = Person('xiaoming', 'male', (2011,1,1), '12')
    print Person.num()

    s1 = Staff('Mr zhang', 'male', (1991,1,1))
    s1 = Staff('Mr wang', 'female', (1994,1,1))
    print s1
    s1.set_position('professor')

    # import doctest
    # doctest.testmod(verbose=True)
