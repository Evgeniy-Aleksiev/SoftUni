from project.person import Person
from project.child import Child

person = Person("Peter", 25)
child = Child("Peter Junior", 5)
print(person.name, "Peter")
print(person.age, 25)
print(child.__class__.__bases__[0].__name__, "Person")
