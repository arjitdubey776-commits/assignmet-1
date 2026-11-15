class Grandparent:
    def show_grandparent(self):
        print("This is the grandparent class")

class Parent(Grandparent):
    def show_parent(self):
        print("This is the parent class")

class Child(Parent):
    def show_child(self):
        print("This is the child class")

obj = Child()
obj.show_grandparent()
obj.show_parent()
obj.show_child()
