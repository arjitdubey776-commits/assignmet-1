class Parent:
    def show_parent(self):
        print("This is the parent class")

class ChildOne(Parent):
    def show_one(self):
        print("This is child one")

class ChildTwo(Parent):
    def show_two(self):
        print("This is child two")

first = ChildOne()
second = ChildTwo()

first.show_parent()
first.show_one()
second.show_parent()
second.show_two()
