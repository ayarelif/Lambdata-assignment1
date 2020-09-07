# attributes/properties
# behaviors/methods
# my_lanbdata/new_class.py

class name():
    pass
    def __init__(self,gender,height,age,style="Normal Fit"):
        self.gender=gender
        self.height=height
        self.age=age

    def fold(self):
        print("Folding the {self.height.upper()} {self.age.upper()} person here")
    



if __name__=="__main__":

    #df=DataFrame({"abbrev":["EA","VA","MA","HA","EAY","HAY"]})

    person=name("Female",5.2,40)
    print(person.gender, person.height, person.age)
    person.fold()

    person2=name(gender="Female",height=5.4,age=30)
    print(person2.gender, person2.height, person2.age)
    person.fold()

    person3=name(gender="Male",height=5.0,age=35, style="Fit Cut")
    print(person3.gender, person3.height, person3.age)
    person.fold()
