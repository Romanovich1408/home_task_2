import datetime
MAX_STUDENTS = 10

class Person:

    def __init__(self, name: str, surname: str, date_of_birth: str):
        """
        :param name:
        :param surname:
        :param date_of_birth: YYYY/MM/DD        
        """
        self.name = name
        self.surname = surname
        self.date_of_birth = date_of_birth

    def __str__(self):
        age = datetime.datetime.now().year - datetime.date(*map(int, self.date_of_birth.split("/"))).year  # вычисление возраста припомощи datetime
        return f"{self.name} {self.surname}, {age} years"  

class Student(Person):

    def __init__(self, name: str, surname: str, date_of_birth: str, sex: str):
        super().__init__(name, surname, date_of_birth)
        self.sex = sex

        def __str__(self):
            res = super().__str__()
            return f"{res}: {self.sex}"

class Group:

    def __init__(self, spec, entrance_year, students=None):
        self.spec = spec
        self.entrance_year = entrance_year
        self.__students = students or []

    def add_student(self, student: Student):
        if len(self.__students) == MAX_STUDENTS:
            return None
        for item in self.__students:
            if (item.surname, item.name, item.date_of_birth) == (student.surname, student.name, student.date_of_birth):
                return None
        self.__students.append(student)

    def __str__(self):
        res =  "\n".join(map(str, self.__students))
        return f"{self.spec}: {self.entrance_year}\nStudents:\n{res}"


if __name__ == "__main__":

      x = Student("Ivan", "Ivanov", "1988/08/14", "M")
      y = Student("Petr", "Petrov", "1991/01/21", "M")

      group = Group("CS", "2006")
      group.add_student(x)
      group.add_student(y)

      print(group)