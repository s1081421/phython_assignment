name="陳俊維"
age=20
height=180
weight=60
def BMI (h,w):
    return(float(w/h/h*100*100))

class Question:
    def __init__(self,description,answer):
        self.description=description
        self.answer=answer

class Person:
    def __init__(self,name,age):
        self.name=name
        self.age=age
    def person_name(self):
        print(self.name)
    def person_age(self):
        print(self.age)
