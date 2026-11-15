class Father:
    def father_skill(self):
        print("Father knows driving")

class Mother:
    def mother_skill(self):
        print("Mother knows cooking")

class Child(Father, Mother):
    def child_skill(self):
        print("Child knows programming")

obj = Child()
obj.father_skill()
obj.mother_skill()
obj.child_skill()
