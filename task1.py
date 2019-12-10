class Student():
    def __init__(self, name, lastname, depatment, year_of_entrance):
        self.name=name
        self.lastname=lastname
        self.depatment=depatment
        self.year_of_entrance=year_of_entrance


    def info(self):
        return f'{self.name}, {self.lastname}, поступил в{self.year_of_entrance}, на факультет{self.depatment}'


student1=Student('Vasia', 'Ivanov', 'Programm', 2017)
print(student1.info())


student2=Student('Sergey', 'Sokolov', 'low', 2018)
print(student2.info())


