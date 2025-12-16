#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
基础类示例
演示 Python 中的类和对象
"""


class Person:
    """人员类 - 演示封装"""

    # 类变量（所有实例共享）
    species = "智人"

    def __init__(self, name, age):
        """初始化方法"""
        # 实例变量（每个实例独有）
        self.name = name
        self.age = age

    def introduce(self):
        """自我介绍方法"""
        return f"大家好，我叫{self.name}，今年{self.age}岁"

    def have_birthday(self):
        """生日方法 - 增加年龄"""
        self.age += 1
        print(f"{self.name} 生日快乐！现在 {self.age} 岁")

    @classmethod
    def from_string(cls, person_str):
        """类方法 - 从字符串创建对象"""
        name, age = person_str.split(',')
        return cls(name, int(age))

    @staticmethod
    def is_adult(age):
        """静态方法 - 判断是否成年"""
        return age >= 18

    def __str__(self):
        """字符串表示"""
        return f"Person(name={self.name}, age={self.age})"

    def __repr__(self):
        """开发者表示"""
        return self.__str__()


class Student(Person):
    """学生类 - 演示继承"""

    def __init__(self, name, age, grade):
        """初始化学生对象"""
        super().__init__(name, age)
        self.grade = grade

    def study(self, subject):
        """学习方法"""
        return f"{self.name} 正在学习 {subject}"

    def introduce(self):
        """重写父类方法 - 多态"""
        return f"大家好，我叫{self.name}，今年{self.age}岁，{self.grade}年级"


class Teacher(Person):
    """教师类 - 演示继承和多态"""

    def __init__(self, name, age, subject):
        """初始化教师对象"""
        super().__init__(name, age)
        self.subject = subject

    def teach(self):
        """教学方法"""
        return f"{self.name} 老师正在教 {self.subject}"

    def introduce(self):
        """重写父类方法"""
        return f"大家好，我是{self.name}老师，今年{self.age}岁，教{self.subject}"


def main():
    """演示类和对象的使用"""
    # 创建 Person 对象
    print("=== Person 类 ===")
    person1 = Person("张三", 25)
    person2 = Person("李四", 30)

    print(person1.introduce())
    print(person2.introduce())
    print()

    print(f"{person1.name} 是成年人吗？{Person.is_adult(person1.age)}")
    print(f"{person2.name} 是成年人吗？{Person.is_adult(person2.age)}")
    print()

    # 使用类方法创建对象
    print("=== 使用类方法 ===")
    person3 = Person.from_string("王五,28")
    print(person3.introduce())
    print()

    # 创建 Student 对象
    print("=== Student 类（继承）===")
    student = Student("小明", 16, "高一")
    print(student.introduce())
    print(student.study("数学"))
    print()

    # 创建 Teacher 对象
    print("=== Teacher 类（继承）===")
    teacher = Teacher("王老师", 35, "物理")
    print(teacher.introduce())
    print(teacher.teach())
    print()

    # 多态示例
    print("=== 多态示例 ===")
    people = [person1, student, teacher]
    for person in people:
        print(person.introduce())
    print()

    # 使用生日方法
    print("=== 使用生日方法 ===")
    person1.have_birthday()
    student.have_birthday()
    print()

    # 对象信息
    print("=== 对象信息 ===")
    print(f"Person 对象: {person1}")
    print(f"Student 对象: {student}")
    print(f"Teacher 对象: {teacher}")
    print()


if __name__ == "__main__":
    main()
