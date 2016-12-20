# 抽象数据类型ADT


Python的基本数据类型

python的组合数据类型：list等

抽象数据类型就是将对象的使用与其具体实现完全隔离开

一个数据类型的操作通常分为3类：

1. 构造操作
2. 解析操作
3. 变动操作

ADT是一种思想，也是一种组织程序的技术

# python的类（面向对象技术）

python里没有直接的ADT定义，实现ADT可以采用很多不同的技术，如class

python没有隐藏抽象的内部信息的方法，只能依靠一些编程约定：

1. 下划线考口的属性或函数名当做内部名字，不应该在外部使用
2. class的特殊函数
3. 静态方法除了没有self，其他方面与实例方法相同，本质上就是类内的局部普通函数
4. 类方法通常用来实现与本类的所有对象有关的操作
5. 对于类而言，在类里定义的名字，其作用域并不自动延伸到类内部嵌套的作用域。类中函数在引用类的属性的时候需要基于类名的属性引用方式
6. 函数内定义的属性的作用域自动延伸到内部嵌套函数

## 继承

相关概念：继承、积累、派生类

派生类需要重新定义 `__init__`函数，完成对该类实例的初始化

python的继承中，实例对函数的调用采用了**动态约束**，即总是优先查找实例对象所属的类中有没有该函数

`super().__init__()`只能用于有`(object)`标示的新式类，不能用于经典类

```
class Person(object):
    _num = 0  # 记录人数

    def __init__(self, name, sex, birthday, ident):
		pass
		
		
class Staff(Person):
    _id_num = 0

    @classmethod
    def _id_gen(cls, birthday):
        cls._id_num += 1
        birth_year = datetime.date(*birthday).year
        return '0{:04}{:05}'.format(birth_year, cls._id_num)

    def __init__(self, name, sex, birthday, entry_date=None):
        super(Staff, self).__init__(name, sex, birthday, Staff._id_gen(birthday))

```


# NOTE

1. python为各种运算符提供了特殊方法，如 `__add__,__sub__,__mul__,__truediv__(/),__mod__(%),__eq__(==),__lt__`