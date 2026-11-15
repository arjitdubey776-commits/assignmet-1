class Employee:
    def __init__(self, salary):
        self.__salary = salary

    def show_salary(self):
        print("Salary:", self.__salary)

    def update_salary(self, salary):
        if salary > 0:
            self.__salary = salary
        else:
            print("Salary must be positive")

employee = Employee(30000)
employee.show_salary()
employee.update_salary(35000)
employee.show_salary()
