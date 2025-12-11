class Student:
    def __init__(self, name, gpa):
        self.name = name
        self.gpa = float(gpa)
    def on_honour_roll(self):
        if self.gpa >= 4.4 :
            return True
        else:
            return False
